#Hey Buddy. your a chad who buys fun this like video games and stuff.

#the Actual comment. this is a bot that sends a notification to my discord server to tell me shit is, in the words of twomod is breaky
import discord
import threading
import io
import os
from flask import Flask, request,jsonify

app = Flask(__name__)
TokenEnv = os.getenv("DISCORD_TOKEN")
ChannelEnv = os.getenv("DISCORD_CHANNEL_ID")
intents =discord.Intents.default()
intents.messages=True
client = discord.Client(intents=intents)
Token= TokenEnv #Do not commit this line 
CHANNEL_ID= 

@app.route('/succeed', methods=['POST'])
async def succeed():
    attachments = request.files['attachment']
    if  not attachments:
        return jsonify({'status':" Errors "}),400
    attachments_file = discord.File(io.BytesIO(attachments.read()), filename=attachments.filename)
    print(CHANNEL_ID)
    channel = client.get_channel("944715470047703090")
    print(channel.type)
    if channel:
        await channel.send(content="build Succeeded", file=attachments_file)
        return jsonify({'status':"success workings "}),200
    else:
        print("Channel ID invalid")
        await channel.send(content="build Succeeded")
        return jsonify({'status':"success Failed"}),200

@app.route('/fail', methods=['POST'])
async def fail():
    attachments = request.files['attachment']
    if  not attachments:
        return jsonify({'status':" Errors "}),400
    attachments_file = discord.File(io.BytesIO(attachments.read()), filename=attachments.filename)
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(content="Build Failed", file=attachments_file)
        return jsonify({'status':"success workings "}),200
    else:
        print("Channel ID invalid")
        await channel.send(content="build failed")
        return jsonify({'status':"success Failed"}),200

@client.event
async def on_ready(): 
    print(TokenEnv)
    print(ChannelEnv)
    print(f'logged in as {client.user.name}')
    print("bot Started")
    print("Starting Flask")
    Flask_thread=threading.Thread(target=run_flask)
    Flask_thread.start()

def run_flask():
    app.run(host='0.0.0.0', port=5000)

if __name__=='__main__':
    try:
        client.run(token=Token)

    except Exception as e:
        print(f'An error has occured: {e}')