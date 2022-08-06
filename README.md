# ThreatQuotient - *Slack Bot*

Author: **Joseph Oladeji**

# Description

**ipAnalysisSlackBot* is a bot that will read messages in the designated channel(s) it has been added to via the `Slack API`,
the bot will scan every message from a user to check for an IP Address using regex. If an IP Address is found the bot will first send
a message in the channel it was sent in. Then it will send an GET Request to the `VirusTotal API` and retrieve information on the IP Address.
Afterwards it will display contextual information based on the IP Address in the channel.

# Date

Date: **08/06/2022** 

## Video Walkthrough

Here's a walkthrough of bot in action:

<img src='https://i.gyazo.com/e54132188f3d78bcdafea839e6b03251.gif'/>

<!-- Replace this with whatever GIF tool you used! -->
GIF created with [Gyazo GIF](https://gyazo.com/en).  

# How do I make create one?
1. Clone this repository onto your local machine and within the slack-bot folder create a folder called ".env"
2. Create a Slack Account at https://slack.com/
3. Create a workspace at https://slack.com/get-started#/landing
4. Make an ngrok acccount and install ngrok.exe at https://ngrok.com/download
5. Enter your command line prompt and ensure that flask (https://pypi.org/project/Flask/) , slackeventsapi (https://pypi.org/project/slackeventsapi/), requests (https://pypi.org/project/requests/), and pathlib (https://pypi.org/project/pathlib/)


## APIs

https://api.slack.com/

https://developers.virustotal.com/

