from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from loader import dp
from filters import IsAdmin, IsUser
import keyboards.inline.inlinekeyboard as ins
import keyboards.default.keyboard as kb
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from aiogram.utils.callback_data import CallbackData





@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(
        '🇺🇿Salom!👋\n"Dilshod Stom" xususiy klinikasining rasmiy Telegram-botiga\n xush kelibsiz!\nIltimos, pastdan o‘zingizga kerak bo‘lgan tilni tanlang.\n \n🇷🇺Здравствуйте!👋\nДобро пожаловать в официальный Telegram-бот частной клиники "Dilshod Stom"!\nПожалуйста, выберите нужный вам язык ниже.',
        reply_markup=kb.lang_kb)


async def process_tart_command(message: types.Message):
    await message.reply(
        '🇺🇿Salom!👋\n"Dilshod Stom" xususiy klinikasining rasmiy Telegram-botiga\n xush kelibsiz!\nIltimos, pastdan o‘zingizga kerak bo‘lgan tilni tanlang.\n \n🇷🇺Здравствуйте!👋\nДобро пожаловать в официальный Telegram-бот частной клиники "Dilshod Stom"!\nПожалуйста, выберите нужный вам язык ниже.',
        reply_markup=kb.lang_kb)

async def process_rutart_command(message: types.Message):
    await message.reply(
        '🇺🇿Salom!👋\n"Dilshod Stom" xususiy klinikasining rasmiy Telegram-botiga\n xush kelibsiz!\nIltimos, pastdan o‘zingizga kerak bo‘lgan tilni tanlang.\n \n🇷🇺Здравствуйте!👋\nДобро пожаловать в официальный Telegram-бот частной клиники "Dilshod Stom"!\nПожалуйста, выберите нужный вам язык ниже.',
        reply_markup=kb.lang_kb)


dp.register_message_handler(process_tart_command, Text(equals="🔄Повторный выбор языка🇷🇺"))
dp.register_message_handler(process_tart_command, Text(equals="🔄Tilni qayta tanlash🇺🇿"))




@dp.message_handler(Text(equals='🇺🇿O‘zbek🇺🇿'))
async def process_menu_command(message: types.Message):
    await message.reply("Kerakli bo‘limni tanlang!", reply_markup=kb.menuz)

async def process_rumenu_command(message: types.Message, state: FSMContext):
    await message.reply("Выберите нужный раздел!", reply_markup=kb.menru)

async def process_r2umenu_command(message: types.Message, state: FSMContext):
    await message.reply("Выберите нужный раздел!", reply_markup=kb.menru)








async def process_art_command(message: types.Message):
    await message.reply("Kerakli bo‘limni tanlang!", reply_markup=kb.menuz)


dp.register_message_handler(process_rumenu_command, Text(equals="🇷🇺Русский🇷🇺" or "🔙Назад"))
dp.register_message_handler(process_r2umenu_command, Text(equals="🔙Назад"))
dp.register_message_handler(process_art_command, text="🔙Ortga")


#


# Где-то в другом месте...


@dp.message_handler(Text(equals='Biz haqimizda'))
async def process_menu_command(message: types.Message):
    await message.reply("Выберите нужный раздел!", reply_markup=kb.amenuz)

async def process_rumenu_command(message: types.Message):
    await message.reply("Kerakli bo‘limni tanlang!", reply_markup=kb.amenru)


dp.register_message_handler(process_rumenu_command, text="О нас")



# @dp.message_handler()
# async def echo_message(msg: types.Message):
# await bot.send_message(msg.from_user.id, msg.text)


@dp.message_handler(text="👩‍⚕Shifokorlarimiz👨‍⚕")
async def doctor_button(message: types.Message):
    await message.answer("Ishladi")


@dp.message_handler(text="📞Telefon raqamlarimiz☎")
async def doctor_button(message: types.Message):
    await message.answer(
        "☎<b>Telefon raqamlarimiz:</b>\n\n📞+998994098257\n\n⚠<i>Iltimos 9:00-18:00 oralig‘ida qo‘ng‘iroq qiling!</i>",
        parse_mode=types.ParseMode.HTML)

async def phoneru_button(message: types.Message):
    await message.answer(
        "☎<b>Наши телефоны:</b>\n\n📞+998994098257\n\n⚠<i>Пожалуйста, звоните с 9:00 до 18:00!</i>",
        parse_mode=types.ParseMode.HTML)

dp.register_message_handler(phoneru_button, text="📞Наши телефоны☎")



