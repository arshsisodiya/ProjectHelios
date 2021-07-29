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

@register(outgoing=True, pattern=r"^\.pdf(?: |$)(.*)")
async def _(event):
    if event.reply_to_msg_id:
     reply_message = await event.get_reply_message()
     chat = "@office2pdf_bot"
     await event.edit("Converting into PDF.....`")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                response = await conv.get_response()
                msg = await conv.send_message(reply_message)
                #response2 = await conv.get_response()
                convert = await conv.send_message("/ready2conv")
                cnfrm = await conv.get_response()
                editfilename = await conv.send_message("Yes")
                enterfilename = await conv.get_response()
                filename = await conv.send_message("Project Helios")
                started = await conv.get_response()
                pdf = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@pdfbot` and retry`")
                return
            await event.client.send_message(event.chat_id, pdf)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id, msg.id, started.id, filename.id, editfilename.id, enterfilename.id, cnfrm.id, pdf.id, convert.id]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit(
                "`Error: Sorry `@office2pdf_bot` is not responding please try again later` ")

CMD_HELP.update(
    {
        "PDF": ".pdf"
        "\nUsage: Convert Given English Text into PDF file "
    }
)

