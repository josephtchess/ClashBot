import discord
import responses
import os
mytok = 'nice try'
async def send_message(username, message, user_message):
    try:
        response = responses.handle_response(username, user_message)
        if response[0] == 0:
            await message.channel.send(response[1])
        elif response[0] == 1:
            await message.channel.send(file=discord.File(response[1]))
            os.remove(response[1])
            await message.channel.send(response[2])
        elif response[0] == 2:
            png_dict = response[1]
            await message.channel.send(username)
            for key in png_dict:
                await message.channel.send(png_dict[key][0] + png_dict[key][2])
                await message.channel.send(file=discord.File(png_dict[key][1]))
                os.remove(png_dict[key][1])
        elif response[0] == 3:
            names = response[1]
            for key in names:
                await message.channel.send(names[key])

    except Exception as e:
        print(e)

def run_bot():
    TOKEN = mytok
    intents = discord.Intents.default()
    intents.message_content = True
    intents.messages = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")
        if user_message[0] == '!':
            await send_message(username, message, user_message[1:])
    client.run(TOKEN)