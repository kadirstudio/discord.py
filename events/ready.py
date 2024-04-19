from discord.ext import commands
from datetime import datetime

class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] Bot {self.bot.user.name} olarak giriş yaptı!')
#kadirstudio tarafından kodlandı.

def setup(bot):
    bot.add_cog(Ready(bot))
