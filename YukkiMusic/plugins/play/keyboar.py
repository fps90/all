
from YukkiMusic import app
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup
from config import OWNER

# تحديد لوحة المفاتيح
keyboard = ReplyKeyboardMarkup([['Button 1', 'Button 2']], resize_keyboard=True)

@app.on_message(filters.command('start') & filters.user(OWNER))
def start_command(client, message):
    message.reply_text('لوحة المفاتيح للمطور:', reply_markup=keyboard)

# دالة لاختبار لوحة المفاتيح
@app.on_message(filters.command('start') & filters.user(OWNER))
def test_command(client, message):
    message.reply_text('قم بتجربة لوحة المفاتيح:', reply_markup=keyboard)
