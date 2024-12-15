from __future__ import annotations

from resource_content import request_resource_text

from disnake.ext import commands
import disnake

class Help(commands.Cog):
    def __init__(self, bot: commands.bot) -> None:
        self._bot: commands.Bot = bot

    @commands.slash_command(name="help", description="Отримай допомогу по командах бота")
    async def _help_command(self, interaction: disnake.CommandInteraction) -> None:
        help_content: str = request_resource_text("help_command")
        await interaction.response.send_message(help_content if help_content is not None else \
            "Помилка: Серверна помилка, відсутній підготовлений текст сценарію, перевірте ресурси сервера на наявність цього сценарію")

def setup(bot: commands.Bot) -> None: bot.add_cog(Help(bot))
