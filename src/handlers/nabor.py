from vkbottle import BaseStateGroup, Keyboard, Text
from vkbottle.bot import Message

from config import labeler, state_dispancer
from utils.user import User
from utils.google import save_info


class Nabor(BaseStateGroup):
    fio = 1
    faculty = 2
    group = 3
    why = 4
    other_group = 5
    old_group = 6
    depatament = 7


yes_no_keyboard = (
    Keyboard(one_time=True)
    .add(Text("Да"))
    .row()
    .add(Text("Нет"))
)


depatament_keyboard = (
    Keyboard(one_time=True)
    .add(Text("Контроль качества"))
    .row()
    .add(Text("SMM"))
    .row()
    .add(Text("Design"))
)

keyboard = (
    Keyboard(one_time=True)
    .add(Text("ИКСС"))
    .row()
    .add(Text("ИСиТ"))
    .row()
    .add(Text("РТС"))
    .row()
    .add(Text("СЦТ"))
    .row()
    .add(Text("ЦЭУБИ"))
    .row()
    .add(Text("ФП"))
    .row()
    .add(Text("ИНО"))
    .row()
    .add(Text("ИМ"))
    .row()
    .add(Text("СПбКТ"))
)


@labeler.message(text="Начать")
async def fio(message: Message):
    await message.answer(
        "Чтобы подать заявку в ККО, нужно ответить на несколько следующих вопросов."
    )
    user = User()
    await message.answer("Введи ФИО")
    await state_dispancer.set(message.peer_id, Nabor.fio, user=user)


@labeler.message(state=Nabor.fio)
async def faculty(message: Message):
    print(message.state_peer.payload)
    user: User | None = message.state_peer.payload["user"]
    user.set_name(message.text)
    await message.answer("Выбери свой факультет", keyboard=keyboard)
    await state_dispancer.set(message.peer_id, Nabor.faculty, user=user)

@labeler.message(state=Nabor.faculty)
async def group(message: Message):
    user: User | None = message.state_peer.payload["user"]
    user.set_faculty(message.text)
    await message.answer("Номер академической группы")
    await state_dispancer.set(message.peer_id, Nabor.group, user=user)

@labeler.message(state=Nabor.group)
async def why(message: Message):
    user: User | None = message.state_peer.payload["user"]
    user.set_group(message.text)
    await message.answer("Почему хочешь в ККО?")
    await state_dispancer.set(message.peer_id, Nabor.why, user=user)

@labeler.message(state=Nabor.why)
async def other_group(message: Message):
    user: User | None = message.state_peer.payload["user"]
    user.set_why(message.text)
    await message.answer("В каких подразделениях ты состоишь кроме ККО?")
    await state_dispancer.set(message.peer_id, Nabor.other_group, user=user)

@labeler.message(state=Nabor.other_group)
async def depatament(message: Message):
    user: User | None = message.state_peer.payload["user"]
    user.set_other_group(message.text)
    await message.answer("В каком подразделении ты состоял?")
    await state_dispancer.set(message.peer_id, Nabor.old_group, user=user)

@labeler.message(state=Nabor.old_group)
async def end(message: Message):
    if message.text == "Нет":
        await message.answer("Спасибо за заявку")
        user: User | None = message.state_peer.payload["user"]
        print(user.get_department())
        save_info(user)
        await state_dispancer.set(message.peer_id, None)
        return
    user: User | None = message.state_peer.payload["user"]
    if user.get_old_group() is None:
        user.set_old_group(message.text)
    await message.answer("В какой отдел кко ты хочешь попасть?", keyboard=depatament_keyboard)
    await state_dispancer.set(message.peer_id, Nabor.depatament, user=user)


@labeler.message(state=Nabor.depatament)
async def end(message: Message):
    user: User | None = message.state_peer.payload["user"]
    user.set_department(message.text)
    await message.answer("Хочешь еще куда-то попасть?", keyboard=yes_no_keyboard)
    await state_dispancer.set(message.peer_id, Nabor.old_group, user=user)


@labeler.message()
async def end(message: Message):
    await message.answer("Спасибо за заявку, если хотите начать заново, то напишите \"Начать\"")