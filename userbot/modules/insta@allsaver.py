import asyncio
from asyncio.exceptions import TimeoutError
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.utils import progress

@register(outgoing=True, pattern=r"^\.ird2(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    msg_link = await event.get_reply_message()
    d_link = event.pattern_match.group(1)

    if msg_link:
        d_link = msg_link.text
        await event.edit("`Downloading...`")
    elif ".com" not in d_link:
        await event.edit("`Enter a valid link to download from`")

    elif "reel" in d_link:
        await event.edit("`Reel is downloading......`")
    elif "stories" in d_link:
        await event.edit("`Sorry but story downloading is not supported yet`")
    else:
        await event.edit("`fetching post from instagram...`")
    chat = "@allsaverbot"
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                response = await conv.get_response()
                msg = await conv.send_message(d_link)
                garbagetext = await conv.get_response()
                angarbasgetext = await conv.get_response()
                video = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@allsaverbot` and retry`")
                return
            await event.client.send_message(event.chat_id, video,)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id, msg.id,video.id, garbagetext.id, angarbasgetext.id]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit("`Error:")
CMD_HELP.update(
    {
        "ird": ".ird <link>"
        "\nUsage: Download files using (Instasaverbotbot)"

    }
)
