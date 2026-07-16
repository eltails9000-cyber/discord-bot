import discord

from discord.ext import commands

from database import ban,check,unban



class Roblox(commands.Cog):

    def __init__(self,bot):

        self.bot=bot



    @discord.slash_command(
        name="robloxban",
        description="Banea jugador de Glory or Death"
    )
    async def robloxban(
        self,
        ctx,
        userid:str,
        reason:str
    ):

        await ctx.defer()


        ban(
            userid,
            reason,
            str(ctx.author)
        )


        await ctx.respond(

            f"""
🚫 **Roblox Ban**

Usuario:
`{userid}`

Razón:
{reason}

Staff:
{ctx.author}
"""
        )



    @discord.slash_command(
        name="robloxcheck"
    )
    async def checkban(
        self,
        ctx,
        userid:str
    ):


        await ctx.defer()


        result=check(userid)


        if result:

            await ctx.respond(

            f"""
🚫 Está baneado

Razón:
{result['reason']}

Staff:
{result['staff']}
"""
            )

        else:

            await ctx.respond(
                "✅ No tiene ban"
            )




    @discord.slash_command(
        name="robloxunban"
    )
    async def unban(
        self,
        ctx,
        userid:str
    ):

        unban(userid)


        await ctx.respond(
            "✅ Ban eliminado"
        )



def setup(bot):

    bot.add_cog(
        Roblox(bot)
    )
