import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = "1617181308:AAH0DGrfbQoD6webTZD0MXvOtmm2GRYCB-c"
admins = [
    312980854,
]



ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
