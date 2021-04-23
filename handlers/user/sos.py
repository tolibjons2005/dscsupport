from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from keyboards.default.markups import all_right_message, cancel_message, submit_markup
from aiogram.types import Message
from states import SosState
from filters import IsUser
from loader import dp, db
from aiogram.dispatcher.filters import Text
import keyboards.default.keyboard as kb


@dp.message_handler(Text(equals='Бесплатная консультация'))
async def cmd_sos(message: Message):
    await SosState.question.set()


    await message.answer('В чем суть проблемы? Опишите как можно подробнее, и мы обязательно вам ответим.\n\n<i>Для повышения качества консультации уточните вопрос и отправьте его одним сообщением.</i>', reply_markup=ReplyKeyboardRemove(), parse_mode=types.ParseMode.HTML)

@dp.message_handler(Text(equals='Bepul maslahat'))
async def cmd_sos(message: Message):
    await SosState.question.set()


    await message.answer('Muammo nimada? Iloji boricha batafsilroq tavsiflab bering va biz sizga albatta javob beramiz.\n\n<i>Konsultatsiya sifatini oshirish uchun savolni tushunarli qilib, bitta xabarda yuboring.</i>', reply_markup=ReplyKeyboardRemove(), parse_mode=types.ParseMode.HTML)


@dp.message_handler(state=SosState.question)
async def process_question(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['question'] = message.text

    
    await message.answer('Barchasi to‘g‘riligiga ishinch hosil qiling. \n\nУбедитесь, что все верно.', reply_markup=submit_markup())
    await SosState.next()
    
    
dp.register_message_handler(process_question, state=SosState.question)


@dp.message_handler(lambda message: message.text not in [cancel_message, all_right_message], state=SosState.submit)
async def process_price_invalid(message: Message):
    await message.answer('Iltimos pastdagi tugmalardan birini bosing.\n\nПожалуйста, нажмите одну из кнопок ниже.')


@dp.message_handler(text=cancel_message, state=SosState.submit)
async def process_cancel(message: Message, state: FSMContext):
    await message.answer('Bekor qilindi!\n\nОтменено!', reply_markup=kb.vask)
    await state.finish()


@dp.message_handler(text=all_right_message, state=SosState.submit)
async def process_submit(message: Message, state: FSMContext):
    cid = message.chat.id

    if db.fetchone('SELECT * FROM questions WHERE cid=?', (cid,)) == None:

        async with state.proxy() as data:
            db.query('INSERT INTO questions VALUES (?, ?)',
                     (cid, data['question']))

        await message.answer('Jo‘natildi! Tez orada javob qaytaramiz.\n\nОтправлено! Мы ответим в ближайшее время.', reply_markup=kb.vask)

    else:

        await message.answer('Berilgan savollar sonining chegarasi oshib ketdi. Birinchi savolingizga javob olganingizdan keyin jo‘nating.\n\nПревышен лимит на количество задаваемых вопросов. Отправьте, когда получите ответ на свой первый вопрос.', reply_markup=kb.vask)

    await state.finish()

# @dp.message_handler(state=SosState.question)
# async def process_question(message: Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['question'] = message.text
#         
#     if til ==2:
#         textn
# 
#     await message.answer('Убедитесь, что все верно.', reply_markup=submit_markup())
#     await SosState.next()
# 
# 
# @dp.message_handler(lambda message: message.text not in [cancel_message, all_right_message], state=SosState.submit)
# async def process_price_invalid(message: Message):
#     await message.answer('Такого варианта не было.')
# 
# 
# @dp.message_handler(text=cancel_message, state=SosState.submit)
# async def process_cancel(message: Message, state: FSMContext):
#     await message.answer('Отменено!', reply_markup=ReplyKeyboardRemove())
#     await state.finish()
# 
# 
# @dp.message_handler(text=all_right_message, state=SosState.submit)
# async def process_submit(message: Message, state: FSMContext):
# 
#     cid = message.chat.id
# 
#     if db.fetchone('SELECT * FROM questions WHERE cid=?', (cid,)) == None:
# 
#         async with state.proxy() as data:
#             db.query('INSERT INTO questions VALUES (?, ?)',
#                      (cid, data['question']))
# 
#         await message.answer('Отправлено!', reply_markup=ReplyKeyboardRemove())
# 
#     else:
# 
#         await message.answer('Превышен лимит на количество задаваемых вопросов.', reply_markup=ReplyKeyboardRemove())
# 
#     await state.finish()
