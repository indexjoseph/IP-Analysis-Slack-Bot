from re import A
import slack, os 
from dotenv import load_dotenv
from pathlib import Path
from slackeventsapi import SlackEventAdapter
from flask import Flask


env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], "/slack/events", app)

# print("Hello! This is a slack bot that has the abilities to receieve and send messages!")
# print("\n" + "Please Enter a Message you would like to the bot to send")


# client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
# chatText = str(input())
# client.chat_postMessage(channel='#response-zone', text=chatText)

if __name__ == "__main__":
    app.run(debug=True)