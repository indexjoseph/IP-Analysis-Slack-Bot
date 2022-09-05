#*Slack Bot*

Author: **Joseph Oladeji**

# Description

**ipAnalysisSlackBot.py** is a bot that will read messages in the designated channel(s) it has been added to via the `Slack API`,
the bot will scan every message from a user to check for an IP Address using regex. If an IP Address is found the bot will first send
a message in the channel it was sent in. Then it will send an GET Request to the `VirusTotal API` and retrieve information on the IP Address.
Afterwards it will display contextual information based on the IP Address in the channel.

# Youtube Walkthrough 

https://www.youtube.com/watch?v=OOdRJM3wnd8&ab_channel=Joseph

# Date

Date: **08/06/2022** 

## Video Walkthrough

Here's a walkthrough of bot in action:

<img src='https://i.gyazo.com/e54132188f3d78bcdafea839e6b03251.gif'/>

<!-- Replace this with whatever GIF tool you used! -->
GIF created with [Gyazo GIF](https://gyazo.com/en).  

## How to set it up for your self

1. Create your Slack workspace
2. Ensure flask, slackeventsapi, slackclient, python-dotenv, and requests are installed via PIP `Example: pip install flask`
3. Go to https://api.slack.com/apps and Create A New App From Scratch and give it an app name and connect it to your workspace.
4. Go to the OAuth Permissions on the left and scroll down to scope and add "channels:history", "channels:read", "channnels:write" are enabled ![image](https://user-images.githubusercontent.com/73621296/183267702-cb2a4a4d-0fbe-41ca-bd93-d2e91c054aa5.png)
7. Look for "OAuth Tokens for your workspace" then ensure to install the bot into your workspace.
8. Copy that OAuth Token and replace the OAuth Token within the .env file.
6. Copy your Signing Secret and replace the one in the .env folder.
7. Go to event subscriptions on thhe left and enable events on your Slack API Website for your bot
8. Go to Basic Information on your Slack API Website for your bot and copy your Signing Secret, go to the .env file and replace the Signing Secret there
9. Ensure you have saved the .env file
10. Run the python script by doing "python .\ipAnalysisSlackBot.py".
11. Download ngrok and run the exe file https://ngrok.com/download
12. In the ngrok CLI run the command "ngrok http 5000"
13. Copy the Forwarding address by highlighting and right clicking it `Example Forwarding address: https://6bed-75-183-210-173.ngrok.io`
14. Go back to the Slack API Website for your app and paste that url and add "/slack/events" to the end `Example: https://6bed-75-183-210-173.ngrok.io/slack/events`
15. Go to subscribe to bot eveents below and add the bot user evennt "message.channels"
16. Go to your slack workspace and add the bot to a channel by just doing @BotName in the chat.
17. Type an example ip address to ensure it's working. (Ensure both the ngrok forwarding address and python script are running)


### Requirements

For general questions/issues about Slack API platform or its server-side, could you submit questions at https://my.slack.com/help/requests/new instead. :bow:

Please read the [Contributing guidelines](https://github.com/slackapi/python-slack-sdk/blob/main/.github/contributing.md) and [Code of Conduct](https://slackhq.github.io/code-of-conduct) before creating this issue or pull request. By submitting, you are agreeing to those rules.

## APIs

https://api.slack.com/

https://developers.virustotal.com/

