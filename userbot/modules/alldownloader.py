import asyncio
from asyncio.exceptions import TimeoutError
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP
from userbot.events import register
from userbot.utils import progress

@register(outgoing=True, pattern=r"^\.rd(?: |$)(.*)")
async def _(event):
        "To recognize a image."
        if not event.reply_to_msg_id:
            return await event.edit("Reply to any user's media message.")
        reply_message = await event.get_reply_message()
        if not reply_message.media:
            return await event.edit(event, "reply to media file")
        chat = "@allsaverbot"
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
                await event.edit("unblock @allsaverbot and try again")
                return
            if response.text.startswith("Follow to @allsavernews channel, in order to keep up to date with all the bot news.."):
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
    {"reels": ">`.rd <text/reply>" "\nUsage: download reels"}
)