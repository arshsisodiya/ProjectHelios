
import os
import subprocess
from asyncio import create_subprocess_shell as asyncSubprocess
from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from userbot.events import register

@register(outgoing=True, pattern=r"^.getch(?: |$)([\s\S]*)")
async def get_media(event):
    catty = event.pattern_match.group(1)
    limit = int(catty.split(" ")[0])
    channel_username = str(catty.split(" ")[1])
    tempdir = os.path.join(TEMP_DOWNLOAD_DIRECTORY, channel_username)
    try:
        os.makedirs(tempdir)
    except BaseException:
        pass
    event = await event.edit("`Downloading Media From this Channel.`")
    msgs = await event.client.get_messages(channel_username, limit=int(limit))
    i = 0
    for msg in msgs:
        mediatype = media_type(msg)
        if mediatype is not None:
            await event.client.download_media(msg, tempdir)
            i += 1
            await event.edit(
                f"Downloading Media From this Channel.\n **DOWNLOADED : **`{i}`"
            )
    ps = subprocess.Popen(("ls", tempdir), stdout=subprocess.PIPE)
    output = subprocess.check_output(("wc", "-l"), stdin=ps.stdout)
    ps.wait()
    output = str(output)
    output = output.replace("b'", " ")
    output = output.replace("\\n'", " ")
    await event.edit(
        f"Successfully downloaded {output} number of media files from {channel_username} to tempdir"
    )


@register(outgoing=True, pattern=r"^.geta(?: |$)([\s\S]*)")
async def get_media(event):
    channel_username = event.pattern_match.group(1)
    tempdir = os.path.join(TEMP_DOWNLOAD_DIRECTORY, channel_username)
    try:
        os.makedirs(tempdir)
    except BaseException:
        pass
    event = await event.edit("`Downloading All Media From this Channel.`")
    msgs = await event.client.get_messages(channel_username, limit=3000)
    i = 0
    for msg in msgs:
        mediatype = media_type(msg)
        if mediatype is not None:
            await event.client.download_media(msg, tempdir)
            i += 1
            await event.edit(
                f"Downloading Media From this Channel.\n **DOWNLOADED : **`{i}`"
            )
    ps = subprocess.Popen(("ls", tempdir), stdout=subprocess.PIPE)
    output = subprocess.check_output(("wc", "-l"), stdin=ps.stdout)
    ps.wait()
    output = str(output)
    output = output.replace("b'", "")
    output = output.replace("\\n'", "")
    await event.edit(
        f"Successfully downloaded {output} number of media files from {channel_username} to tempdir"
    )

