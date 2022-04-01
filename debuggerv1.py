@client.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print('[ERROR]: You\'re missing permission to execute this command')
        await ctx.send('[ERROR]: You\'re missing permission to execute this command', delete_after=30)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"[ERROR]: Missing arguments: {error}")
        await ctx.send(f"[ERROR]: Missing arguments: {error}", delete_after=30)
    elif isinstance(error, numpy.AxisError):
        print('Invalid Image')
        await ctx.send('Invalid Image', delete_after=3)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"[ERROR]: 404 Forbidden Access: {error}")
        await ctx.send(f"[ERROR]: 404 Forbidden Access: {error}", delete_after=30)
    elif "Cannot send an empty message" in error_str:
        print('[ERROR]: Message contents cannot be null')
        await ctx.send('[ERROR]: Message contents cannot be null', delete_after=30)
    else:
        print(f'[ERROR]: {error_str}')
        await ctx.send(f'[ERROR]: {error_str}', delete_after=30)
