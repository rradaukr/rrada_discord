from __future__ import annotations

from config import Configuration

from disnake.ext import commands
import disnake

def _is_owner(interaction: disnake.CommandInteraction) -> bool: return interaction.author.id == int(Configuration.OWNER_ID)

class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self._bot: commands.Bot = bot

    @commands.slash_command(name="kick", description="Виключити користувача з сервера")
    async def _kick_command(self, interaction: disnake.CommandInteraction, user: disnake.User, reason: str = commands.Param(max_length=256)) -> None:
        if _is_owner(interaction):
            await interaction.guild.kick(user, reason=reason if reason is not None else "без причини")
            await interaction.response.send_message(f"{user.mention} був виключений з серверу через {interaction.author.mention}, по причині -> `{reason if reason is not None else 'без причини'}`")
        else:
            await interaction.response.send_message("У вас немає доступу до цієї команди!")

    @commands.slash_command(name="ban", description="Забанити користувача")
    async def _ban_command(self, interaction: disnake.CommandInteraction, user: disnake.User, reason: str = commands.Param(max_length=256)) -> None:
        if _is_owner(interaction):
            await interaction.guild.ban(user, reason=reason if reason is not None else "без причини")
            await interaction.response.send_message(f"{user.mention} був забанений на сервері через {interaction.author.mention}, по причині -> `{reason if reason is not None else 'без причини'}`")
        else:
            await interaction.response.send_message("У вас немає доступу до цієї команди!")

    @commands.slash_command(name="clear", description="Очистити кілька повідомлень з каналу")
    async def _clear_command(self, interaction: disnake.CommandInteraction, amount: commands.Range[int, 1, ...]) -> None:
        if _is_owner(interaction):
            messages = await interaction.channel.history(limit=amount).flatten()
            for message in messages: await message.delete()
            await interaction.response.send_message(f"{interaction.author.mention} очистив `{len(messages)}` повідомлень")
        else:
            await interaction.response.send_message("У вас немає доступу до цієї команди!")

def setup(bot: commands.Bot) -> None: bot.add_cog(Moderation(bot))
