from __future__ import annotations

from config import Configuration

from disnake.ext import commands
import disnake, os

instance_intents = disnake.Intents.all()
bot_instance: commands.Bot = commands.Bot(command_prefix=",", intents=instance_intents, owner_id=Configuration.OWNER_ID)

if os.path.exists("extensions/"):
    for file in os.listdir("extensions/"): 
        if os.path.isdir(f"extensions/{file}"): continue
        bot_instance.load_extension(f"extensions.{file[:-3]}")

if __name__ == "__main__": bot_instance.run(Configuration.TOKEN)
