from queue import Empty
from re import A
import slack, os
import re
from dotenv import load_dotenv
from pathlib import Path
from slackeventsapi import SlackEventAdapter
from flask import Flask
import json

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
    wholeText = text.split()
    addresses = checkForIPAddresses(wholeText)
    response = "Hey there! There was no IP Addresses found in the message previously sent"
    if len(addresses) > 0:
        response = "Hey There! There was one or more IP Addresses found within the message previously sent"+"\nHere's a list of the addresse(s) found: "
        for address in addresses:
            response += " " + address + " "

    if user_id != BOT_ID:
        client.chat_postMessage(channel=channel_id, text=response)

def checkForIPAddresses(entireMessage):
  regexCheck = re.compile(
    r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
  )
  
  addressesFound = []
  
  for words in entireMessage:
      words = words.rstrip()
      result = regexCheck.search(words)
    
      if result:
          addressesFound.append(words)
        
  return addressesFound


if __name__ == "__main__":
    app.run(debug=True)