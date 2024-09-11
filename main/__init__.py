#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 25933128
API_HASH = "7478fdb23a39fa343103e9a65786e996"
BOT_TOKEN = "7475809676:AAF8AdZTQxQkmWpmHFSd213W9ZaoozNs7oU"
SESSION = "BQGLtUgAYmN5yVTEeheLDZae883ngsomNxGM2CuxGmjVpR_dH6aVdN_UcLp91Q1wz_GXhfis4v74yoJLAX7bk9FHcFoDJqGqdzXgoK-YLbFiOzC6Oi7tPb-c8wXjiTtnv-ZGCNasL-UkSvGdWFz14Ct5jmBwL0X6rb_J3ufr04sFHXCEh1lV6Uc4VHm5lo1rs3u2P9uP8rkzIxgVgr4m7SCt6e3IETPm1b3eh8kXU3YxLngYpQklazi8FMtPM41tbahgzcDZYDp2BnItcfzxh_dxbuw9nFjEtxH4I4t5Ns5UW-5CVCBBHSLpSeRX7d7kSfGZ4KcYn2ruOhQ0QOucDtwHKQAAAAG3jj2zAA"
FORCESUB = 
AUTH = 7450879906

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
