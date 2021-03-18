if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "2901265"
    OWNER_ID = "1678331806"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "@VegetaxD"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://ewawttkr:JbHw9yQf3Uj5qNxGC2wLvGVY0Z_L1f9Q@satao.db.elephantsql.com:5432/ewawttkr'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    # sed has been disabled after the discovery that certain long-running sed commands maxed out cpu usage
    # and killed the bot. Be careful re-enabling it!
    NO_LOAD = ['translation', 'rss', 'sed']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = [1410616929]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = [1047091391]  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = [970558707]  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = 'https://paypal.me/madarchodmanik'  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
