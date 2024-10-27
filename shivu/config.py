class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7038202445"
    sudo_users = "7757912959",
    GROUP_ID = -1002252184024
    TOKEN = "7297627525:AAGwV9BHee2Qisn4u12--4710r26OhHBWRk"
    mongo_url = "mongodb+srv://GOKU:MISSBHOPALI@goku.pzzsl8d.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://files.catbox.moe/ofeqts.jpg"]
    SUPPORT_CHAT = "https://t.me/Anime_Group_India_Chat"
    UPDATE_CHAT = "https://t.me/Shorekeeper_updates"
    BOT_USERNAME = "HosinoXharembot"
    CHARA_CHANNEL_ID = "-1002252184024"
    api_id = 23028479
    api_hash = "c1e6a93b04c0810a5c282d8d8d44ea6f"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
