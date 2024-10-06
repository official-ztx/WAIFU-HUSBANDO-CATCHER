class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6765826972"
    sudo_users = "6845325416", "6765826972"
    GROUP_ID = -1002202172045
    TOKEN = "6707490163:AAHZzqjm3rbEZsObRiNaT7DMtw_i5WPo_0o"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "ANIME_CHAT_GROUP_ZTX"
    UPDATE_CHAT = "ZTX_ORG"
    BOT_USERNAME = "Collect_Em_AllBot"
    CHARA_CHANNEL_ID = "-1002202172045"
    api_id = 26627014
    api_hash = ""

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
