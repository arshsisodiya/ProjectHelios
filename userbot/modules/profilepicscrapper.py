import asyncio
from telethon import events
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern=r"^\.p(oto|pic)(?: |$)(.*)")
async def _(event):
    "To get user or group profile pic"
    uid = "".join(event.raw_text.split(maxsplit=1)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    if user:
        photos = await event.client.get_profile_photos(user.sender)
        u = True
    else:
        photos = await event.client.get_profile_photos(chat)
        u = False
    if uid.strip() == "":
        uid = 1
        if int(uid) > (len(photos)):
            return await event.edit("`No photo found of this NIBBA / NIBBI. Now u Die!`"
            )
        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    elif uid.strip() == "all":
        if len(photos) > 0:
            await event.client.send_file(event.chat_id, photos)
        else:
            try:
                if u:
                    photo = await event.client.download_profile_photo(user.sender)
                else:
                    photo = await event.client.download_profile_photo(event.input_chat)
                await event.client.send_file(event.chat_id, photo)
            except Exception:
                return await event.edit("`This user has no photos to show you`")
    else:
        try:
            uid = int(uid)
            if uid <= 0:
                await event.edit(
                    event, "```number Invalid!``` **Are you Comedy Me ?**"
                )
                return
        except BaseException:
            await event.edit("`Are you comedy me ?`")
            return
        if int(uid) > (len(photos)):
            return await edit_delere(
                event, "`No photo found of this NIBBA / NIBBI. Now u Die!`"
            )

        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    await event.delete()

CMD_HELP.update(
    {"poto": ">`.poto` \ `.`ppic <text/reply>" "\nUsage: Reply to a user to get his profile pic or use command along\
        with profile pic number to get desired pic else use .poto all to get\
        all pics. If you don't reply to any one\
        then the bot will get the chat profile pic"}
)