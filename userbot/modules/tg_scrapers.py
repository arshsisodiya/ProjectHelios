import os

import requests

from userbot.events import register
from userbot.utils import progress
from userbot.utils.helper import edit_or_reply, fetch_audio

@register(outgoing=True, pattern=r"^\.sazam (?:(now)|(.*) - (.*))")
async def shazamm(event):
    kek = await event.edit("`Shazaming In Progress!`")
    if not message.reply_to_message:
        await event.edit("Reply To The Audio.")
        return
    if os.path.exists("helios.mp3"):
        os.remove("helios.mp3")
    kkk = await fetch_audio(client, message)
    downloaded_file_name = kkk
    f = {"file": (downloaded_file_name, open(downloaded_file_name, "rb"))}
    await event.edit("**Searching For This Song In Friday's DataBase.**")
    r = requests.post("https://starkapis.herokuapp.com/shazam/", files=f)
    try:
        xo = r.json()
    except JSONDecodeError:
        await event.edit(
            "`Seems Like Our Server Has Some Issues, Please Try Again Later!`"
        )
        return
    if xo.get("success") is False:
        await event.edit("`Song Not Found IN Database. Please Try Again.`")
        os.remove(downloaded_file_name)
        return
    xoo = xo.get("response")
    zz = xoo[1]
    zzz = zz.get("track")
    zzz.get("sections")[3]
    nt = zzz.get("images")
    image = nt.get("coverarthq")
    by = zzz.get("subtitle")
    title = zzz.get("title")
    messageo = f"""<b>Song Shazamed.</b>
<b>Song Name : </b>{title}
<b>Song By : </b>{by}
<u><b>Identified Using Friday - Get Your Friday From</b></u>
"""
    await client.send_photo(message.chat.id, image, messageo, parse_mode="HTML")
    await kek.delete()
