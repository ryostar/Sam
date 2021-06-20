# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1897791328:AAFvM-m2INO1F0BFieJsOVG-yPjIa2sZ7_g"
    OWNER_ID = (
        "1816000450"  # If you dont know, run the bot and do /id in your private chat with it
    )
    OWNER_USERNAME = "Kuri69"
    TELETHON_HASH = "93601b58e1ca8309238701d7ea9dc078"   # for purge stuffs
    TELETHON_ID = 5790236

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgresql://ri:1@103.124.92.181:5432/ri"  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = (
        []
    )  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = (
        []
    )  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = (
        []
    )  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WHITELIST_CHATS = []
    BLACKLIST_CHATS = []
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = None  # banhammer marie sticker
    ALLOW_EXCL = True  # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /
    CUSTOM_CMD = "/ !" # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with more custom handler!
    API_OPENWEATHER = None  # OpenWeather API
    WALL_API = None
    SPAMWATCH_API = "D1xqiSR1PaU8LD1EYSxAHKrUXQiccZnl6BpZUNWo9W4Jt9F0xpvvzOXoQ6wvOS6y"

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
