from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

language = ReplyKeyboardMarkup(
    keyboard = [
        [
        KeyboardButton(text = "Uzbek ➡️ English"),
        KeyboardButton(text = "English ➡️ Uzbek"),
        
        ],
        [
        KeyboardButton(text = "Uzbek ➡️ Russian"),
        KeyboardButton(text = "Russian ➡️ Uzbek"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Menudan birini tanlang"
)
