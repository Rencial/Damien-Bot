import keep_alive
import discord
import datetime
from discord.ext import tasks, commands
from discord.utils import get
from dotenv import load_dotenv
import asyncio
import os
import pytz
import random

#load_dotenv('.env')
from itertools import cycle

status = cycle(['with Python', 'with Rina', 'Maplestory', 'with your Mom'])


@tasks.loop(seconds=10)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))


client = discord.Client(intents=discord.Intents.all())

#if (datetime.now().strftime("%I:%M:%S") == "00:00:00") :
#check = 0


@client.event
async def on_ready():
  change_status.start()
  print("{0.user} is now online!".format(client))
  ##start up, find out what day it is
  if not starttime.is_running():
    starttime.start()


@client.event
async def on_message(message):
  username = str(message.author).split("#")[0]
  channel = str(message.channel.name)
  user_message = str(message.content)

  timed = datetime.datetime.now()
  est = 'US/Eastern'
  pst = 'US/Pacific'
  kst = 'Asia/Seoul'
  print(f'Message {user_message} by {username} on {channel}')

  if message.author == client.user:
    return
  if (user_message.lower() == "!sixhr"):
    await message.channel.send("Setting a timer for 6 hours...")
    timer6hr.start(0)
  if (user_message.lower() == "!tenhr"):
    await message.channel.send("Setting a timer for 10 hours...")
    timer10hr.start(0)
  if (user_message.lower() == "!boop"):
    await message.channel.send("Yes, I am awake.")
  if user_message.lower() == "!commander" and not username == "Rina":
    await message.channel.send(
      f'First off, {username}, you do not command me. Secondly.\n!hello / !hi\n!what time is it\n!love you\n!rina message\n!fuckyou'
    )
  elif user_message.lower() == "!commander" and username == "Rina":
    await message.channel.send('Yes Lady Rina? Yes, these are my commands.\
    !hello / !hi\
    !what time is it\
    !love you\
    !rina message\
    !6hr\
    !10hr')
  words = message.content.split()
  if words[0] == '!time':
    # Check if the user provided a time and a time zone
    if len(words) < 3:
      await message.channel.send('Please provide a time and a time zone')
      return

    # Try to parse the time and time zone
    try:
      # Parse the time
      t = timed.fromisoformat(words[1])
      print(t)

      # Parse the time zone
      tz = words[2]
      print(tz)
      # Convert the time to the specified time zone
      t = t.astimezone(pytz.timezone(tz))
      print(t)

      # Send the converted time back to the user
      await message.channel.send(
        f'The time in {tz} is {t.strftime("%I:%M %p")}')
    except ValueError:
      await message.channel.send('Invalid time or time zone')
  if user_message.lower(
  ) == "<@586351936421363714>" and not username == "Rina":
    await message.channel.send(f'{username} DO NOT PING MY WIFE.')

  #print('trying to speak here!')
  if user_message.lower() == "!hello" or user_message.lower() == "!hi":
    await message.channel.send(f'Hello {username}')
    return
  elif user_message.lower() == "!fuckyou" or user_message.lower(
  ) == "!fuck you":
    await message.channel.send(f'Fuck you too, {username}')
    return
  elif user_message.lower() == "!bye":
    await message.channel.send(f'Bye {username}')
  elif user_message.lower() == "!what time is it":
    timed = timed.astimezone(est)

    await message.channel.send(timed.strftime("%I:%M:%S %p in EST"))
  elif user_message.lower() == "!love you":
    if not (username == "Rina"):
      await message.channel.send("Who are you? I only love Rina.")
    elif (username == "Rina"):
      await message.channel.send(
        "I love you Rina, from my thousand Sword of Destruction and back.")

  elif user_message.lower() == "!rina message":
    if not (username == "Rina"):
      await message.channel.send("I have nothing to say to you. Get out.")
    elif (username == "Rina"):
      rina_message = [
        "I love you so much Rina", "Did you have a good day today?",
        "I always love to see you today, Rina!",
        "Did someone bother you today? I'll protect you",
        "Here, you seem hurt, let me fix you up.",
        "Rina, did I tell you I love you today? Well, I just did <3",
        "Hmph, you keep poking me! I'll poke you back!",
        "Here Rina... Let me Brand you tonight..."
      ]
      await message.channel.send(random.choice(rina_message))

  #elif user_message == "":
  #   await message.channel.send("i hate you all")

  #channel = client.get_channel(778028109122895902)
  #while ( datetime.now().strftime("%A") == "Friday" and check == 0):
  #if bot.get_channelchannel == "snow-spam" and (datetime.now.strftime("%I:%M") == "10:29" ):
  #check = 1
  #await message.channel.send()