@dp.message_handler(text="🌐Internetdagi manzillarimiz🌐")
async def doctor_button(message: types.Message):

    await message.answer(
        '<b>Internetdagi manzillarimiz:</b>\n\n<a href="https://www.facebook.com/dilshodstomclinic">Facebook sahifamiz</a>\n<a href="https://www.instagram.com/dilshodstom_clinic/">Instagram sahifamiz</a>\n<a href="https://t.me/dilshodstom_clinic">Telegram kanalimiz</a>\n<a href="https://t.me/dsc_group">Telegram guruhimiz</a>\n<a href="https://www.youtube.com/channel/UCEs_zvIoIKZ5j8tXfN-c9kg">YouTube kanalimiz</a>',
        parse_mode=types.ParseMode.HTML)

async def netpage_button(message: types.Message):
    await message.answer(
        '<b>Наши адреса в Интернете:</b>\n\n<a href="https://www.facebook.com/dilshodstomclinic">Наша страница в фейсбуке</a>\n<a href="https://www.instagram.com/dilshodstom_clinic/">Наша страница в инстаграм</a>\n<a href="https://t.me/dilshodstom_clinic">Наш телеграм-канал</a>\n<a href="https://t.me/dsc_group">Наша группа Telegram</a>\n<a href="https://www.youtube.com/channel/UCEs_zvIoIKZ5j8tXfN-c9kg">Наш канал на YouTube</a>',
        parse_mode=types.ParseMode.HTML)

dp.register_message_handler(netpage_button, text="🌐Наши адреса в интернете🌐")

@dp.message_handler(text="🗺Manzilimiz🗺")
async def doctor_button(message: types.Message):
    link='<a href="https://clck.ru/UMBdj">Ustiga bosing</a>'
    await message.answer('<b>Manzilimiz:</b>\nToshkent viloyati, Qibray tumani, "Chimkent Yo‘li" ko‘chasi, 139a-uy.\n\n<b>Mo‘ljal:</b>\n "Karvonsaroy" choyxonasi.\n\n<i>Pastdagi havolani kerakli dastur orqali ochish orqali ham klinikamizni topishingiz mumkin!</i>',  parse_mode=types.ParseMode.HTML)
    await message.answer(link,  parse_mode=types.ParseMode.HTML)

async def adressbar_button(message: types.Message):
    link='<a href="https://clck.ru/UMBdj">Нажмите здесь</a>'
    await message.answer('<b>Наш адресс:</b>\nТашкентская область, Кибрайский район,улица "Chimkent Yo‘li", 139а дом.\n\n<b>Орентир:</b>\n "Karvonsaroy" чайхана.\n\n<i>Вы также можете найти нашу клинику, открыв ссылку через нужное приложение!</i>',  parse_mode=types.ParseMode.HTML)
    await message.answer(link,  parse_mode=types.ParseMode.HTML)

dp.register_message_handler(adressbar_button, text="🗺Наш адресс🗺")



# dp.register_message_handler(cmd_test2, commands="test2")

@dp.callback_query_handler(text="cancel")
async def phone_button(call: CallbackQuery):
    await call.message.answer("Ishladi", reply_markup=ins.phonesuz)


@dp.callback_query_handler(text="1")
async def back_button(call: CallbackQuery):
    await call.answer(
        '🇺🇿Salom!👋\n"Dilshod Stom" xususiy klinikasining rasmiy Telegram-botiga\n xush kelibsiz!\nIltimos, pastdan o‘zingizga kerak bo‘lgan tilni tanlang.\n \n🇷🇺Здравствуйте!👋\nДобро пожаловать в официальный Telegram-бот частной клиники "Dilshod Stom"!\nПожалуйста, выберите нужный вам язык ниже.',
        reply_markup=kb.lang_kb, show_alert=True)




catalog = '🛍️ Каталог'
balance = '💰 Баланс'
cart = '🛒 Корзина'
delivery_status = '🚚 Статус заказа'

settings = '⚙️ Настройка каталога'
orders = '🚚 Заказы'
questions = 'savollarbormiuka'

@dp.message_handler(IsAdmin(), commands='menu')
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(settings)
    markup.add(questions, orders)

    await message.answer('Меню', reply_markup=markup)

@dp.message_handler(IsUser(), commands='menu')
async def user_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(catalog)
    markup.add(balance, cart)
    markup.add(delivery_status)

    await message.answer('Меню', reply_markup=markup)


