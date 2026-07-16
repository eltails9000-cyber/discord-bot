from config import OWNER_ID


async def owner_check(ctx):

    if ctx.author.id != OWNER_ID:

        await ctx.respond(
            "❌ No tienes permisos para usar este bot.",
            ephemeral=True
        )

        return False

    return True
