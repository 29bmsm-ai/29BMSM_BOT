import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# 🔑 Bot tokenini shu yerga joylang
API_TOKEN = "8333103716:AAGPwCcX9cP-fqDnFBJILWoV2FzpOii4ey8"

def get_main_menu():
    kb = [
        [KeyboardButton(text="🏫 Maktab haqida"), KeyboardButton(text="👨‍🏫 O‘qituvchilar")],
        [KeyboardButton(text="📅 Dars jadvali"), KeyboardButton(text="📰 Yangiliklar")],
        [KeyboardButton(text="🎓 Qabul"), KeyboardButton(text="🖼️ Fotogalereya")],
        [KeyboardButton(text="📞 Aloqa")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

async def cmd_start(message: types.Message):
    text = (
        "🎓 *29BMSM InfoBot* ga xush kelibsiz!\n\n"
        "Quyidagi bo‘limlardan birini tanlang 👇"
    )
    await message.answer(text, reply_markup=get_main_menu(), parse_mode="Markdown")

async def about_school(message: types.Message):
    text = (
        "🏫 *Maktab haqida*\n\n"
        "29-sonli Bolalar musiqa va san’at maktabi o‘quvchilarga musiqa, rassomchilik va boshqa san’at yo‘nalishlarida ta’lim beradi.\n\n"
        "📅 Asos solingan yili: 1989\n"
        "👨‍💼 Direktor: G‘.X. Karimov\n"
        "📍 Manzil: Toshkent shahri, Yunusobod tumani"
    )
    await message.answer(text, parse_mode="Markdown")

async def teachers_info(message: types.Message):
    text = (
        "👨‍🏫 *O‘qituvchilar:*\n\n"
        "🎹 Abdurahmonova M. — Fortepiano\n"
        "🎻 Usmonov J. — Skripka\n"
        "🎨 Tursunova D. — Tasviriy san’at\n"
        "🥁 Xolmatov R. — Urmali cholg‘ular"
    )
    await message.answer(text, parse_mode="Markdown")

async def schedule_info(message: types.Message):
    text = (
        "📅 *Dars jadvali:*\n\n"
        "🕘 Darslar 14:00 dan 19:00 gacha.\n"
        "📆 Dushanbadan – Shanbagacha.\n"
        "Yakshanba – dam olish kuni."
    )
    await message.answer(text, parse_mode="Markdown")

async def news_info(message: types.Message):
    text = (
        "📰 *So‘nggi yangiliklar:*\n\n"
        "🎵 15-oktabr — “Yosh iste’dodlar” tanlovi o‘tkazildi.\n"
        "🏆 3 nafar o‘quvchi faxrli o‘rinlarni qo‘lga kiritdi."
    )
    await message.answer(text, parse_mode="Markdown")

async def admission_info(message: types.Message):
    text = (
        "🎓 *Qabul haqida:*\n\n"
        "🧒 Qabul 7 yoshdan 14 yoshgacha bo‘lgan bolalar uchun.\n"
        "📝 Hujjat topshirish muddati: 1-avgustgacha.\n"
        "📞 Ma’lumot uchun: +998 90 123 45 67"
    )
    await message.answer(text, parse_mode="Markdown")

async def gallery_info(message: types.Message):
    text = (
        "🖼️ *Fotogalereya:*\n\n"
        "📸 Tanlovlar, konsertlar va mashg‘ulotlardan suratlar tez orada joylanadi."
    )
    await message.answer(text, parse_mode="Markdown")

async def contact_info(message: types.Message):
    text = (
        "📞 *Aloqa:*\n\n"
        "📍 Manzil: Toshkent sh., Yunusobod tumani\n"
        "☎️ Telefon: +998 71 123 45 67\n"
        "📧 Email: info@bmsm.uz\n"
        "📱 Telegram: @Bmsm_29_official"
    )
    await message.answer(text, parse_mode="Markdown")

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    dp.message.register(cmd_start, Command("start"))
    dp.message.register(about_school, F.text == "🏫 Maktab haqida")
    dp.message.register(teachers_info, F.text == "👨‍🏫 O‘qituvchilar")
    dp.message.register(schedule_info, F.text == "📅 Dars jadvali")
    dp.message.register(news_info, F.text == "📰 Yangiliklar")
    dp.message.register(admission_info, F.text == "🎓 Qabul")
    dp.message.register(gallery_info, F.text == "🖼️ Fotogalereya")
    dp.message.register(contact_info, F.text == "📞 Aloqa")

    print("🤖 29BMSM InfoBot ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
