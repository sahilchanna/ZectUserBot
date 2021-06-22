from pyrogram import filters
from Zect import app, HELP, CMD_HELP
from config import PREFIX
from Zect.helpers.pyrohelper import get_arg

HELP.update(
    {
        "**🔸Admin Tools**": "__ban, unban, promote, demote, kick, mute, unmute, gmute, ungmute, pin, purge, del, invite__",
        "**🔸AFK**": "__afk, unafk__",
        "**🔸Alive**": "__alive, zect , zect ping__",
        "**🔸Developer**": "__eval, term__",
        "**🔸Misc**": "__paste, tr, whois, id__",
        "**🔸Notes**": "__save, get, clear, clearall, notes__",
        "**🔸Anti-PM**": "__pmguard, setpmmsg, setlimit, setblockmsg, allow, deny__",
        "**🔸Sticker**": "__kang, stkrinfo__",
        "**🔸Greetings**": "__setwelcome, clearwelcome__",
        "**🔸Updater**": "__update__",
    }
)


@app.on_message(filters.command("help", PREFIX) & filters.me)
async def help(client, message):
    args = get_arg(message)
    if not args:
        text = "**Available Commands**\n\n"
        for key, value in HELP.items():
            text += f"{key}: {value}\n\n"
        await message.edit(text)
        return
    else:
        module_name = args
        module_help = CMD_HELP.get(args, False)
        if not module_help:
            await message.edit("__Invalid module name specified.__")
            return
        else:
            await message.edit(module_help)
