
from YukkiMusic import app
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, Message
from config import OWNER

# تحديد لوحة المفاتيح
keyboard = ReplyKeyboardMarkup([['Button 1', 'Button 2']], resize_keyboard=True)

@app.on_message(filters.command(["start", "help"]) & filters.private & filters.user(OWNER))
async def start_(c: Client, message: Message):
    await message.reply_text('لوحة المفاتيح للمطور:', reply_markup=keyboard)
