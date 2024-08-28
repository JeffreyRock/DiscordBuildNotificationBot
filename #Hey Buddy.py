#Hey Buddy. your a chad who buys fun this like video games and stuff.

#the Actual comment. this is a bot that sends a notification to my discord server to tell me shit is, in the words of twomod is breaky
import discord
import threading
import io
import os
from flask import Flask, request,jsonify

app = Flask(__name__)
TokenEnv = "MTI3MzA3NjQ3NzUwMzQ3MTY4Nw.GaRGRy.tlrr7DskWJyX4dcblkQ97itmLUbGkvkgbFunSA"
ChannelEnv = "1163708902165204993"
intents =discord.Intents.default()
intents.messages=True
client = discord.Client(intents=intents)
Token= TokenEnv #Do not commit this line 
CHANNEL_ID= ChannelEnv

@app.route('/succeed', methods=['POST'])
def succeed():
    attachments = request.files['attachment']
    if  not attachments:
        return jsonify({'status':" Errors "}),400
    attachments_file = discord.File(io.BytesIO(attachments.read()), filename=attachments.filename)
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        client.loop.create_task(channel.send(content="build Succeeded", file=attachments_file))
        return jsonify({'status':"success workings "}),200
    else:
        return jsonify({'status':"success Failed"}),404

@app.route('/fail', methods=['POST'])
def fail():
    attachments = request.files['attachment']
    if  not attachments:
        return jsonify({'status':" Errors "}),400
    attachments_file = discord.File(io.BytesIO(attachments.read()), filename=attachments.filename)
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        client.loop.create_task(channel.send(content="Build Failed", file=attachments_file))
        return jsonify({'status':"success workings "}),200
    else:
        return jsonify({'status':"success Failed"}),404

@client.event
async def on_ready(): 
    print(TokenEnv)
    print(ChannelEnv)
    print(f'logged in as {client.user.name}')
    print("Starting bot")

def run_flask():
    app.run(host='0.0.0.0', port=5000)

if __name__=='__main__':
    try:
        client.run(token=Token)
        print("Starting Flask")
        app.run(host='0.0.0.0', port=5000) 
    except Exception as e:
        print(f'An error has occured: {e}')