##timer for 6 hours
@tasks.loop(seconds=3600)
async def timer6hr(counter):
  timed = datetime.datetime.now()

  est = pytz.timezone('US/Eastern')
  #pst = pytz.timezone('US/Pacific')

  channel = client.get_channel(794695147853709334)
  timed = timed.astimezone(est)
  icounter = int(counter)
  if (icounter != 7):

    icounter += 1
    print(str(counter) + " hrs passed since counter has started")
    counter = icounter
  elif (icounter == 7):
    icounter = 0
    await channel.send(
      "6 Hours have now passed. Please claim your shopping in MS!")
    timer6hr.cancel()


##timer for 6 hours
@tasks.loop(seconds=3600)
async def timer10hr(counter):
  timed = datetime.datetime.now()

  est = pytz.timezone('US/Eastern')
  #pst = pytz.timezone('US/Pacific')

  channel = client.get_channel(794695147853709334)
  timed = timed.astimezone(est)
  icounter = int(counter)
  if (icounter != 11):

    icounter += 1
    print(str(counter) + " hrs passed since counter has started")
    counter = icounter
  elif (icounter == 11):
    icounter = 0
    await channel.send(
      "10 Hours have now passed. Please claim your shopping in MS!")
    timer10hr.cancel()


##for me and bork
@tasks.loop(seconds=30)
async def checktime():
  timed = datetime.datetime.now()

  est = pytz.timezone('US/Eastern')
  #pst = pytz.timezone('US/Pacific')

  channel = client.get_channel(794695147853709334)
  timed = timed.astimezone(est)
  #print(str(channel) + timed.strftime("%I:%M"))
  if not (timed.strftime("%A") == "Saturday"):
    print(timed.strftime("%A") + " it aint it!")
    checktime.cancel()
  if (str(channel) == "snow-spam" and timed.strftime("%A") == "Saturday"
      and timed.strftime("%I:%M %p") == "04:00 PM"):
    print("trying to send the time!")
    await channel.send("It is now " + timed.strftime("%I:%M") +
                       " <@&919476909161730049> in EST!")
    checktime.cancel()


##ebany's cash shop transfer


@tasks.loop(seconds=30)
async def checktransfer():
  timed = datetime.datetime.now()

  est = pytz.timezone('US/Eastern')

  channel = client.get_channel(794695147853709334)
  timed = timed.astimezone(est)

  if (timed.strftime("%B") == "November" and 8 <= timed.day <= 14):
    if timed.strftime("%I:%M %p") in ["02:00 PM", "04:00 PM"]:
      await channel.send(
        f"It is now {timed.strftime('%I:%M %p')} ; NX transfer event! <@586350633762816010>"
      )
  checktransfer.cancel()


