import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '>>')
client.remove_command('help')

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages deleted')


@client.command(pass_context = True)
async def kick(ctx, member: discord.User):
    await client.kick(member)
    await client.delete_message(ctx.message)

@client.command(pass_context = True)
async def ban(ctx, member: discord.User):
    await client.ban(member)
    await client.delete_message(ctx.message)
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
