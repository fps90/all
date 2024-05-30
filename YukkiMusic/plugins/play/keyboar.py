
from YukkiMusic import app
from strings.filters import command
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, Message
from config import OWNER

# تحديد لوحة المفاتيح
keyboard = ReplyKeyboardMarkup([['Button 1', 'Button 2']], resize_keyboard=True)

@app.on_message(command(["/start", "/admin"]) & filters.private & filters.user(OWNER))
async def start_or_help_command(client, message: Message):
    await message.reply_text('لوحة المفاتيح للمطور:', reply_markup=keyboard)
