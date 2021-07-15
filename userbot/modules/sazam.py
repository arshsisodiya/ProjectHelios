import asyncio
import io
import os
from pathlib import Path
from ShazamAPI import Shazam
from telethon import types
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url
from userbot import CMD_HELP
from userbot.events import register
from userbot.utils import media_type
from userbot.utils.logger import logging



@register(outgoing=True, pattern=r"^\.sid(?: |$)(.*)")
async def _(event):
    "To reverse search music by bot."
    if not event.reply_to_msg_id:
        return await event.edit("```Reply to an audio message.```")
    reply_message = await event.get_reply_message()
    chat = "@SongIDbot"
    await event.edit("```Identifying the song```")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(reply_message)
            check = await conv.get_response()
            if check.text.startswith("No Match"):
                return await event.edit(
                    "An error while identifying the song. Try to use a 5-10s long audio message."
                )
            await event.edit("Wait just a sec...")
            await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
            message.delete()
        except YouBlockedUserError:
            await event.edit("```Please unblock (@SongIDbot) and try again```")
            return

@register(outgoing=True, pattern=r"^\.sid2(?: |$)(.*)")
async def _(event):
    "To recognize a song."
    if not event.reply_to_msg_id:
        return await event.edit("Reply to any user's media message.")
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        return await event.edit(event, "reply to media file")
    chat = "@SongIDbot"
    if reply_message.sender.bot:
        return await event.edit(event, "Reply to actual users message.")
    await event.edit("recognizeing this media")
    async with bot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            song = await conv.get_response()
            """- don't spam notif -"""
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("`Unblock `@SongIDbot` and retry`")
            return
        await bot.send_file(event.chat_id, song, caption=details.text)
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, response.id, msg.id, details.id, song.id]
        )
        await event.delete()

CMD_HELP.update(
    {
        "shazam": ">`.szm <reply to voice/audio>" "\nUsage: Reverse search audio file using shazam api"}
)