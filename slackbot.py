import slack, os, re, requests, json, re
from dotenv import load_dotenv
from pathlib import Path
from slackeventsapi import SlackEventAdapter
from flask import Flask

env_path = Path(".") / ".env" # Path to env for tokens
load_dotenv(dotenv_path=env_path) # Loads the .env file variables

app = Flask(__name__) # Web server to handle events from Slack API
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'],
 "/slack/events", 
app) # Allows to program to hhandle events from Slack API

client = slack.WebClient(token=os.environ['SLACK_TOKEN']) # Slack Token to connect
BOT_ID = client.api_call("auth.test")['user_id'] # Retrives BOT ID Number

@slack_event_adapter.on("message") # Handles message events
def message(payload):
    event = payload.get("event", {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    addresses = []
    
    if user_id != BOT_ID and type(text) == str:
        whole_text = text.split()
        addresses = checkForIPAddresses(whole_text)
    
    if len(addresses) > 0 and user_id != BOT_ID:
        client.chat_postMessage(channel=channel_id, 
        text="Hey there! There was one or more IP Addresses found in the"+
        "message previously sent.")
        for address in addresses:
             message = "\n\nIP Address: " + address
             client.chat_postMessage(channel=channel_id, text=message)
             analysis = cleanJsonOutput(getIPInformation(address))
             client.chat_postMessage(channel=channel_id, text=analysis)

"""
@Summary {message} - This method handles each meessage and checks if the
message is from a user that is not the Bot. If so the method will take each word
within the message and put it in an list, where it'll be checked for IP Addresses.
If addresses were found within the message the bot will display a message saying
it found address, and provide an analysis on all IP addresses found.
@Parameter {JSON - payload} - A JSON Object consisting of information about each
message sent within the designated channel.
"""

def checkForIPAddresses(entire_message):
    
  regex_check = re.compile(
    r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
  )
  
  addresses_found = []
  
  for words in entire_message:
      words = words.rstrip()
      foundIP = regex_check.search(words)
    
      if foundIP:
          addresses_found.append(words)
        
  return addresses_found

"""
@Summary {checkForIPAdresses} - This method if each word matches the regex
pattern for an IP Adresses, if it does match than the word (address) gets
appended to the list.
@Parameter {list - entire_message} - User message that was sent in the 
designated channel.
@Returns {List - addresses_found} - A list of ip addresses found within 
the message.
"""

def getIPInformation(location):
    
    url = "https://www.virustotal.com/api/v3/ip_addresses/" + location
    headers = {
        "Accept": "application/json",
        "x-apikey":
        "a8a9120c6ef5ddf3791bca1719350d1f9157a392c209089730b6d6a13a58aaf9"
    }

    response = requests.get(url, headers=headers)

    return response.text

"""
@Summary {getIPInformation} - This method sends a request to the virustotal 
api to analyze the address and output the information retrieved.
@Parameter {String - location} - The IP Addreess that will be analyzed.
@Returns {String - response.text} - A string consisting of the JSON object
analysis made on the IP address by the virus total API.
"""

def cleanJsonOutput(data):
    analysis = json.loads(data)
    cmc_key = "CMC Threat Intelligence"
    analyze_key = "last_analysis_results"
    analysisCMC = analysis["data"]["attributes"][analyze_key][cmc_key]
    returnText = str(analysis["data"]["attributes"]["whois"]) + "\n"

    for keys in analysisCMC:
        returnText += " " + str(keys).capitalize() + " : " + str(analysisCMC[keys]).capitalize() + " "
        
    return returnText

"""
@Summary {cleanJsonOutput} - This method parses the json output from the virus
total api and takes specific information from the object to output back to the
slack channnel.
@Parameter {String - data} - The JSON object in String form.
@Returns {String - returnText} - A clean formatted message to send.
"""

if __name__ == "__main__":
    app.run(debug=True)
    