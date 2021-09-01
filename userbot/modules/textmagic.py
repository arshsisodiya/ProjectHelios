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
@register(outgoing=True, pattern=r"^\.txtmagic(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    msg_link = await event.get_reply_message()
    d_link = event.pattern_match.group(1)

    if msg_link:
        d_link = msg_link.text
        await event.edit("`it's Magic`")
    chat = "@TextMagicBot"
    try:
        async with event.client.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                bot_reply = await conv.get_response()
                msg = await conv.send_message(d_link)
                response = await conv.get_response()

                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
                await event.edit(response.text)
            except YouBlockedUserError:
                await event.edit("`Unblock `@TextMagicBot` and retry`")
                return
            await event.client.send_message(event.chat_id, response)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id, msg.id, bot_reply.id]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit("`Error: `@TextMagicBot` is not responding please try again later")



