from queue import Empty
from re import A
from urllib import response
import slack, os, re, requests, json
import re
from dotenv import load_dotenv
from pathlib import Path
from slackeventsapi import SlackEventAdapter
from flask import Flask

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], "/slack/events", 
app)

# print("Hello! This is a slack bot that has the abilities to receieve and send messages!")
# print("\n" + "Please Enter a Message you would like to the bot to send")

# chatText = str(input())

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']
@slack_event_adapter.on("message")


def message(payload):
    event = payload.get("event", {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    if user_id != BOT_ID:
        whole_text = text.split()
        addresses = checkForIPAddresses(whole_text)
    response = "Hey there! There was one or more IP Addresses found in the message previously sent."
    if len(addresses) > 0 and user_id != BOT_ID:
        client.chat_postMessage(channel=channel_id, text=response)
        for address in addresses:
             client.chat_postMessage(channel=channel_id, text="\n\nIP Address: " + address)
             analysis = cleanJsonOutput(getIPInformation(address))
             client.chat_postMessage(channel=channel_id, text=analysis)


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

def getIPInformation(location):
    
    url = "https://www.virustotal.com/api/v3/ip_addresses/" + location
    headers = {
        "Accept": "application/json",
        "x-apikey":
        "a8a9120c6ef5ddf3791bca1719350d1f9157a392c209089730b6d6a13a58aaf9"
    }

    response = requests.get(url, headers=headers)

    return response.text

def cleanJsonOutput(data):
    analysis = json.loads(data)
    analysisCMC = analysis["data"]["attributes"]["last_analysis_results"]["CMC Threat Intelligence"]
    returnText = str(analysis["data"]["attributes"]["whois"]) + "\n"
    for keys in analysisCMC:
        returnText += " " + str(keys).capitalize() + " : " + str(analysisCMC[keys]).capitalize() + " "
    return returnText

if __name__ == "__main__":
    app.run(debug=True)