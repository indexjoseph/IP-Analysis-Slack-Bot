# ThreatQuotient - *Slack Bot*

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
2. Ensure flask, slackeventsapi, python-dotenv, and requests are installed via PIP
3. Go to https://api.slack.com/apps andd Create A New App From Scratch and give it an app name and connect it to your workspace.
4. Copy your Signing Secret and replace the one in the .env folder.
5. 

### Requirements

For general questions/issues about Slack API platform or its server-side, could you submit questions at https://my.slack.com/help/requests/new instead. :bow:

Please read the [Contributing guidelines](https://github.com/slackapi/python-slack-sdk/blob/main/.github/contributing.md) and [Code of Conduct](https://slackhq.github.io/code-of-conduct) before creating this issue or pull request. By submitting, you are agreeing to those rules.

## APIs

https://api.slack.com/

https://developers.virustotal.com/

