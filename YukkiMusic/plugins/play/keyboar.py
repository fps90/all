from YukkiMusic import app
from strings.filters import command
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, Message
from config import OWNER

# تحديد لوحة المفاتيح
keyboard = ReplyKeyboardMarkup(
    [
        [('⦗ فتح الكيبورد ⦘')],
        [('⦗ اعادة تشغيل ⦘'), ('⦗ تحديث السورس ⦘')],
        [('حذف الاعضاء الفيك'), ('حذف الجروبات الفيك')],
        [('الاصدار'), ('تحديث السورس'), ('سرعه السيرفر')],
        [('اذاعه للمستخدمين'), ('اذاعه للجروبات')],
        [('اذاعه للمطورين'), ('اذاعه للاساسيين'), ('اذاعه قنوات')],
        [('اذاعه للكل'), ('توجيه للكل')],
        [('توجيه للمستخدمين'), ('توجيه للجروبات'), ('توجيه للقنوات')],
        [('توجيه للاساسيين'), ('توجيه للمطورين')],
        [('حذف الكيبورد ⚒️')]
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)

@app.on_message(command(["⦗ فتح الكيبورد ⦘", "/start"]) & filters.private & filters.user(OWNER))
async def start_or_help_command(client, message: Message):
    await message.reply_text('اهلأ بك عزيزي ⦗ المطور الاساسي ⦘ \n – – – – – – \n⦗ يمكنك التحكم عن طريق الأزرار أدناه ⦘', reply_markup=keyboard)
