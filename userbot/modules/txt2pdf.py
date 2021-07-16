#Copyright @arshsisodiya
#https://github.com/arshsisodiya
#https://twitter.com/arshsisodiya

#Created by arshsisodiya for ProjectHelios

import asyncio
from asyncio.exceptions import TimeoutError
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, bot
from userbot.events import register

@register(outgoing=True, pattern=r"^\.pdf (?:(eng)|(.*) - (.*))")
async def _(event):
    "For English Language"
    if event.pattern_match.group(1) == "eng":
     if not event.reply_to_msg_id:
        return await event.edit("Reply to any text message.")
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        return await event.edit("Reply to text message")
    chat = "@pdfbot"
    await event.edit("Converting Your English Text into PDF.....`")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                response = await conv.get_response()
                text = await conv.send_message("/text")
                response2 = await conv.get_response()
                msg = await conv.send_message(reply_message)
                response3 = await conv.get_response()
                font = await conv.send_message("Roboto")
                cnfrm = await conv.get_response()
                pdf = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@pdfbot` and retry`")
                return
            await event.client.send_message(event.chat_id, pdf)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id, msg.id, text.id, response2.id, response3.id, cnfrm.id, pdf.id, font.id]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit(
                "`Error: Sorry `@pdfbot` is not responding please try again later` ")

@register(outgoing=True, pattern=r"^\.pdf (?:(hi)|(.*) - (.*))")
async def _(event):
    "For Hindi Langauge since Roboto Fonts Doesn't support Devnagari"
    if event.pattern_match.group(1) == "hi":
     if not event.reply_to_msg_id:
        return await event.edit("Reply to any text message.")
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        return await event.edit("Reply to text message")
    chat = "@pdfbot"
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                response = await conv.get_response()
                text = await conv.send_message("/text")
                response2 = await conv.get_response()
                msg = await conv.send_message(reply_message)
                response3 = await conv.get_response()
                font = await conv.send_message("Noto Sans")
                cnfrm = await conv.get_response()
                pdf = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@pdfbot` and retry`")
                return
            await event.client.send_message(event.chat_id, pdf)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id, msg.id,text.id,  response2.id, response3.id, cnfrm.id, pdf.id, font.id]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit(
                "`Error: Sorry `@pdfbot` is not responding please try again later` ")


CMD_HELP.update(
    {
        "Text2PDF": ".pdf eng"
        "\nUsage: Convert Given English Text into PDF file "
        "\n\n.pdf hi"
        "\nUsage:Convert Given Hindi Text into PDF file"

    }
)

