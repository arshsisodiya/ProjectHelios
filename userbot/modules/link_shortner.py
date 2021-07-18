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

@register(outgoing=True, pattern=r"^\.short(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    msg_link = await event.get_reply_message()
    query = event.pattern_match.group(1)

    if msg_link:
        query = msg_link.text
        await event.edit("`Shortning your link✂️✂️✂️`")
    chat = "@ShortUrlBot"
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                response = await conv.get_response()
                await event.edit("`Sending your link to cloud☁️ ☁️`")
                send_query = await conv.send_message(query)
                await event.edit("`Send your link to cloud successful☁️ ☁️`")
                garbagetext = await conv.get_response()
                await event.edit("`Fetching short url from cloud ☁️ ☁️`")
                shorturl = await conv.get_response()
                await event.edit("`Here is your short url👇👇👇👇`")
                garbagetext1 = await conv.get_response()
                garbagetext2 = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@ShortUrlBot` and retry`")
                return
            await event.client.send_message(event.chat_id, garbagetext )
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id, send_query.id, garbagetext.id, garbagetext1.id, garbagetext2.id]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit("`Error: `@ShortUrlBot` is not responding")
CMD_HELP.update(
    {
        "`link shortner`": ".short <url>"
                "\nUsage: Reply or paste a link to get "
                "short url using `@ShortUrlBot`"
    }
)

