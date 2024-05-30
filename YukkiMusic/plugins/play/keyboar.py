
from YukkiMusic import app
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, Message
from config import OWNER
from YukkiMusic.misc import SUDOERS

# تحديد لوحة المفاتيح
keyboard = ReplyKeyboardMarkup([['Button 1', 'Button 2']], resize_keyboard=True)

@app_client.on_message(filters.command('start') & ~filters.user(SUDOERS) & ~filters.user(OWNER))
async def start_command(client, message: Message):
    await message.reply_text('لوحة المفاتيح للمطور:', reply_markup=keyboard)
