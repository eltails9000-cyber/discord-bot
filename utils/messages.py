import asyncio


async def auto_delete(ctx, seconds=3):

    await asyncio.sleep(seconds)

    try:
        await ctx.delete_original_response()
    except:
        pass
