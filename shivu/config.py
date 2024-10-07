class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7089408502"
    sudo_users = "6845325416", "1647602447"
    GROUP_ID = -1002210286036
    TOKEN = "7564089592:AAH9w8KMHroJqxTFhWxJky1TKGCyVQWzxfg"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://files.catbox.moe/ofeqts.jpg"]
    SUPPORT_CHAT = "ANIME_CHAT_GROUP_ZTX"
    UPDATE_CHAT = "ZTX_ORG"
    BOT_USERNAME = "Guess_Your_Character_bot"
    CHARA_CHANNEL_ID = "-1002210286036"
    api_id = 26627014
    api_hash = "1df5b09d720bb0174708e9077011c145"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
