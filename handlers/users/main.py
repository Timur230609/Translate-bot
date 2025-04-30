from loader import dp, db 
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import F
from translator import eng,uz,ru,ru_uz
from state.help_stt import Uzbek,English,Uzbek_ru,Russian


#uzbek--->>english
@dp.message(F.text=="Uzbek ➡️ English")
async def tarjimon(message: Message, state:FSMContext):
    await message.answer(text="Matn yoki so'z kiriting...")
    await state.set_state(Uzbek.uz)

@dp.message(Uzbek.uz)
async def uzbek(message:Message, state:FSMContext):
    text = eng(message.text)
    tarjimon = f"{message.text} ->> {text}"
    await message.answer(tarjimon)
    await state.clear()
    #end------------------------------



#english--->>uzbek
@dp.message(F.text=="English ➡️ Uzbek")
async def tarjimon(message: Message, state:FSMContext):
    await message.answer(text="Matn yoki so'z kiriting...")
    await state.set_state(English.eng)

@dp.message(English.eng)
async def english(message:Message, state:FSMContext):
    text = uz(message.text)
    tarjimon = f"{message.text} ->> {text}"
    await message.answer(tarjimon)
    await state.clear()
    #en------------------------------



#uzbek--->>russian
@dp.message(F.text=="Uzbek ➡️ Russian")
async def uzbek_ru(message: Message, state:FSMContext):
    await message.answer(text="Matn yoki so'z kiriting...")
    await state.set_state(Uzbek_ru.uz_ru)

@dp.message(Uzbek_ru.uz_ru)
async def uzbek_rus(message:Message, state:FSMContext):
    text = ru(message.text)
    tarjimon = f"{message.text} ->> {text}"
    await message.answer(tarjimon)
    await state.clear()
    #end-------------------------------


@dp.message(F.text=="Russian ➡️ Uzbek")
async def uzbek_ru(message: Message, state:FSMContext):
    await message.answer(text="Matn yoki so'z kiriting...")
    await state.set_state(Russian.ru)

@dp.message(Russian.ru)
async def uzbek_rus(message:Message, state:FSMContext):
    text = ru_uz(message.text)
    tarjimon = f"{message.text} ->> {text}"
    await message.answer(tarjimon)
    await state.clear()
    #end-------------------------------