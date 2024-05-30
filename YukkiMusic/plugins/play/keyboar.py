
from YukkiMusic import app
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup
from config import OWNER

# تحديد لوحة المفاتيح
keyboard = ReplyKeyboardMarkup([['Button 1', 'Button 2']], resize_keyboard=True)

@app.on_message(filters.command('admin') & filters.user(OWNER))
def start_(client, message):
    message.reply_text('اهلا بك عزيزي ⦗ المطور الاساسي ⦘ \n – – – – – –', reply_markup=keyboard)