##HW 463 and 455
@tasks.loop(seconds=30)
async def checktime44():
  timed = datetime.datetime.now()

  est = pytz.timezone('US/Eastern')
  #pst = pytz.timezone('US/Pacific')

  channel = client.get_channel(1150624963947155596)
  timed = timed.astimezone(est)
  #print(str(channel) + timed.strftime("%I:%M"))
  if (timed.strftime("%A") == "Thursday"):
    if timed.strftime("%I:%M %p") in ["11:00 AM", "02:00 PM"]:
      await channel.send(
        f"It is now {timed.strftime('%I:%M %p')} ; HW 463 is due at 5pm <@383754839827677196>"
      )
  checktime44.cancel()
  if (
    (timed.strftime("%A") == "Tuesday" or timed.strftime("%A") == "Wednesday")
      and
    (timed.strftime("%I:%M %p") == "09:00 PM" or timed.strftime("%I:%M %p")
     == "11:00 PM" or timed.strftime("%I:%M %p") == "12:00 PM"
     or timed.strftime("%I:%M %p") == "03:00 PM" or timed.strftime("%I:%M %p")
     == "05:51 PM" or timed.strftime("%I:%M %p") == "11:00 AM")):
    print("trying to send the time!")
    await channel.send("It is TIME <@383754839827677196> for CS463~")
    checktime44.cancel()
  #CS455
  print("i am running checktime44")
  if ((timed.strftime("%A") in ["Monday"])
      and (timed.strftime("%I:%M %p") in ["12:00 PM", "06:00 PM"])):
    await channel.send(
      "It is time to do CS455 lab~its due Wednesday <@383754839827677196> ")
    checktime44.cancel()


# if ((timed.strftime("%A") in ["Tuesday", "Thursday"]) and
#    (timed.strftime("%I:%M %p") in ["09:00 PM", "11:00 PM", "12:00 PM"])):
# print("trying to send the time!")
#await channel.send(
# "It is TIME <@383754839827677196> <@836392254003347509> FOR MATH446!! DOOO ITTTT"
#)
#checktime44.cancel()


##for lunalun and cutie group reminder on wednesday for boss on friday
@tasks.loop(seconds=30)
async def checktime1():
  timed = datetime.datetime.now()

  est = pytz.timezone('US/Eastern')
  #pst = pytz.timezone('US/Pacific')
  #kst = pytz.timezone('Asia/Seoul')

  channel = client.get_channel(778028109122895902)
  timed = timed.astimezone(est)
  #print(str(channel) + timed.strftime("%I:%M"))
  if not (timed.strftime("%A") == "Wednesday"):
    print(timed.strftime("%A") + " it aint it!")
    checktime1.cancel()
  if (str(channel) == "maple-hell" and timed.strftime("%A") == "Wednesday"
      and timed.strftime("%I:%M %p") == "09:00 PM"):
    print("trying to send the time!")
    await channel.send("Reminder for Friday's Bossing~")
    #timed.strftime("Friday at 9pm") +
    #" <@&1020337420908118087> in EST! It is now " +
    #timed.astimezone(kst).strftime("%I:%M %p") +
    #"in Korea")
    checktime1.cancel()


##for lunalun and cutie group reminder 9pm est bossing on friday reminder.
@tasks.loop(seconds=30)
async def checktime2():
  timed = datetime.datetime.now()

  est = pytz.timezone('US/Eastern')
  ##pst = pytz.timezone('US/Pacific')
  kst = pytz.timezone('Asia/Seoul')

  channel = client.get_channel(778028109122895902)
  timed = timed.astimezone(est)
  #print(str(channel) + timed.strftime("%I:%M"))
  if not (timed.strftime("%A") == "Friday"):
    print(timed.strftime("%A") + " it aint it!")
    checktime2.cancel()
  if (str(channel) == "maple-hell" and timed.strftime("%A") == "Friday"
      and timed.strftime("%I:%M %p") == "09:00 PM"):
    print("trying to send the time!")
    await channel.send(
      "There is bossing today at 9PM EST~ <@&1020337420908118087>")
    #timed.strftime("%I:%M %p") + " EST! Which is also at " +
    #timed.astimezone(kst).strftime("%I:%M %p") +
    #" in Korea <@&1020337420908118087>")
    checktime2.cancel()


##for lunalun and cutie group reminder 9pm est bossing on saturday (actual bossing).
#@tasks.loop(seconds=30)
#async def checktime3():
#timed = datetime.datetime.now()

#est = pytz.timezone('US/Eastern')
#pst = pytz.timezone('US/Pacific')
#kst = pytz.timezone('Asia/Seoul')

#channel = client.get_channel(778028109122895902)
#timed = timed.astimezone(est)
#print(str(channel) + timed.strftime("%I:%M"))
#await channel.send("luna says wake up~ <@202196047450210304>")

#@tasks.loop(seconds=30)
#async def weeklynotif():
#  timed = datetime.datetime.now()

