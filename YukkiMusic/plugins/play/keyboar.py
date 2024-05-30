from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import OWNER
from YukkiMusic import app

# تعريف لوحة المفاتيح
keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("زر 1"), KeyboardButton("زر 2")],
        [KeyboardButton("زر 3"), KeyboardButton("زر 4")]
    ],
    resize_keyboard=True
)

# تعريف الأمر لعرض لوحة المفاتيح
@app.on_message(filters.command("start"))
async def start_command(client, message):
    if message.from_user.id == OWNER:  # التحقق مما إذا كان المستخدم المطلوب هو المالك
        await message.reply_text("مرحبًا بك! اختر أحد الأزرار:", reply_markup=keyboard)
   

@app.on_message(filters.text & ~filters.command("start"))
async def handle_message(client, message):
    if message.from_user.id == OWNER:  # التحقق مما إذا كان المستخدم المطلوب هو المالك
