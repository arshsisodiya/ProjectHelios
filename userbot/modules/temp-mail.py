# Copyright (C) 2021 arshsisodiya
#https://github.com/arshsisodiya
#https://twitter.com/arshsisodiya

#Created by arshsisodiya for ProjectHelios

import asyncio
from asyncio import sleep
from asyncio.exceptions import TimeoutError
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, bot
from userbot.events import register

@register(outgoing=True, pattern=r"^\.tempmail (?:(n)|(.*) - (.*))")
async def _(event):
 await event.edit("`Getting your temporary email`")
 if event.pattern_match.group(1) == "n":
    chat = "@TempMail_org_bot"
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                response = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@TempMail_org_bot` and retry`")
                return
            await event.client.send_message(event.chat_id, response)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id,]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Error: `@TempMail_org_bot` is not responding try again after some time")


@register(outgoing=True, pattern=r"^\.tempmail (?:(r)|(.*) - (.*))")
async def _(event):
 await event.edit("`Refeshing Your Inbox`")
 if event.pattern_match.group(1) == "r":
    chat = "@TempMail_org_bot"
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("Refresh inbox")
                response = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@TempMail_org_bot` and retry`")
                return
            await event.client.send_message(event.chat_id, response)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id, ]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Error: `@TempMail_org_bot` is not responding try again after some time")

@register(outgoing=True, pattern=r"^\.tempmail (?:(new)|(.*) - (.*))")
async def _(event):
 await event.edit("`Generating new Temp-Mail`")
 if event.pattern_match.group(1) == "new":
    chat = "@TempMail_org_bot"
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("Generate new")
                response = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@TempMail_org_bot` and retry`")
                return
            await event.client.send_message(event.chat_id, response)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id,]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Error: `@TempMail_org_bot` is not responding try again after some time")

@register(outgoing=True, pattern=r"^\.tempmail (?:(s)|(.*) - (.*))")
async def _(event):
 await event.edit("`Getting mails from your Temp-Mail Inbox.......`")
 if event.pattern_match.group(1) == "s":

    chat = "@TempMail_org_bot"
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("Show email")
                response = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@TempMail_org_bot` and retry`")
                return
            await event.client.send_message(event.chat_id, response)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id,]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Error: `@TempMail_org_bot` is not responding try again after some time")

@register(outgoing=True, pattern=r"^\.tempmail (?:(d)|(.*) - (.*))")
async def _(event):
 await event.edit("`Deleting your old Temp-Mail and Creating new`")
 if event.pattern_match.group(1) == "d":

    chat = "@TempMail_org_bot"
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("Delete")
                response = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@TempMail_org_bot` and retry`")
                return
            await event.client.send_message(event.chat_id, response)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id,]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Error: `@TempMail_org_bot` is not responding try again after some time")


CMD_HELP.update(
    {
        "TempMail": ".tempmail n"
        "\nUsage: Create your Temporary Email "
        "\n\n.tempmail new"
        "\nUsage:create new Temporary Email"
        "\n\n.tempmail r"
        "\nUsage: Refresh your Temp mail inbox"
        "\n\n.tempmail s"
        "\nUsage: Show emails from your Temp mail inbox"
        "\n\n.tempmail d"
        "\nUsage: delete your current temporary email and create a new one\n"

    }
)

