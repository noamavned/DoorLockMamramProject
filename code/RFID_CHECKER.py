import time
import sys
sys.path.append('path/to/src/')
from Database import Database as db
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
sys.path.append('path/to/name/ path/to/python3.9/site-packages/')
from discord.ext import commands, tasks
import discord
from discord import app_commands
import os
import subprocess
import cv2
outPin = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(outPin, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(26, GPIO.IN)
st = 5
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)
bot.remove_command("help")

def check():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(outPin, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        reader = SimpleMFRC522()
        d = db()
        keys = d.get_keys()
        ot = d.get_tagText()
        idd, text = reader.read()
        if idd == None:
            return None
        if str(idd) not in keys:
            return text.strip() == ot.strip()
        return True
    except:
        exit()
                    
d = db()
d.res_trys()

@bot.event
async def on_ready():
    looped.start()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Hello World"))
    synced = await bot.tree.sync()
    print("I'm in")
    print(bot.user)

@bot.tree.command(name = "reboot", description = "Sets channel as main channel")
@app_commands.describe(password = "Password")
async def rebootDevice(interaction: discord.Interaction, password: str):
    if password.strip() == d.get_pass():
        await interaction.response.send_message(f'Rebooting device named {d.get_machineName()}')
        subprocess.call(['reboot'])
    else:
        await bot.get_channel(interaction.channel_id).send('**Access denied!**')

@bot.tree.command(name = "set_channel", description = "Sets channel as main channel")
@app_commands.describe(password = "Password")
async def setChannel(interaction: discord.Interaction, password: str):
    if password.strip() == d.get_pass():
        d.update_ctx(f'{interaction.channel_id}')
        await interaction.response.send_message(f'set channel to {interaction.channel_id}')
    else:
        await bot.get_channel(interaction.channel_id).send('**Access denied!**')

@bot.tree.command(name = "show_trys", description = "Shows how many trys left boefore locking lock")
async def showTrys(interaction: discord.Interaction):
    await interaction.response.send_message(f'{3 - int(d.get_trys())} trys left!')

@bot.tree.command(name = "reset_trys", description = "Resets the trys to 0")
@app_commands.describe(password = "Password")
async def resetTrys(interaction: discord.Interaction, password: str):
    if password.strip() == d.get_pass():
        d.res_trys()
        await interaction.response.send_message('Trys got reset')
    else:
        await bot.get_channel(interaction.channel_id).send('**Access denied!**')
        
@bot.tree.command(name = "beep", description = "Beeps for 5 seconds")
@app_commands.describe(password = "Password")
async def beep(interaction: discord.Interaction, password: str):
    if password.strip() == d.get_pass():
        await interaction.response.send_message('Beeping')
        GPIO.output(16, 1)
        time.sleep(5)
        GPIO.output(16, 0)
        await interaction.edit_original_response(content = 'Done')
    else:
        await bot.get_channel(interaction.channel_id).send('**Access denied!**')

@bot.tree.command(name = "unlock", description = "Unlocks the lock")
@app_commands.describe(password = "Password")
async def unlock(interaction: discord.Interaction, password: str):
    if password.strip() == d.get_pass():
        Open = d.get_open() == "true"
        if not Open:
            await interaction.response.send_message('Unlocked')
            GPIO.output(16, 1)
            time.sleep(0.25)
            GPIO.output(16, 0)
            d.update_open("true")
            GPIO.output(outPin, GPIO.LOW)
            d.res_trys()
        else:
            await bot.get_channel(interaction.channel_id).send('Already unlocked')
    else:
        await bot.get_channel(interaction.channel_id).send('**Access denied!**')

@bot.tree.command(name = "lock", description = "Locks the lock")
@app_commands.describe(password = "Password")
async def lock(interaction: discord.Interaction, password: str):
    if password.strip() == d.get_pass():
        Closed = d.get_open() == "false"
        if not Closed:
            await interaction.response.send_message('Locked')
            GPIO.output(16, 1)
            time.sleep(0.25)
            GPIO.output(16, 0)
            d.update_open("false")
            GPIO.output(outPin, GPIO.HIGH)
            d.res_trys()
        else:
            await bot.get_channel(interaction.channel_id).send('Already locked')
    else:
        await bot.get_channel(interaction.channel_id).send('**Access denied!**')
        
@bot.tree.command(name = "state", description = "Shows if lock is closed or open")
@app_commands.describe(password = "Password")
async def state(interaction: discord.Interaction, password: str):
    if password.strip() == d.get_pass():
        s = d.get_open() == "true"
        await interaction.response.send_message(f'Lock is {["Closed", "Open"][s]}')
    else:
        await bot.get_channel(interaction.channel_id).send('**Access denied!**')

@bot.tree.command(name = "send_pic", description = "Sends a picture from the camera connected to the lock")
async def sendPic(interaction: discord.Interaction):
    imagePath = '/home/noamavned/project/src/img.png'
    try:
        if os.path.exists(imagePath):
            os.remove(imagePath)
        await interaction.response.send_message('OK')
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
        cap.set(cv2.CAP_PROP_EXPOSURE, -5)
        cap.set(cv2.CAP_PROP_GAIN, 3)
        ret, frame = cap.read()
        cv2.imwrite(imagePath, frame)
        await bot.get_channel(interaction.channel_id).send(file=discord.File(imagePath))
        os.remove(imagePath)
    except:
        await bot.get_channel(interaction.channel_id).send('**Can\'t use the camera to capture**')

@bot.tree.command(name = "ping", description = "Pings the bot to show the respond time")
@app_commands.describe(password = "Password")
async def ping(interaction: discord.Interaction, password: str):
    if password.strip() == d.get_pass():
        latency = bot.latency
        await interaction.response.send_message(f'{round(latency * 1000)}ms')
    else:
        await bot.get_channel(interaction.channel_id).send('**Access denied!**')
        
@tasks.loop(seconds=1)
async def looped():
    try:
        d = db()
    except:
        exit()
    c = check()
    if c:
        GPIO.output(16, 1)
        time.sleep(0.25)
        GPIO.output(16, 0)
        iii = d.get_open()
        time.sleep(0.5)
        if iii == "true":
            d.update_open("false")
            GPIO.output(outPin, GPIO.HIGH)
        else:
            d.update_open("true")
            GPIO.output(outPin, GPIO.LOW)
        d.res_trys()
        time.sleep(2)
    elif c != None:
        d.inc_trys()
        for i in range(3):
            GPIO.output(16, 1)
            time.sleep(0.25)
            GPIO.output(16, 0)
            time.sleep(0.25)
        t = d.get_trys()
        print(f'{t} trys wrong')
        if int(t) == 3:
            d.res_trys()
            cid = d.get_ctx()
            if cid != 'None':
                await bot.get_channel(int(cid)).send(f'**Detected 3 trys to open the lock named {d.get_machineName()}!**')
                imagePath = '/home/noamavned/project/src/img.png'
                try:
                    if os.path.exists(imagePath):
                        os.remove(imagePath)
                    cap = cv2.VideoCapture(0)
                    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
                    cap.set(cv2.CAP_PROP_EXPOSURE, -5)
                    cap.set(cv2.CAP_PROP_GAIN, 3)
                    ret, frame = cap.read()
                    cv2.imwrite(imagePath, frame)
                    await bot.get_channel(int(cid)).send(file=discord.File(imagePath))
                    os.remove(imagePath)
                except:
                    await bot.get_channel(int(cid)).send('**Can\'t use the camera to capture**')
            time.sleep(5)


bot.run(d.get_token())