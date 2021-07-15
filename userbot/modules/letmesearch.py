from asyncio import sleep
import requests
from userbot.events import register
from userbot import CMD_HELP

@register(outgoing=True, pattern=r"^\.gg(?: |$)(.*)")
async def _(event):
    """Searches the given query in Google and shows you the link of that query."""
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=http://google.com/search?q={}".format(
        input_str.replace(" ", "+")
    )
    response_api = requests.get(sample_url).text
    event = await event.edit("`Searching.....`")
    await sleep(2)
    if response_api:
        await event.edit(
            "Let me **Google** that for you:\n👉 [{}]({})\n`Thank me later 😉` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await event.edit("`Something went wrong. Please try again later.`", 5)

        CMD_HELP.update(
            {
                "search": ".gg <query> >"
                            "\nUsage:Searches the given query in Google and shows you the link of that query)"
            }
        )
