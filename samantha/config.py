# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1722127255:AAGD8YpaGk5KhkRQWE7Y7ws4Q43ilW5iUo0"
    OWNER_ID = (
        "1838880848"  # If you dont know, run the bot and do /id in your private chat with it
    )
    OWNER_USERNAME = "HiSabo"
    TELETHON_HASH = "93601b58e1ca8309238701d7ea9dc078"   # for purge stuffs
    TELETHON_ID = 5790236

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://hzjjtjfpxdhzax:299b7e8170a928ac0f2fab3b1fa16a653c2ec5d93336ccd541421b671fcf4721@ec2-34-232-191-133.compute-1.amazonaws.com:5432/dp3poevb7pmq6"  # needed for any database modules
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
    PORT = 5432
    DEL_CMDS = True  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = None  # banhammer marie sticker
    ALLOW_EXCL = True  # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /
    CUSTOM_CMD = False # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with more custom handler!
    API_OPENWEATHER = None  # OpenWeather API
    SPAMWATCH_API = None # Your SpamWatch token
    WALL_API = None

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
