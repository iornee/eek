import discord
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
import random


client = commands.Bot(command_prefix='/')
status = cycle(['Being Rewritten', 'Code being added by iorn_miner#3984', 'iorn_miner\'s homepage','alecdev.cf','To invite the bot use this link http://iornbot.tk/'])


@client.event
async def on_ready():
    print('Bot is ready.')
    change_status.start()


@client.command()
async def latest_updates(ctx):
    embed = discord.Embed(
        title='Lastest Updates',
        description='added poll',
        colour=discord.Colour.blue()
    )

    embed.set_footer(text='')
    embed.set_image(url='')
    await ctx.send(embed=embed)

@client.command()
async def poll(ctx,*, pollarg) :

    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
        colour=discord.Colour.blue(),
        title=f"Poll: {pollarg}",

    )

    embed.set_author(name=f"{client.user.name}", icon_url=f"") #
    embed.set_footer(text=f"Code given by tic :D | Check out alecdev.cf | {client.user.name}")
    message = await ctx.send(embed=embed)
    await message.add_reaction('👍')
    await message.add_reaction('👎')


@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=(next(status))))


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.send("You have been kicked by {}#{} for {}".format(ctx.author.name, ctx.author.discriminator, reason))
    await member.kick(reason=reason)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.send("You have been banned by {}#{} for {}".format(ctx.author.name, ctx.author.discriminator, reason))
    await member.ban(reason=reason)


@client.command()
@commands.has_permissions(ban_members=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild=ctx.guild
    for role in guild.roles:
        if role.name == 'Muted':
            await member.add_roles(role)
    await member.send("You have been muted by {}#{} for {}".format(ctx.author.name, ctx.author.discriminator, reason))
    await ctx.send(f'User {member} has been muted')


@client.command()
async def invite(ctx):
    await ctx.send('Here is your very epic invite https://smolurl.tk/koala')


@client.command()
async def memes(ctx):
    memes = ["https://cdn.discordapp.com/attachments/751024007028932668/751024040495546448/reddit_meme_4.jpg", "https://cdn.discordapp.com/attachments/751024007028932668/751024040784691230/reddit_meme_5.jpg", "https://cdn.discordapp.com/attachments/751024007028932668/751024042118742046/reddit_meme_6.jpg", "https://cdn.discordapp.com/attachments/751024007028932668/751024043410587718/reddit_meme_7.jpg", "https://cdn.discordapp.com/attachments/751024007028932668/751024045461340190/reddit_meme_8.jpg", "https://cdn.discordapp.com/attachments/751024007028932668/751024048422781008/reddit_meme_9.png", "https://cdn.discordapp.com/attachments/751024007028932668/751024049739792475/reddit_meme_10.jpg", "https://media.discordapp.net/attachments/751024007028932668/751024051455000667/reddit_meme_2.jpg?width=498&height=755", "https://cdn.discordapp.com/attachments/751024007028932668/751024052079951872/reddit_meme_3.jpg", "https://cdn.discordapp.com/attachments/751024007028932668/751024901011406909/reddit_meme_1.jpg", "https://cdn.discordapp.com/attachments/751032251508326402/751032940980469870/custom_meme_1.jpg","https://cdn.discordapp.com/attachments/751032251508326402/751032316654125166/meme_6.jpg", "https://cdn.discordapp.com/attachments/751032251508326402/751032349139009586/meme_1.jpg", "https://cdn.discordapp.com/attachments/751032251508326402/751032351039029248/meme_2.jpg","https://cdn.discordapp.com/attachments/751032251508326402/751032351630557254/meme_3.jpglol"]

    await ctx.send(random.choice(memes))




@client.command()
async def cat_pic(ctx):
    embed = discord.Embed(
        title='Cat Pic :D',
        description='CAT PIC YAY',
        colour=discord.Colour.blue()
    )

    embed.set_footer(text='')
    embed.set_image(url='https://cdn.discordapp.com/attachments/745217987262414949/751003748788207636/cat_1.jpg')
    await ctx.send(embed=embed)

@client.command()
async def cat_pic2(ctx):
    embed = discord.Embed(
        title='Cat Pic :D',
        description='CAT PIC YAY',
        colour=discord.Colour.blue()
    )

    embed.set_footer(text='')
    embed.set_image(url='https://cdn.discordapp.com/attachments/751004489754083358/751004538353483794/cat_2.jpg')
    await ctx.send(embed=embed)








client.run('NzQ2Mjc1NTU2MDM0NjA5MTUy.Xz99RQ.BDR2LFKTc7dDg27OlKkRR-tr65I')
