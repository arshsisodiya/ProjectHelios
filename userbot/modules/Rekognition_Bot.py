import asyncio
import glob
import os
import time
from asyncio.exceptions import TimeoutError
import requests
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP
from userbot.events import register
from userbot.utils import progress

@register(outgoing=True, pattern=r"^\.recognize")
async def _(event):
    "To recognize a image."
    if not event.reply_to_msg_id:
        return await edit(event, "Reply to any user's media message.")
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        return await edit_or_reply(event, "reply to media file")
    chat = "@Rekognition_Bot"
    if reply_message.sender.bot:
        return await event.edit("Reply to actual users message.")
    cat = await event.edit(event, "recognizeing this media")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("unblock @Rekognition_Bot and try again")
            return
        if response.text.startswith("See next message."):
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            response = await response
            msg = response.message.message
            await event.edit(msg)
        else:
            await event.edit("sorry, I couldnt find it")
        await event.client.send_read_acknowledge(conv.chat_id)
CMD_HELP.update(
    {
        "\n\n .recognize <reply to any image>"
        "\nUsage: Get information about an image using AWS Rekognition. Find out information including detected labels, faces. text and moderation tags)"
    }
)