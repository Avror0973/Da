import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = "1208991081:AAE-cQN1A5S8swYd5eVa1WUmoWA8I2pQ108"
admins = [
    312980854,
    958479767,
]

allowed_users = [312980854]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
