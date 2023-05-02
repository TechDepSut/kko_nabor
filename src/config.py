from vkbottle import BuiltinStateDispenser, API
from vkbottle.bot import BotLabeler
import os


api = API(os.environ.get("TOKEN"))
labeler = BotLabeler()
state_dispancer =  BuiltinStateDispenser()