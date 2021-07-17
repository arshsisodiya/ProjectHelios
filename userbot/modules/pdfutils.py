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

@register(outgoing=True, pattern=r"^\.pdf (?:(photo)|(.*) - (.*))")
async def _(event):
    "."
    if event.pattern_match.group(1) == "photo":
     if not event.reply_to_msg_id:
        return await event.edit("Reply to any user's media message.")
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        return await event.edit(event, "reply to media file")
    chat = "@pdfbot"
    await event.edit("converting your photos into pdf please send another photo via command `.pdf photo2`")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                photocmd = await conv.send_message("/photo")
                photo = await event.client.send_message(chat, reply_message)
                response = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@pdfbot` and retry`")
                return
            await sleep (30)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id, photocmd.id, photo.id,response.id]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Error: `@pdfbot` is not responding try again after some time")

@register(outgoing=True, pattern=r"^\.pdfphoto(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    msg_link = await event.get_reply_message()
    d_link = event.pattern_match.group(1)

    if msg_link:
        d_link = msg_link.media
        await event.edit("`sending...`")
    chat = "@pdfbot"
    await event.edit("`sending.........`")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(d_link)
                await sleep(2)
                torrent = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@pdfbot` and retry`")
                return
            await event.client.send_message(event.chat_id, torrent,)
            await event.client.delete_messages(
                conv.chat_id, [msg.id, torrent.id]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit("`Error: `@pdfbot` is not responding please try again later")

@register(outgoing=True, pattern=r"^\.pdf (?:(photof)|(.*) - (.*))")
async def _(event):
    "."
    if event.pattern_match.group(1) == "photof":
     if not event.reply_to_msg_id:
        return await event.edit("Reply to any user's media message.")
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        return await event.edit(event, "reply to media file")
    chat = "@pdfbot"
    await event.edit("converting your photos into pdf please wait.........")
    try:
        async with bot.conversation(chat) as conv:
            try:
                photo = await event.client.send_message(chat, reply_message)
                donecmd = await conv.send_message("To PDF")
                response = await conv.get_response()
                fresponse = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@pdfbot` and retry`")
                return
            await event.client.send_message(event.chat_id, fresponse)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id, fresponse.id]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Error: `@pdfbot` is not responding try again after some time")

