from aiogram import Bot, Dispatcher
from data import config
from baza.sqlite import Database
from aiogram.client.session.aiohttp import AiohttpSession

session = AiohttpSession(proxy='http://proxy.server:3128')

ADMINS = config.ADMINS
TOKEN = config.BOT_TOKEN
CHANNELS = config.CHANNELS

bot = Bot(TOKEN, session=session)
db = Database(path_to_db="main.db")
dp = Dispatcher()
