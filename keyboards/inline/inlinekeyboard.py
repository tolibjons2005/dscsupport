from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


cancel = InlineKeyboardMarkup(row_width=1)
cancelinkb= InlineKeyboardButton(text="🔙Ortga", callback_data="back")
cancel.insert(cancelinkb)
"""
doctorsuz=InlineKeyboardButton("👩‍⚕Shifokorlarimiz👨‍⚕", callback_data="doctorrsuz")
phoneuz = InlineKeyboardButton('📞Telefon raqamlarimiz☎',callback_data="pphoneuz")
adressuz = InlineKeyboardButton("🗺Manzilimiz🗺", callback_data="adresssuz")
socialuz = InlineKeyboardButton("🌐Internetdagi manzillarimiz🌐", callback_data="interntus")
reportuz = InlineKeyboardButton('⚠Taklif,shikoyat va murojaatlar uchun⚠', callback_data="rrepotuz")
back = InlineKeyboardButton("🔙Ortga", callback_data="back")
amenz = InlineKeyboardMarkup().add(doctorsuz).row(phoneuz,adressuz).add(socialuz).add(reportuz)
"""
phonesuz = InlineKeyboardMarkup()
phonelins1 = InlineKeyboardButton("asdfsf", phone_button="tel:+998994098257")
phonesuz.add(phonelins1)