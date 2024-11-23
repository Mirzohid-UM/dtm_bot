from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup



menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📊Ball yetadigan yo'nalishlar",)],
        [KeyboardButton(text="Mandat natijasi",),KeyboardButton(text="Yo'nalishlar bo'yicha")],
        [KeyboardButton(text="Viloyat kesimida"),KeyboardButton(text="2023- yil ballar")]
    ],
        resize_keyboard=True
 )
location_contact_button = ReplyKeyboardMarkup(

        keyboard=[
            [KeyboardButton(text= "Lakatsiya yuborish", request_location=True)],
            [KeyboardButton(text="Kontakt Yuborish", request_contact=True )]
        ],
    resize_keyboard=True
)


channel_list=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kanal-1", url="https://t.me/Mirzohid_Portfolio")
        ],
        [
            InlineKeyboardButton(text="Tekshirish ✅", callback_data="check_subsciption")
        ]
    ]
)
