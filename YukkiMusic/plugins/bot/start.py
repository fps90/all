from YukkiMusic import app
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import SUPPORT_GROUP, SUPPORT_CHANNEL, OWNER_ID


# دالة وهمية add_served_user لتجنب الخطأ
async def add_served_user(user_id: int):
    # يمكنك إضافة منطق تخزين المستخدم هنا إذا لزم الأمر
    pass

@app.on_message(
    filters.command(["start", "str"]) & filters.private
)
async def start_(c: Client, message: Message):
    user_id = message.from_user.id
    await add_served_user(user_id)
    await message.reply_text(
        f"""ههݪاެ حبيب {message.from_user.mention()} ❤️‍🔥\n
اެناެ بَۅت بَمميࢪ࣪اެتَ متَعدَدةَ ݪتشغِيݪ اެݪاغاެنِي فَي اެݪمَجمَۅعاتَ 🥇.

-› MᥲᎥꪀƚᥲᎥᏁᥱძ ხy -› [S᥆ᥙrᥴᥱ Frᥱᥱძ᥆ꪔ](http://t.me/xl444)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⦗ اوامر البوت ⦘", callback_data="command_list")
                ],[
                    InlineKeyboardButton("⦗ قناة السورس ⦘", url=SUPPORT_CHANNEL),
                    InlineKeyboardButton("⦗ قناة التحديثات ⦘", url=SUPPORT_GROUP),
                ],
                [
                    InlineKeyboardButton("⦗ مطور البوت ⦘", user_id=OWNER_ID),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@app.on_callback_query(filters.regex("home_start"))
async def start_set(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""ههݪاެ حبيب [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) ❤️‍🔥\n
اެناެ بَۅت بَمميࢪ࣪اެتَ متَعدَدةَ ݪتشغِيݪ اެݪاغاެنِي فَي اެݪمَجمَۅعاتَ 🥇.

-› MᥲᎥꪀƚᥲᎥᏁᥱძ ხy -› [S᥆ᥙrᥴᥱ Frᥱᥱძ᥆ꪔ](http://t.me/xl444)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⦗ اوامر البوت ⦘", callback_data="command_list")
                ],
                [
                    InlineKeyboardButton("⦗ قناة السورس ⦘", url=SUPPORT_CHANNEL),
                    InlineKeyboardButton("⦗ قناة التحديثات ⦘", url=SUPPORT_GROUP),
                ],
                [
                    InlineKeyboardButton("⦗ مطور البوت ⦘", user_id=OWNER_ID),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@app.on_callback_query(filters.regex("user_guide"))
async def guide_set(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""طريقة التشغيل ، تابع في الاسفل ↓

1-› أولا ، أضفني الى مجموعتك
2-› بعد ذالك قم برفعي كمشرف واعطائي صلاحيات مثل باقي البشر.
3-› بعد ذالك اكتب `.تحديث` بيانات البوت
3-› اضف سيدي ومولاي  في مجموعتك او اكتب `.انضم` لدعوة المساعد
4-› اذ لم تستطيع اضافة المساعد او واجهت مشاكل تحدث مع رئيس الوزراء  .

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("-› ࢪجَۅعَ", callback_data="home_start")
                ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("command_list"))
async def commands_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("👍🏻قائمة الاوامر")
    await query.edit_message_text(
        f"""- تابع الازرار في الاسفل ↓

يمديك تشوف كل اوامر البوت عن طريق زر اوامر البوت""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("-› اوامر البوت", callback_data="user_command"),
                ],
                [
                    InlineKeyboardButton("-› ࢪجَۅعَ", callback_data="home_start")
                ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("user_command"))
async def user_set(_, query: CallbackQuery):
    await query.answer("👍🏻اوامر التشغيل")
    await query.edit_message_text(
        f"""- تابع الاوامر في الاسفل ↓

-› .شغل - بالرد على ملف صوتي او اسم أغنية
-› .اصعد - لصعود حساب المساعد في المكالمة
-› .انزل - لنزول المساعد من المكالمة
-› .تخطي - لتخطي اغنية في التشغيل
-› .كافي - لايقاف تشغيل جميع الاغاني
-› .اضبط - لضبط صوت حساب المساعد
-› .فيديو - بالرد على مقطع فيديو او اسم فيديو
-› .الانتضار - لرؤية قائمة الانتضار التشغيل
-› .ابحثلي - لبحث عن فيديو من اليوتيوب
-› .بحث - لتحميل اغنية من اليوتيوب
-› .كتم - لكتم صوت المساعد 
-› .بنك - لإضهار بنك البوت
-› .انضم - لدعوة حساب المساعد

. شكراً لقرائتك الاوامر - أتمنى لك يوماً تعيساً 🦴 """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("-› ࢪجَۅعَ", callback_data="command_list")]]
        ),
    )
