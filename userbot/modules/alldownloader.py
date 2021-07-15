import asyncio
from asyncio.exceptions import TimeoutError
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.utils import progress

@register(outgoing=True, pattern=r"^\.rd(?: |$)(.*)")
async def _(event):
        "To recognize a image."
        if not event.reply_to_msg_id:
            return await event.edit("Reply to any user's media message.")
        reply_message = await event.get_reply_message()
        if not reply_message:
            return await event.edit("reply to a link")
        chat = "@allsaverbot"
        if reply_message.sender.bot:
            return await event.edit("Reply to actual users message.")
        await event.edit("downloading this media")
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                response = await conv.get_response()
                msg = await conv.send_message(d_link)
                details = await conv.get_response()
                song = await conv.get_response()
                """"- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("unblock @allsaverbot and try again")
                return
            await bot.send_file(event.chat_id, song, caption=details.text)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id, msg.id, details.id, song.id]
            )
            await event.delete()



CMD_HELP.update(
    {"reels": ">`.rd <text/reply>" "\nUsage: download reels"}
)