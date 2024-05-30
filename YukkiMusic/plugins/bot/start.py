from YukkiMusic import app
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import SUPPORT_GROUP, SUPPORT_CHANNEL, OWNER_USER


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
                    InlineKeyboardButton("⦗ اوامر البوت ⦘", callback_data="user_command")
                ],[
                    InlineKeyboardButton("⦗ قناة السورس ⦘", url=SUPPORT_CHANNEL),
                    InlineKeyboardButton("⦗ قناة التحديثات ⦘", url=SUPPORT_GROUP),
                ],
                [
                    InlineKeyboardButton("⦗ مطور البوت ⦘", url=f"https://t.me/{OWNER_USER}"),
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
                    InlineKeyboardButton("⦗ مطور البوت ⦘", url=f"https://t.me/{OWNER_USER}"),
                ],
            ]
        ),
        disable_web_page_preview=True,
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
                    InlineKeyboardButton("-› اوامر التشغيل", callback_data="user_command"),
                ],
                [
                    InlineKeyboardButton("-› ࢪرجَۅعَ", callback_data="home_start"),
                    InlineKeyboardButton("التالي", callback_data="next"),
                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("next"))
async def next_set(_, query: CallbackQuery):
    await query.answer("التالي")
    await query.edit_message_text(
        "يرجى اختيار نوع الأوامر:",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⦗ اوامر الادمن ⦘", callback_data="admin_commands"),
                    InlineKeyboardButton("⦗ اوامر المطور ⦘", callback_data="developer_commands"),
                ],
                [
                    InlineKeyboardButton("-› ࢪرجَۅعَ", callback_data="command_list"),
                    InlineKeyboardButton("التالي", callback_data="user_command"),
                ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("user_command"))
async def guide_set(_, query: CallbackQuery):
    await query.answer("اوامر التشغيل")
    await query.edit_message_text(
        f"""طريقة التشغيل ، تابع في الاسفل ↓

1-› أولا ، أضفني الى مجموعتك
2-› بعد ذالك قم برفعي كمشرف واعطائي صلاحيات مثل باقي البشر.
3-› بعد ذالك اكتب `.تحديث` بيانات البوت
3-› اضف سيدي ومولاي في مجموعتك او اكتب `.انضم` لدعوة المساعد
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



@app.on_callback_query(filters.regex("admin_commands"))
async def guide_set(_, query: CallbackQuery):
    await query.answer("اوامر الادمن")
    await query.edit_message_text(
        f"""اوامر الادمن""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("-› ࢪجَۅعَ", callback_data="home_start")
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("developer_commands"))
async def guide_set(_, query: CallbackQuery):
    await query.answer("اوامر المطورين")
    await query.edit_message_text(
        f"""اوامر المطورين ↓

1-› أولا ، أضفني الى مجموعتك
2-› بعد ذالك قم برفعي كمشرف واعطائي صلاحيات مثل باقي البشر.
3-› بعد ذالك اكتب `.تحديث` بيانات البوت
3-› اضف سيدي ومولاي @{me_user.username} في مجموعتك او اكتب `.انضم` لدعوة المساعد
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

