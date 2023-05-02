from vkbottle import Bot
from config import api, state_dispancer
from handlers import labeler


if __name__ == '__main__':
    labeler.load(labeler)
    bot = Bot(api=api, labeler=labeler, state_dispenser=state_dispancer)
    bot.run_forever()