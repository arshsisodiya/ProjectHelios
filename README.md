# Project Helios

![logo](https://github.com/arshsisodiya/ProjectHelios/blob/demon/resources/Project_Helios.png)


```
#include <std/disclaimer.h>
/**
    Your Telegram account may get banned.
    I am not responsible for any improper use of this bot
    This bot is intended for the purpose of having fun with memes,
    as well as efficiently managing groups.
    You ended up spamming groups, getting reported left and right,
    and you ended up in a Finale Battle with Telegram and at the end
    Telegram Team deleted your account?
    And after that, then you pointed your fingers at us
    for getting your acoount deleted?
    I will be rolling on the floor laughing at you.
/**
```
Thanks [Prajju](https://github.com/PrajjuS) For Docker Image and Repl.it Session String Generator <br>

[![Build](https://img.shields.io/github/workflow/status/arshsisodiya/ProjectHelios/FailedChecker?style=for-the-badge)](https://github.com/arshsisodiya/ProjectHelios/actions "build")

![Docker_Size](https://img.shields.io/docker/image-size/elytra8/fizfed?style=for-the-badge)

![Docker_Pulls](https://img.shields.io/docker/pulls/elytra8/fizfed?style=for-the-badge)

![Spec](https://img.shields.io/badge/Made%20with-LOVE-black?style=for-the-badge)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Generate String Session
Easy way to get STRING_SESSION.

### Run on repl.it
[![Run repl.it](https://img.shields.io/badge/run-string__session.py-blue?style=flat-square&logo=repl.it)](https://session.uraniumcore.repl.run)

### or Run on your terminal
```
wget https://raw.githubusercontent.com/arshsisodiya/ProjectHelios/demon/terminal_getstring.sh && bash terminal_getstring.sh
```

## How To Host?

The easiest way to deploy this great bot! is click on button below.
Make sure you have an account of heroku and follow all the steps required.

<p align="left"><a href="https://heroku.com/deploy?template=https://github.com/arshsisodiya/ProjectHelios/blob/demon"> <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku" /></a></p>

For further guide you can head to [Arsh Sisodiya](https://t.me/NmberSeven) or read this [guide](https://telegra.ph/How-to-host-a-Telegram-Userbot-07-01-2)

##Detailed guide about vars and deployment
# Hello.
## Myself Arsh
Have a look at my [Repo](https://github.com/arshsisodiya/ProjectHelios) to deploy Helios USERBOT. 
To use user bot we should have an idea about vars.
## Envoirnment VARS.
<details> 
<summary><b>Click Here For More Details</b></summary>

**API_KEY**: you can get this value from the link given below [here](https://telegram.dog/UseTGXBot).

**API_HASH**: automatically you are going to get this value API_KEY .

**STRING_SESSION**: After getting the  values you have to go for the [session generator](https://session.uraniumcore.repl.run) here you are going to get two option as shown Y/N select Y and sign in with phone number in international format as +918999993456.

**HEROKU_MEMEZ**: This Value Should be settled to "True" for deploying on heroku.

**HEROKU_API_KEY**: you can get this value from from the link given below [here](https://dashboard.heroku.com/account).

**HEROKU_APP_NAME**: This Value will be same as you have filled earlier in app named heroku.

**GITHUB_ACCESS_TOKEN**: you can get this Value from the link given below [here](https://github.com/settings/tokens).

**GIT_REPO_NAME**: This value is required to do commits through Userbot.

**COUNTRY**: This value is required for Date , Time and Weather example:India.

**TZ_NUMBER**: If the country name is not set or else showing an error then set this value example:+5.5 .

**TELEGRAPH_SHORT_NAME**: telegraph shortname for graph credits.

**OPEN_WEATHER_MAP_APPID**: you can get your own APPID (API key) from the link given below [here](https://api.openweathermap.org/data/2.5/weather).

**BOTLOG**: Incase  if you want to turn off from the logging, you can click on false.

**BOTLOG_CHATID**: fill the following data using private group id and it works with supergroup. Get id by giving command to haruka /id in the super group fill this value skip getting error.

**PM_AUTO_BAN**: set this to True for PM protection.

**YOUTUBE_API_KEY**: This key required to search in youtube, you will get this from the link given below [here](https://console.cloud.google.com).

**OCR_SPACE_API_KEY**: Required for image to text get OCR API Key for .ocr command. you can also get this from the link given below [here](https://ocr.space/ocrapi).

**REM_BG_API_KEY**: API Key for .rbg command. you can also get this from the link given below  gib  [here](https://www.remove.bg/api).

**ANTI_SPAMBOT**: Kicks spambots from group after they join or when thay  arrive  in groups ,Requires admin powers in groups to kick.

**ANTI_SPAMBOT_SHOUT**: Report spambots to @admins in groups after they join, just in case when you don't have admin powers to kick that shit yourself.

**TMP_DOWNLOAD_DIRECTORY**: don't change this value for better assistance.

**USER_TERM_ALIAS**: Terminal alias name.

**QUOTES_API_TOKEN**: same as quotly but require api token. you can also get token from the link given below
[here](http://antiddos.systems).

**CLEAN_WELCOME**: When a new person joins, the old welcome message will be deleted.

**BIO_PREFIX**: Prefix for Last.FM Module Bio.

**DEFAULT_BIO**: Default profile bio.

**ALIVE_NAME**: Name for .alive command.

**G_DRIVE_CLIENT_ID**: for gdrive values refer to gdrive section below.

**G_DRIVE_CLIENT_SECRET**: Refer to Gdrive section below.

**G_DRIVE_AUTH_TOKEN_DATA**: Refer to Gdrive section below.

**GDRIVE_INDEX_URL**: Gdrive Index Url (Refer to Gdrive section below.)

**LYDIA_API_KEY**: This Module Needs CoffeeHouse API to work. so Join [here](https://telegram.dog/IntellivoidDevhere) and send #activateapi and follow instructions.

**WEATHER_DEFCITY**: City name for weather module.

**LOGSPAMMER**: Set this to True in case you want the error logs to be stored in the userbot log group, instead of spitting out the file in the current chat, requires a valid BOTLOG_CHATID to be set.
</details>

# HEROKU
What is Heroku?
Answer:-Heroku is a cloud platform as a service (PaaS) supporting several programming languages. One of the first cloud platforms, Heroku has been in development since June 2007, when it supported only the Ruby programming language, but now supports Java, Node.js, Scala, Clojure, Python, PHP, and Go.[1][2] For this reason, Heroku is said to be a polyglot platform as it has features for a developer to build, run and scale applications in a similar manner across most languages. Heroku was acquired by Salesforce.com in 2010 for $212 million.
## Want to deploy on HEROKU

 if you Want to make account click [here](https://signup.heroku.com).

if you already have an account or created one now click [here](https://heroku.com/deploy?template=https://github.com/arshsisodiya/ProjectFizilion/blob/demon) for deploying.

Now fill the required values

And Done your userbot should be alive now

## Gdrive
[Click here](https://console.cloud.google.com/flows/enableapi?apiid=drive)

Login to your gmail.com account. It is recommended to use a gmail.com for creating the API.

Select Create a Project, Accept the Terms of Service, and select your Country of Residence.

Click on Agree and Continue button.

Click on Get Credentials button.

In the new screen, scroll down.

 Which API are you using? select Google Drive API from the dropdown.

Where will you be calling the API from? select Other UI (e.g. Windows, CLI tool)

 What data will you be accessing? select User data.

Click on What credentials do you need?

A pop-up will appear.

Click on SET UP CONSENT SCREEN.

A new tab will open.

Give your application name, and logo that should display on the consent screen.

Since this is going to be used for your personal purposes, we do not need verification. 

Google allows the first 100 users to be authenticated without the verification status.

Scroll Down and Click on the Save button.

now you can close this tab, and return to the previous tab.

Click on the Refresh button.

Click on the Create OAuth Client ID button.

Click on the Done button.

The page will get refreshed. 

Click on the Edit button.

Copy the Client ID and Client secret.

Add the Client ID to the G_DRIVE_CLIENT_ID key, in Heroku Environment Variable.

Add the Client secret to the G_DRIVE_CLIENT_SECRET key, in Heroku Environment Variable.

This plugin also requires the BOTLOG_CHATID to be set.

Send a small file, in your BOTLOG_CHATID Group.

[This process should be done after deploying]

Reply .gd to this file.

A link will appear. 

**The below six steps should be done in less than 1 minute.**

Open the link in your browser, and login to the Google Drive account.

All gDrive functionalities will be done on this account.

This need same account which you have created for API in.

After login, it will display a code. 

Reply this code to the in your BOTLOG_CHATID to the message from which you opened link.

It will now give a txt file 

Open and copy code

And set it in G_DRIVE_AUTH_TOKEN_DATA IN HEROKU VAR

Gdrive is now ready to use.

#Gdrve Index

Refer to This Gitlab Repo for Creating and hosting Index
[Gdrive Index Repo](https://gitlab.com/ParveenBhadooOfficial/Google-Drive-Index)

## Youtube
Go [here](https://console.developers.google.com/apis/dashboard)

Open menu

Select same project as gdrive

Reopen menu

In api & services

Select libraries

Search YouTube data

Select YouTube data api

Click on enable api

Open menu and now goto api & services

Select credentials

Now from right side there is three dot button and down from it there is one more same button

Click on button and Create Credentials

Then choose (help me choose)

Same as gdrive but select YouTube data api

Where you will be calling the API from? --> select other ui eg. Windows

What kind of data you will be accessing? --> select public data 

Click on What credentials do I need

It will give a api key now

If not goto menu api&services --> credentials 

And in API Keys section 

There should be one api key 

Open it and copy 

Now paste it to heroku vars with YOUTUBE_API_KEY


## Extras

Want to contact Owner/lead dev click [here](https://telegram.dog/NmberSeven)



## Groups and Support


## Credits

Thanks:
* [RaphielGang](https://github.com/RaphielGang) - Telegram-Paperplane
* [AvinashReddy3108](https://github.com/AvinashReddy3108) - PaperplaneExtended
* [kandnub](https://github.com/kandnub) - TG-UserBot
* [AdekMaulana](https://github.com/adekmaulana) - ProjectBish
* [Mr.Miss](https://github.com/keselekpermen69) - Userbutt
* [GengKapak](https://github.com/GengKapak) - DCLXVI
* [Mkaraniya](https://github.com/mkaraniya) & [Dev73](https://github.com/Devp73) - OpenUserBot
* [MoveAngel](https://github.com/MoveAngel) - One4U

and many more people who aren't mentioned here, but may be found in [Contributors](https://github.com/arshsisodiya/ProjectHelios/graphs/contributors).

## License

This userbot licensed on [Raphielscape Public License](https://github.com/arshsisodiya/ProjectHelios/blob/demon/LICENSE) - Version 1.d, February 2020

Graphics Copyrighted By [Arsh Sisodiya](https://t.me/NmberSeven) © 2021
