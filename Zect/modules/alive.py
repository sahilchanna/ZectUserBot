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
  `zect` -> Show off to people with your bot using this command.
  `ping` -> Shows you the response speed of the bot.
  `zect` -> Show off to people with your bot using this command.
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


@app.on_message(filters.command("zect", PREFIX) & filters.me)
async def alive(_, m):
    start_time = time.time()
    uptime = get_readable_time((time.time() - StartTime))
    reply_msg = f"**╭────────────────**\n"
    reply_msg += f"__**zect**__`{https://github.com/sahilchanna/ZectUserBot}`\n"
    reply_msg += f"__Python__ ➟`{__python_version__}`\n"
    reply_msg += f"__zect version__➟`{__pyro_version__}`\n"
    end_time = time.time()
    reply_msg += f"__zect uptime__➟ {uptime}\n"
    reply_msg += f"**╰────────────────**\n" 
    video = "https://telegra.ph/file/94420a12eec35e6dda0e3.mp4" 
    await m.delete()
    await app.send_video(m.chat.id, video , caption=reply_msg)
    

@app.on_message(filters.command("alive", PREFIX) & filters.me)
async def alive(_, m):
    start_time = time.time()
    uptime = get_readable_time((time.time() - StartTime))
    reply_msg = f"**╭────────────────**\n"
    reply_msg += f"__**The Bot**__\n"
    reply_msg += f"__Python__ ➟`{__python_version__}`\n"
    reply_msg += f"__pyro version__➟`{__pyro_version__}`\n"
    end_time = time.time()
    reply_msg += f"__uptime__➟ {uptime}\n"
    reply_msg += f"**╰────────────────**\n" 
    photo = "https://telegra.ph/file/3f443150c22b6bc213cd6.jpg" 
    await m.delete()
    await app.send_video(m.chat.id, photo , caption=reply_msg)
    




