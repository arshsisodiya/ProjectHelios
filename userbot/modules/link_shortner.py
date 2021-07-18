# Copyright (C) 2021 arshsisodiya
# https://github.com/arshsisodiya
# https://twitter.com/arshsisodiya

# Created by arshsisodiya for ProjectHelios

import asyncio
from asyncio import sleep
from asyncio.exceptions import TimeoutError
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.short(?: |$)(.*)")
async def _(event):
    await event.edit("`Shortning your link ✂️✂️✂️`")
    if event.fwd_from:
        return
    msg_link = await event.get_reply_message()
    d_link = event.pattern_match.group(1)

    if msg_link:
        d_link = msg_link.text
        await event.edit("`Shortning your replied link ✂️✂️✂️`")
    elif "https" not in d_link:
        await event.edit("`Enter a valid link to short, make sure it start  with` `http://` or `https://`")
    else:
        await event.edit("`Shortning your replied link ✂️✂️✂️`")
    chat = "@ShortUrlBot"
    try:
        async with event.client.conversation(chat) as conv:
            try:
                await event.edit("`Sending your link to server☁️☁️☁️`")
                msg_start = await conv.send_message("/start")
                bot_reply = await conv.get_response()
                msg = await conv.send_message(d_link)
                await event.edit("`Fetching short url from server☁️☁️☁️`")
                response = await conv.get_response()
                await event.edit("`here is your short url👇👇👇👇`")
                url = await conv.get_response()
                sponser = await conv.get_response()

                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
                await event.edit(response.text)
            except YouBlockedUserError:
                await event.edit("`Unblock `@ShortUrlBot` and retry`")
                return
            await event.client.send_message(event.chat_id,  url)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id, msg.id, bot_reply.id, sponser.id]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit("`Error: `@ShortUrlBot` is not responding please try again later")

CMD_HELP.update(
    {
        "`shortlink`": ".short <url>"
                "\nUsage: Reply or paste a link to get"
                "\nshort url using `@ShortUrlBot`"
    }
)