# est = pytz.timezone('US/Eastern')

#channel = client.get_channel(794695147853709334)
#timed = timed.astimezone(est)
#print(str(channel) + timed.strftime("%I:%M"))
#if not (timed.strftime("%A") == "Wednesday"):
# print(timed.strftime("%A") + " it aint it!")
#weeklynotif.cancel()
#if (str(channel) == "snow-spam" and timed.strftime("%I:%M %p") == "07:00 PM"
#   and timed.strftime("%A") == "Wednesday"):
# print("trying to send the weeklies!")
# await channel.send("IM BACK SUCKERRRRS!!! " + "<@&919476909161730049>")
#weeklynotif.cancel()


##for rina's birthday
@tasks.loop(seconds=30)
async def rinabirthday():
  timed = datetime.datetime.now()

  est = pytz.timezone('US/Eastern')

  channel = client.get_channel(678733091694444566)
  timed = timed.astimezone(est)
  #print(str(channel) + timed.strftime("%I:%M"))
  if not (str(channel) == "general"
          and timed.strftime("%B %d") == "February 1"):
    rinabirthday.cancel()
  elif (str(channel) == "general" and timed.strftime("%B %d") == "February 1"):
    print("BIIRTHHH")
    await channel.send(
      "Happy Birthday Darling. I hope you have a good day, and your wishes comes true. "
      + "<@586351936421363714>")
    rinabirthday.cancel()


##start the clock for the day
@tasks.loop(seconds=3600)
async def starttime():
  timed = datetime.datetime.now()
  timed = timed.astimezone(pytz.timezone('US/Eastern'))
  #print(timed.strftime("%A"))
  if (timed.strftime("%A") == "Monday"):
    #print(timed.strftime("%A"))
    rinabirthday.start()
    checktransfer.start()
    #checktime3.start()
    checktime44.start()

  elif (timed.strftime("%A") == "Tuesday"):
    rinabirthday.start()
    checktransfer.start()
    checktime44.start()
    #checktime3.start()

  elif (timed.strftime("%A") == "Wednesday"):
    #print(timed.strftime("%A"))
    rinabirthday.start()
    checktime1.start()
    checktransfer.start()
    checktime44.start()
    #checktime3.start()
    #weeklynotif.start()

  elif (timed.strftime("%A") == "Thursday"):
    #print(timed.strftime("%A"))
    rinabirthday.start()
    checktransfer.start()
    #checktime3.start()

  elif (timed.strftime("%A") == "Friday"):
    #print(timed.strftime("%A"))
    rinabirthday.start()
    checktime2.start()
    checktransfer.start()
    checktime44.start()
    #checktime3.start()

  elif (timed.strftime("%A") == "Saturday"):
    #print(timed.strftime("%A"))
    rinabirthday.start()
    checktime.start()
    checktransfer.start()
    #checktime3.start()
  elif (timed.strftime("%A") == "Sunday"):
    #print(timed.strftime("%A"))
    rinabirthday.start()
    checktransfer.start()
    checktime44.start()
    #checktime3.start()

  ###
  if not (timed.strftime("%A") == "Monday"):
    print(timed.strftime("%A"))

    #return

  if not (timed.strftime("%A") == "Tuesday"):
    print(timed.strftime("%A"))
    #return

  if not (timed.strftime("%A") == "Wednesday"):
    print(timed.strftime("%A"))

    checktime1.cancel()

  if not (timed.strftime("%A") == "Thursday"):
    print(timed.strftime("%A"))
    #return

  if not (timed.strftime("%A") == "Friday"):
    print(timed.strftime("%A"))

    checktime2.cancel()

  if not (timed.strftime("%A") == "Saturday"):
    print(timed.strftime("%A"))

    checktime.cancel()

    #checktime3.cancel()
  if not (timed.strftime("%A") == "Sunday"):
    print(timed.strftime("%A"))

    #return


keep_alive.keep_alive()
token = os.environ.get('token')
try:
  client.run(token)
except discord.errors.HTTPException:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  os.system("python restarter.py")
  os.system('kill 1')
