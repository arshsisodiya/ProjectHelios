import asyncio
from asyncio import sleep
from asyncio.exceptions import TimeoutError
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, bot
from userbot.events import register

@register(outgoing=True, pattern=r"^\.tempmail (?:(new|n)|(.*) - (.*))")

async def _(event):
 await event.edit("`Getting your Temp mail`")
 if event.pattern_match.group(1) == "new" "n":
    chat = "@TempMail_org_bot"
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                response = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@TempMail_org_bot` and retry`")
                return
            await event.client.send_message(event.chat_id, response)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id,]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Error: `@TempMail_org_bot` is not responding or you are trying to downloading instagram stories")


@register(outgoing=True, pattern=r"^\.tmr(?: |$)(.*)")
async def _(event):
    await event.edit("`Refeshing Your Inbox`")
    chat = "@TempMail_org_bot"
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("Refresh inbox")
                response = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@TempMail_org_bot` and retry`")
                return
            await event.client.send_message(event.chat_id, response)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id,]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Error: `@TempMail_org_bot` is not responding")

@register(outgoing=True, pattern=r"^\.tmn(?: |$)(.*)")
async def _(event):
    await event.edit("`Generating new Temp-Mail`")
    chat = "@TempMail_org_bot"
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("Generate new")
                response = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@TempMail_org_bot` and retry`")
                return
            await event.client.send_message(event.chat_id, response)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id,]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Error: `@TempMail_org_bot` is not responding")

@register(outgoing=True, pattern=r"^\.tms(?: |$)(.*)")
async def _(event):
    await event.edit("`Getting mails from your Temp-Mail Inbox.......`")
    chat = "@TempMail_org_bot"
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("Show email")
                response = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@TempMail_org_bot` and retry`")
                return
            await event.client.send_message(event.chat_id, response)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id,]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Error: `@TempMail_org_bot` is not responding")

@register(outgoing=True, pattern=r"^\.tmd(?: |$)(.*)")
async def _(event):
    await event.edit("`Deleting your old Temp-Mail and Creating new`")
    chat = "@TempMail_org_bot"
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("Delete")
                response = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Unblock `@TempMail_org_bot` and retry`")
                return
            await event.client.send_message(event.chat_id, response)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id,]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Error: `@TempMail_org_bot` is not responding")


CMD_HELP.update(
    {
        "Temp-Mail": ".tmail"
        "\nUsage: Create Temporary Email "

    }
)

