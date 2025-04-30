from aiogram.fsm.state import State, StatesGroup

class Help(StatesGroup):
    help = State()




class Uzbek(StatesGroup):
    uz = State()

class English(StatesGroup):
    eng = State()

class Uzbek_ru(StatesGroup):
    uz_ru = State()

class Russian(StatesGroup):
    ru = State()
