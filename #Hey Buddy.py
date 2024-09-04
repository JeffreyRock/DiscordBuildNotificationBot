#Hey Buddy. your a chad who buys fun this like video games and stuff.

#the Actual comment. this is a bot that sends a notification to my discord server to tell me shit is, in the words of twomod is breaky
import discord
import threading
import io
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load environment variables securely (consider using a library like `python-dotenv`)
discord_token = os.getenv("DISCORD_TOKEN")
discord_channel_id = 944715418390626386
# Intents for improved functionality (consider adding more as needed)
intents = discord.Intents.default()
intents.messages = True
intents.members = True  # For checking channel types (optional)

client = discord.Client(intents=intents)

@app.route('/test', methods=['POST'])
async def test():
    """Tests the bot's functionality and logs channel information."""
    print(f"Channel ID: {discord_channel_id}")

    channels = client.get_all_channels()
    for channel in channels:
        if channel is not None:
            print(f"Channel Type: {channel.type}")
            print(f"Channel Name: {channel.name}")
            print(f"Channel ID: {channel.id}")
        else:
            print("Channel not found.")

    return jsonify({"Status": "Check logs"}), 200

@app.route('/succeed', methods=['POST'])
async def succeed():
    """Sends a success message to the Discord channel with an optional attachment."""
    attachments = request.files.get('attachment')
    channel = client.get_channel(discord_channel_id)

    if not channel:
        for channelOption in client.get_all_channels():
            if(channelOption.id == 944715418390626386):
                channel = channelOption
                print("channel found")
                break
        return jsonify({'status': "Invalid channel ID"}), 400
        
    if attachments:
        attachments_file = discord.File(io.BytesIO(attachments.read()), filename=attachments.filename)
        await channel.send(content="Build Succeeded", file=attachments_file)
    else:
        await channel.send(content="Build Succeeded")

    return jsonify({'status': "Success"}), 200

@app.route('/fail', methods=['POST'])
async def fail():
    """Sends a failure message to the Discord channel with an optional attachment."""
    attachments = request.files.get('attachment')
    channel = client.get_channel(discord_channel_id)

    if not channel:
        return jsonify({'status': "Invalid channel ID"}), 400

    if attachments:
        attachments_file = discord.File(io.BytesIO(attachments.read()), filename=attachments.filename)
        await channel.send(content="Build Failed", file=attachments_file)
    else:
        await channel.send(content="Build Failed")

    return jsonify({'status': "Success"}), 200

@client.event
async def on_ready():
    """Logs bot startup messages and starts the Flask server."""
    print(f'Logged in as {client.user.name}')
    print("Bot Started")
    print("Starting Flask")

    Flask_thread = threading.Thread(target=run_flask)
    Flask_thread.start()

def run_flask():
    """Runs the Flask server in a separate thread."""
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    try:
        client.run(discord_token)
    except Exception as e:
        print(f'An error occurred: {e}')