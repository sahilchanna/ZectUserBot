from config import PREFIX
import asyncio
import time
from datetime import datetime
from pyrogram import filters
from Zect import app, StartTime, CMD_HELP
from sys import version_info

from pyrogram import __version__ as __pyro_version__
from pyrogram.types import Message

CMD_HELP.update(
    {
        "Alive": """
『 **Alive** 』
  `alive` -> Show off to people with your bot using this command.
  `ping` -> Shows you the response speed of the bot.
"""
    }
)

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@app.on_message(filters.command("alive", PREFIX) & filters.me)
async def alive(_, m):
    start_time = time.time()
    uptime = get_readable_time((time.time() - StartTime))
    reply_msg =  f"__**ι αɱ αʅιʋҽ ʂιɾ**__\n"
    reply_msg += f"__**ԋσɯ ɾ υ ʂιɾ**__\n\n"
    reply_msg += f"**ᎧᏬᏒ ᏰᎧᏖ**\n"
    reply_msg += f"__Python__: `{__python_version__}`\n"
    reply_msg += f"__@Pyrogram version__: `{__pyro_version__}`\n"
    end_time = time.time()
    reply_msg += f"__Zect uptime__: {uptime}"
    photo = "https://telegra.ph/file/ed851ecd3803b3b411594.mp4"
    await m.delete()
    await app.send_photo(m.chat.id, photo, caption=reply_msg)


@app.on_message(filters.command("ping", PREFIX) & filters.me)
async def pingme(_, message: Message):
    start = datetime.now()
    await message.edit("`Pong!`")
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    await message.edit(f"**Pong!**\n\n`{m_s}ms`")


@app.on_message(filters.command("yokohama", PREFIX) & filters.me)
async def _(event):
    start = dt.now()
    x = await eor(event, "`Pong!`\n ⪻ⓦⒶⒾⓣ⪼ ")
    if event.fwd_from:
        return
    end = dt.now()
    ms = (end - start).microseconds / 1000
    uptime = grt((time.time() - start_time))
    await x.edit(f"**Pong** `{ms}ms`\n**➥Uptime** - `{uptime}`\n**➥✯☫уσкσнαмα вσт☫ ✯**")

@app.on_message(filters.command("cmds", PREFIX) & filters.me)
async def cmds(event):
    await allcmds(event)

