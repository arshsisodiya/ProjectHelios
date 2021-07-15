import asyncio
import io
import os
from pathlib import Path
from ShazamAPI import Shazam
from telethon import types
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url
from userbot import CMD_HELP
from userbot.events import register
from userbot.utils import media_type
from userbot.utils.logger import logging

@register(outgoing=True, pattern=r"^\.szm(?: |$)(.*)")
async def shazamcmd(event):
    "To reverse search song."
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Voice", "Audio"]:
        return await event.edit("__Reply to Voice clip or Audio clip to reverse search that song.__")
    catevent = await event.edit("__Downloading the audio clip...__")
    try:
        for attr in getattr(reply.document, "attributes", []):
            if isinstance(attr, types.DocumentAttributeFilename):
                name = attr.file_name
        dl = io.FileIO(name, "a")
        await event.client.fast_download_file(
            location=reply.document,
            out=dl,
        )
        dl.close()
        mp3_fileto_recognize = open(name, "rb").read()
        shazam = Shazam(mp3_fileto_recognize)
        recognize_generator = shazam.recognizeSong()
        track = next(recognize_generator)[1]["track"]
    except Exception as e:
        return await event.edit("**Error while reverse searching song:**\n__{str(e)}__"
        )
    image = track["images"]["background"]
    song = track["share"]["subject"]
    await event.client.send_file(
        event.chat_id, image, caption=f"**Song:** `{song}`", reply_to=reply
    )
    await event.delete()

@register(outgoing=True, pattern=r"^\.shazam(?: |$)(.*)")
async def _(event):
    "To reverse search music by bot."
    if not event.reply_to_msg_id:
        return await event.edit("```Reply to an audio message.```")
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    await event.edit("```Identifying the song```")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(reply_message)
            check = await conv.get_response()
            if not check.text.startswith("Audio received"):
                return await event.edit(
                    "An error while identifying the song. Try to use a 5-10s long audio message."
                )
            await event.edit("Wait just a sec...")
            result = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("```Please unblock (@auddbot) and try again```")
            return
    namem = f"**Song Name : **`{result.text.splitlines()[0]}`\
        \n\n**Details : **__{result.text.splitlines()[2]}__"
    await event.edit(namem)

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
            result = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("```Please unblock (@SongIDbot) and try again```")
            return
    namem = f"**Song Name : **`{result.text.splitlines()[0]}`\
        \n\n**Details : **__{result.text.splitlines()[2]}__"
    await event.edit(namem)


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
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461083923)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("unblock @SongIDbot and try again")
            return
        if response.text.startswith("Perfect Match."):
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
        "shazam": ">`.szm <reply to voice/audio>" "\nUsage: Reverse search audio file using shazam api"}
)