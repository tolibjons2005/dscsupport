from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



languz=KeyboardButton("🇺🇿O‘zbek🇺🇿")
langru=KeyboardButton("🇷🇺Русский🇷🇺")
lang_kb=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(languz).add(langru)

aboutsuz=KeyboardButton("Biz haqimizda")
consultuz=KeyboardButton("Bepul maslahat")
bac = KeyboardButton("🔄Повторный выбор языка🇷🇺", callback_data="cancel")
menuz=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(aboutsuz, consultuz ).add(bac)


aboutsuz=KeyboardButton("О нас")
consultuz=KeyboardButton("Бесплатная консультация")
bac = KeyboardButton("🔄Tilni qayta tanlash🇺🇿", callback_data="cancel")
menru=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(aboutsuz, consultuz ).add(bac)

# doctorsuz=KeyboardButton("👩‍⚕Shifokorlarimiz👨‍⚕")
phoneuz=KeyboardButton('📞Telefon raqamlarimiz☎')
adressuz=KeyboardButton("🗺Manzilimiz🗺")
socialuz=KeyboardButton("🌐Internetdagi manzillarimiz🌐")
reportuz=KeyboardButton('⚠Taklif,shikoyat va murojaatlar uchun⚠')
back = KeyboardButton("🔙Ortga")
amenuz = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(phoneuz,adressuz).add(socialuz).add(back)

bask = KeyboardButton("🔙Ortga")
hask = KeyboardButton("🔙Назад")
vask = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(bask, hask)

# doctorsuz=KeyboardButton("👩‍⚕Наши врачи👨‍⚕")
phoneuz=KeyboardButton('📞Наши телефоны☎')
adressuz=KeyboardButton("🗺Наш адресс🗺")
socialuz=KeyboardButton("🌐Наши адреса в интернете🌐")
reportuz=KeyboardButton('⚠Для предложений, жалоб и обращений⚠')
back = KeyboardButton("🔙Назад")
amenru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(phoneuz,adressuz).add(socialuz).add(back)
# .add(doctorsuz)
# .add(doctorsuz)

"""
menu = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="🇺🇿O‘zbek🇺🇿"),
    ],
    [
        KeyboardButton(text="🇷🇺Русский🇷🇺")
    ],
    ]
)
"""