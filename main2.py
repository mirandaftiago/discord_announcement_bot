

# This example requires the 'message_content' intent.

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.content.startswith('!send_to_role'):
            role_name = message.content.split()[1]
            role = discord.utils.get(message.guild.roles, name=role_name)
            print()
            if role is not None:
                for member in role.members:
                    print(member)               
                    await member.send('Hello from the bot!')
            else:
                await message.channel.send(f"Could not find role '{role_name}' in this server.")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTA5NjA5ODMxODQ0ODMzMjk4Mw.GfWPDS.0j7ALevX3-LCQURWXYf9foOHjxpUYMGE09aO2w')