import discord

# Replace <YOUR_TOKEN_HERE> with your bot token
TOKEN = 'MTA5NjA5ODMxODQ0ODMzMjk4Mw.GfWPDS.0j7ALevX3-LCQURWXYf9foOHjxpUYMGE09aO2w'

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

    elif message.content.startswith('!send_to_role'):
        role_name = message.content.split()[1]
        print(role_name)
        role = discord.utils.get(message.guild.roles, name=role_name)
        print(role)
        if role is not None:
            members = role.members
            member_names = [member.name for member in members]
            response = f'Members with the {role_name} role: {", ".join(member_names)}'
            await message.channel.send(response)

            offline_members = [member for member in role.members if member.status == discord.Status.offline]
            print(offline_members)
            responseOffline = f"Members with the '{role_name}' role who are offline: {', '.join([member.name for member in offline_members])}"
            await message.channel.send(responseOffline)

            # send message to all members with the specified role
            for member in members:
                try:
                    await member.send("Hello from the bot!")
                except discord.Forbidden:
                    # Handle the case where the bot doesn't have permission to DM the member
                    pass
        else:            
            await message.channel.send(f"Could not find role '{role_name}' in this server.")

client.run(TOKEN)