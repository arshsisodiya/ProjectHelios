import asyncio
from asyncio.exceptions import TimeoutError
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern=r"^\.stt(?: |$)(.*)")
async def _(event):
    "To recognize a image."
    if not event.reply_to_msg_id:
        return await event.edit("Reply to any user's media message.")
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        return await event.edit(event, "reply to media file")
    chat = "@voicybot"
    if reply_message.sender.bot:
        return await event.edit(event, "Reply to actual users message.")
    await event.edit("recognizeing this media")
    async with event.client.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            await event.client.forward_messages(chat, reply_message)
            response = await conv.get_response()
            """- don't spam notif -"""
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("`Unblock `@voicybot` and retry`")
            return
        await bot.send_file(event.chat_id, response)
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, response.id, msg.id, ]
        )
        await event.delete()


CMD_HELP.update(
    {
        "stt": ".speech to text "
                 "\nUsage: Reply to a audio file to convert it into text "
                 "using `@voicybot`"
    }
)

