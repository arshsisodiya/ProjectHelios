 
import asyncio
import logging
import math
import os
import time
from math import ceil
from traceback import format_exc
from userbot.events import register
from userbot.utils import progress

from pyrogram import Client
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import (
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)

async def fetch_audio(client, message):
    """Fetch Audio From Videos Or Audio Itself"""
    c_time = time.time()
    if not message.reply_to_message:
        await message.edit("`Reply To A Video / Audio.`")
        return
    warner_stark = message.reply_to_message
    if warner_stark.audio is None and warner_stark.video is None:
        await message.edit("`Format Not Supported`")
        return
    if warner_stark.video:
        await message.edit("`Video Detected, Converting To Audio !`")
        warner_bros = await message.reply_to_message.download(
            progress=progress, progress_args=(message, c_time, f"`Downloading Audio!`")
        )
        stark_cmd = f"ffmpeg -i {warner_bros} -map 0:a friday.mp3"
        await runcmd(stark_cmd)
        final_warner = "friday.mp3"
    elif warner_stark.audio:
        await message.edit("`Download Started !`")
        final_warner = await message.reply_to_message.download(
            progress=progress, progress_args=(message, c_time, f"`Downloading Video!`")
        )
    await message.edit("`Almost Done!`")
    return final_warner

