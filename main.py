import discord
import os
from dotenv import load_dotenv

# Load the Discord bot token from the .env file
load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True # enable the members intent
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('!list_members'):
        members = []
        async for member in message.guild.fetch_members(limit=None):
            members.append(member)
        member_names = [member.name for member in members]
        await message.channel.send(f'Members in this server: {", ".join(member_names)}')

@client.event
async def on_message(message):
    if message.content.startswith('!list_members'):
        # Code to list all members in the server
        pass

    elif message.content.startswith('!send_to_role'):
        # Split the message into its parameters
        params = message.content.split()[1:]
        role_name = params[0]
        custom_message = ' '.join(params[1:])

        # Find the role and its members
        role = discord.utils.get(message.guild.roles, name=role_name)
        if role is not None:
            members = role.members

            # send message to all members with the specified role
            for member in members:
                try:
                    await member.send(custom_message)
                except discord.Forbidden:
                    # Handle the case where the bot doesn't have permission to DM the member
                    pass
        else:            
            await message.channel.send(f"Could not find role '{role_name}' in this server.")

client.run(TOKEN)