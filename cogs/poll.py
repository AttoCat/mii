from discord.ext import commands
import discord


class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, title, *choices):
        """!poll <title> <任意の数の要素(20以下、指定しなければ さんせいorはんたい)> で投票を行います。"""
        if len(choices) > 20:
            await ctx.send("要素の最大数は20です！")
            return
        if len(title) > 256:
            await ctx.send("タイトルの文字数が多すぎます！")
            return
        emoji = 0x0001f1e6
        num = 0
        content = ""
        emojis = []
        if len(choices) == 0:
            emojis += [
                "<:__sansei:703788213919023104>",
                "<:__hantai:703788248362647594>"]
        else:
            for num, choice in enumerate(choices):
                reaction = chr(emoji + num)
                content += f"{reaction}：{choice}\n"
                num += 1
                emojis.append(reaction)
        embed = discord.Embed(
            title=title,
            description=content,
            color=0x3aee67
        )
        msg = await ctx.send(embed=embed)
        [await msg.add_reaction(e) for e in emojis]


def setup(bot):
    bot.add_cog(Poll(bot))
