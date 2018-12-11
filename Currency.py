# Work with Python 3.6
import discord

TOKEN = 'NTAyMjg5ODk3NTg4MjYwODY2.DqmKeg.BHGfzWyZIc9VdVjBPvtQnWVLe5k'

client = discord.Client()

class user:

    def __init__(self, name):
        self.name = name
        self.balance = 30



@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!Hello Bot'):
        msg1 = 'hello'.format(message)
        await client.send_message(message.channel, msg1)
    if message.content.startswith('!balance'):
        lol = message.author.id
        await client.send_message(message.channel, lol)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    userArray = {}
    print('------')
    for server in client.servers:
        for member in server.members:
            u1 = user(member)
            userArray[str(member)] = u1

    print (userArray["pix3lbandit#3398"].balance)
client.run(TOKEN)