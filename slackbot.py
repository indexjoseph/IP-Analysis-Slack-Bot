import slack, os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)
print("Hello! This is a slack bot that has the abilities to receieve and send messages!")
print("\n" + "Please Enter a Message you would like to the bot to send")
chatText = str(input())

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
for i in range(3):
    client.chat_postMessage(channel='#response-zone', text=chatText)