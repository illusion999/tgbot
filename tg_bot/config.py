from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1410616929  # my telegram ID
    OWNER_USERNAME = "MysticOp"  # my telegram username
    API_KEY = "1745756051:AAHs2614ly6ruWYZUUtHBznX-gRbZ9u3mwY"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://ewawttkr:JbHw9yQf3Uj5qNxGC2wLvGVY0Z_L1f9Q@satao.db.elephantsql.com:5432/ewawttkr'  # sample db credentials
    MESSAGE_DUMP = '-1001309372845' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1047091391, 1678331806]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
