#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6794664235:AAGIHPV9WGyLZmMP_w9djdS4wK9aBH5uPhI")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "16674747"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "b2de5fa3bd61ca397fbb650b0435d792")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001817115017"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1983980399"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://p:pendii11@cluster0.5z0yl.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001899541435"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI work for Asya Redroom.")
try:
    ADMINS = [
        int(x)
        for x in (
            os.environ.get(
                "ADMINS",
                "5488952329",
            ).split()
        )
    ]
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "True") == "True"

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = (
    os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
)
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.extend((OWNER_ID, 1250450587))
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
