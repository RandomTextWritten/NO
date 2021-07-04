import discord
from discord import message
from discord.embeds import Embed
from discord.message import Message
from discord.ext import commands


intents = discord.Intents().all()
client = discord.Client()
bot = commands.Bot("*", intents=intents)
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

warns = []

@bot.event
async def on_ready():
	print("Bot is ready sir!{0.user}".format(bot))
	for i in bot.guilds[0].members:
		warns.append([i.id, 0])

@bot.command(pass_context=True)
@commands.has_role("Trial Moderator")
async def say(ctx, *args):
	await ctx.channel.purge(limit=1)
	tosay = ""
	for i in args:
		tosay += i + " "
	await ctx.channel.send(tosay)

@bot.command(pass_context=True)
@commands.has_role("Trial Moderator")
async def warn(ctx, user: discord.Member):
	id = user.id
	for i in warns:
		if int(i[0]) == int(id):
			i[1] = i[1] + 1
	await ctx.channel.send("User has been warned")

@bot.command(pass_context=True)
@commands.has_role("Trial Moderator")
async def warnings(ctx, user: discord.Member):
	id = user.id
	for i in warns:
		if int(i[0]) == int(id):
			await ctx.channel.send(i[1])

@bot.command(pass_context=True)
async def member_count(ctx):
	guild = ctx.guild
	await ctx.channel.send(len(guild.members))

@bot.command(pass_context=True)
@commands.has_role("Trial Moderator")
async def delete(ctx, limit:int=1):
	await ctx.channel.purge(limit=(limit+1))

@bot.command(pass_context=True)
@commands.has_role("Trial Moderator")
async def hof_submit(ctx, msgid, *args):
	await ctx.channel.purge(limit=1)
	msg = await ctx.fetch_message(msgid)
	channel = await bot.fetch_channel(858889422220165130)
	bname = ""
	for i in args:
		bname += i + " "
	result = f"{bname}, built by {msg.author.mention} {msg.attachments[0].url}"
	await channel.send(result)

@bot.command(pass_context=True)
@commands.has_role("Trial Moderator")
async def hob_submit(ctx, msgid, *args):
	await ctx.channel.purge(limit=1)
	msg = await ctx.fetch_message(msgid)
	channel = await bot.fetch_channel(858890421634990100)
	bname = ""
	for i in args:
		bname += i + " "
	result = f"{bname}, built by {msg.author.mention} {msg.attachments[0].url}"
	await channel.send(result)

@bot.command(pass_context=True)
@commands.has_role("Trial Moderator")
async def kick(ctx, person : discord.Member):
	ctx.guild.kick(person)
	await ctx.channel.send(f"Member {person} has been kicked")

@bot.command(pass_context=True)
@commands.has_role("Trial Moderator")
async def ban(ctx, user : discord.Member = None):
	banembed = discord.Embed(title="-ban")
	banembed.add_field(name="-ban {@user}", value="Bans a user")
	if not user:
		await ctx.channel.send(embed=banembed)
	else:
		guild = ctx.guild
		await guild.ban(user=user)
		await ctx.channel.send(f"Member {user.mention} has been banned")

@bot.command(pass_context=True)
@commands.has_role("Trial Moderator")
async def mute(ctx, member:discord.Member, *, reason = None):
	await ctx.channel.purge(limit=1)
	print(member)
	if not member:
		await ctx.channel.send(embed=Embed(title="Mute").add_field("*mute {user}", "Mutes the user"))
	else:
		role = discord.utils.get(ctx.guild.roles, name="muted")
		if role == None:
			role = await ctx.guild.create_role(name="muted")
			perms = discord.Permissions()
			perms.update(read_messages = True, read_message_history = True, connect = True, speak = False, send_messages = False)
		#perms = discord.Permissions()
		#perms.update(read_messages = True, read_message_history = True, connect = True, speak = False, send_messages = False)
		await member.add_roles(role)
		await member.add_roles(role)
		await ctx.channel.send(f"{member.mention} has been muted")

@bot.command(pass_context=True)
@commands.has_role("Trial Moderator")
async def unmute(ctx, user: discord.Member = None):
	if not user:
		await ctx.channel.send(embed=Embed(title="Mute").add_field("*mute {user}", "Mutes the user"))
	else:
		role = discord.utils.get(ctx.message.server.roles, name='member')
		await bot.remove_roles(user, role)
		await bot.say("{} has been umuted".format(user.name))


bot.run("ODYwNzQ5NTMyODQ0MzkyNDk4.YN_xeA.4xZmVR7PGVNndfP0Pajzbk8eWz4")