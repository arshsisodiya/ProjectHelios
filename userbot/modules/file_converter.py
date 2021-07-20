"""File Converter
.nfc """
import asyncio
import os
import time
from datetime import datetime
from telethon.tl.types import InputMediaUploadedDocument
from telethon.tl.types import DocumentAttributeAudio
from telethon.utils import get_attributes
from userbot.events import register
from userbot.utils import media_type
from userbot import CMD_HELP, bot, TEMP_DOWNLOAD_DIRECTORY


@register(outgoing=True, pattern=r"^\.nfc(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    if reply_message is None:
        await event.edit("reply to a media to use the `nfc` operation.\nInspired by @FileConverterBot")
        return
    await event.edit("trying to download media file, to my local")
    try:
        start = datetime.now()
        c_time = time.time()
        downloaded_file_name = await bot.download_media(
            reply_message,
            TEMP_DOWNLOAD_DIRECTORY,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                bot.progress(d, t, event, c_time, "trying to download")
            )
        )
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))
    else:
        end = datetime.now()
        ms = (end - start).seconds
        await event.edit("Downloaded to `{}` in {} seconds.".format(downloaded_file_name, ms))
        new_required_file_name = ""
        new_required_file_caption = ""
        command_to_run = []
        voice_note = False
        supports_streaming = False
        if input_str == "voice":
            new_required_file_caption = "NLFC_" + str(round(time.time())) + ".opus"
            new_required_file_name = TEMP_DOWNLOAD_DIRECTORY + "/" + new_required_file_caption
            command_to_run = [
                "ffmpeg",
                "-i",
                downloaded_file_name,
                "-map",
                "0:a",
                "-codec:a",
                "libopus",
                "-b:a",
                "100k",
                "-vbr",
                "on",
                new_required_file_name
            ]
            voice_note = True
            supports_streaming = True
        elif input_str == "mp3":
            new_required_file_caption = "NLFC_" + str(round(time.time())) + ".mp3"
            new_required_file_name = TEMP_DOWNLOAD_DIRECTORY + "/" + new_required_file_caption
            command_to_run = [
                "ffmpeg",
                "-i",
                downloaded_file_name,
                "-vn",
                new_required_file_name
            ]
            voice_note = False
            supports_streaming = True
        else:
            await event.edit("not supported")
            os.remove(downloaded_file_name)
            return
        logger.info(command_to_run)
        t_response, e_response = await bot.run_command(command_to_run)
        os.remove(downloaded_file_name)
        if os.path.exists(new_required_file_name):
            end_two = datetime.now()
            force_document = False
            file_handle = await event.client.upload_file(
                new_required_file_name,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    bot.progress(d, t, event, c_time, "trying to upload")
                )
            )
            attributes, mime_type = get_attributes(
                new_required_file_name,
                mime_type=None,
                attributes=[],
                force_document=force_document,
                voice_note=voice_note,
                video_note=False,
                supports_streaming=supports_streaming,
                thumb=None
            )
            os.remove(new_required_file_name)
            attributes = [DocumentAttributeAudio(
                duration=attributes[-1].duration,
                voice=voice_note,
                title=Config.NFC_TITLE,
                performer=Config.NFC_PERFORMER,
                waveform=attributes[-1].waveform
            )]
            media = InputMediaUploadedDocument(
                file=file_handle,
                mime_type=mime_type,
                attributes=attributes,
                thumb=None,
                force_file=force_document
            )
            await event.reply(
                file=media
            )
            ms_two = (end_two - end).seconds
            await event.edit(f"converted in {ms_two} seconds")

