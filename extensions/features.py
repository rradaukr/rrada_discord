from __future__ import annotations

from disnake.ext import commands
import disnake, random

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self._bot: commands.Bot = bot
        
    @commands.Cog.listener("on_ready")
    async def _rada_system_running(self) -> None:
        await self._bot.change_presence(activity=disnake.Activity(
            type=disnake.ActivityType.watching, name="на систему ради"))
        
    @commands.Cog.listener("on_member_join")
    async def _new_people_come(self, member: disnake.Member) -> None:
        try:
            brole_id = member.guild.get_role(1317506375445909524)
            rrole_id = member.guild.get_role(1317506588818276412)
            if brole_id is None or rrole_id is None: return None

            if not member.bot: await member.add_roles(brole_id)
            else: await member.add_roles(rrole_id)
        except Exception as e: return None
        
    @commands.Cog.listener("on_message")
    async def _random_feature_emojis(self, context: disnake.Message) -> None:
        chance: int = random.randint(0, 100)
        if chance > 82:
            emojis = context.guild.emojis
            if emojis:
                random_emoji = random.choice(emojis)
                await context.add_reaction(random_emoji)

        await self._bot.process_commands(context)

    @commands.slash_command(name="ping", description="Перевірка пінгу бота")
    async def _ping_command(self, interaction: disnake.CommandInteraction) -> None:
        await interaction.response.send_message(f"Пінг(Сігма) -> `{round(self._bot.latency * 1000)}мс`-1")

def setup(bot: commands.Bot) -> None: bot.add_cog(Ping(bot))
