import asyncio

from pyrogram import Client, filters
import config
from AnonXMusic.utils.decorators import AdminRightsCheck
from AnonXMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from config import BANNED_USERS

@app.on_message(filters.regex("^ميوزك$") & filters.group & ~BANNED_USERS) 
@AdminRightsCheck
async def khalid(client: Client, message: Message):
    user = message.from_user.mention
    await message.reply_text(f"""✧ <b> اهلين </b> {user} !\n✧ <b> اضغط الزر عشان تشوف اوامر دينا</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "الاوامر", callback_data=f"am"),
                ],
            ]
        ),
    )



@app.on_message(filters.regex("^دينا الاحصائيات$") & filters.user(6228635168))
async def ahtek(client: Client, message: Message):
    m_reply = await message.reply_text(f"✧ <b> اهلين مطوري ارحب</b>\n✧ <b> هذي احصائيات دينا يا روحي :</b>\n\n-› عدد المشتركين : 12478\n-› عدد المجموعات : 11346\n\n• تم زيادة 1204 مشترك ونقص 2103 مجموعة  في اخر 24 ساعة\n\n- عدد الطرد من بوتات اخرى : 843\n- طرد يدوي : 1302\n\n╼╾")
    await m_reply_text("")


@app.on_message(filters.command("","."))
def vgdg(client,message):
        message.reply_text(
            f"""✧ Welcome Baby,
ᴅᴇᴠᴇʟᴏᴘᴇʀ -› [『𝐖𝐇𝐈𝐒𝐊𝐄𝐘 𝐓𝐍𝐓 ⏎ 』♪](t.me/A_S_A_S_K)
ᴄʜᴀɴɴᴇʟ -› [𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂](t.me/Mlze1bot)""", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "تحديثات دينا 🍻", url=f"t.me/Mlze1bot")
                    ]
                ]
            ),
            disable_web_page_preview=True

        )




@app.on_message(filters.regex("^رابط الحذف$"))
async def delet(client: Client, message: Message):
    await message.reply_text(f"""✧ <b> اهلين ياحلو</b>\n✧ <b> هذي روابط حذف جميع مواقع التواصل بالتوفيق</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Telegram •", url=f"https://my.telegram.org/auth?to=delete"),
                    InlineKeyboardButton(
                        "• Instagram •", url=f"https://www.instagram.com/accounts/login/?next=/accounts/remove/request/permanent/"),
                ],[
                    InlineKeyboardButton(
                        "• Snapchat •", url=f"https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fdeleteaccount"),
                    InlineKeyboardButton(
                        "• Facebook •", url=f"https://www.faecbook.com/help/deleteaccount"),
                ],[
                    InlineKeyboardButton(
                        "• Twitter •", url=f"https://mobile.twitter.com/settings/deactivate"),

                ],
            ]
        ),
    )


@app.on_message(filters.command("دينا نادي المطور", [".", ""]) & filters.group)
async def kstr(client: Client, message: Message):
       chat = message.chat.id
       gti = message.chat.title
       link = await app.export_chat_invite_link(chat)
       usr = await client.get_users(message.from_user.id)
       chatusername = f"@{message.chat.username}"
       user_id = message.from_user.id
       user_ab = message.from_user.username
       user_name = message.from_user.first_name
       buttons = [[InlineKeyboardButton(gti, url=f"{link}")]]
       reply_markup = InlineKeyboardMarkup(buttons)
       
       await app.send_message(-1001936852140, f"- قام {message.from_user.mention}\n- بمناداتك عزيزي المطور\n- ايديه {user_id}\n- يوزره @{user_ab}\n- ايدي القروب {message.chat.id}\n- يوزر القروب {chatusername}",
       reply_markup=reply_markup,
       )
       await message.reply_text(
        f"""✧ <b> ابشر ياعيوني ارسلت للمطور بيخش القروب ويشوف مشكلتك بأقرب وقت </b>\n\n✧ <b> تابع قناة البوت عشات تشوف التحديثات</b> -› [• 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 •](t.me/Mlze1bot)""", disable_web_page_preview=True     
    )


REPLY_MESSAGE = "✧ <b> اهلين ياحلو تحكم من الازرار اسفل </b>"




REPLY_MESSAGE_BUTTONS = [

         [

             ("كيفية استخدام دينا"),                   

             ("اوامر دينا")




          ],
          [
             ("المسلسلات")
          ], 
          [

             ("المطور"),

             ("السورس")

          ],

          [

             ("اخفاء الازرار")

          ]

]




  

@app.on_message(filters.regex("^داااااااينا$") & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        photo=config.DRTYU_VENUE,
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اخفاء الازرار") & filters.group)
async def down(client, message):
          m = await message.reply("✧ <u> ابشر تم اخفاء الازرار بنجاح</u>\n✧ <b> لو تبي تطلعها مرة ثانية اكتب دينا</b>", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.group & filters.command(["كيفية استخدام دينا"],""))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""✧ <b> هلا والله ياعيني عشان تفعل بوت دينا اتبع الخطوات الي بالاسفل </b>
1 • ارفعه مشرف بكل الصلاحيات 
2 • لو تبي تشوف الاوامر اكتب [ م الاوامر ] ولو تبي تشغل على طول اكتب دينا شغلي + اسم المقطع الصوتي
• مثال : دينا شغلي قالوا عليكي
- لو واجهت مشكله كلم مطور البوت ~ @A_S_A_S_K""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "𝗔𝗦𝗔𝗔𝗤", user_id=6218149232),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/smauabot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.group & filters.command(["السورس"],""))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""✧ <b> اهلين فيك بسورس دينا ياحلو
• لو تبي تنصب مثل هالبوت تواصل مع مطور السورس
• عندك استفسار او اقتراح بخصوص البوت تواصل مع مطور البوت</b>
مطور السورس -› [𝗔𝗦𝗔𝗔𝗤](t.me/A_S_A_S_K)
قناة السورس -› [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂](t.me/Mlze1bot)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "تحديثات دينا 🍻", url=f"https://t.me/Mlze1bot"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/smauabot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )




REPLY_MESSAGE = "**صلي علي اشرف خلق الله 🥹✨**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("السورس"),
                ("مطور"),
    ],
    [
        ("صور شباب"),
        ("صور بنات")
                ("صوره"),
    ],
    [
        ("استوري")
                ("غنيلي")
                ("متحركه")
    ],
    [
        ("النقشبندي"),
        ("قران")
                ("اذكار"),
    ],
    [
        ("افلام")
    ],
    [
            ("خيروك"),
        ("اقتباسات"),
               ("انصحني")
                           ("احكام")
    ],
    [
            ("هيدرات")
        ("انمي")
    ],
    [
        ("تويت"),
        ("صراحه")
            ("نكته"),
        ("كتبات")
    ],
    [
        ("الالعاب")
                ("احسب"),
        ("ابراج")
    ],
   
    [
        ("اخفاء الازرار . 🕷")
    ]
]
 
@app.on_message(filters.private("^/start"))
async def com(_, message: Message):             
        text = REPLY_MESSAGEE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONSS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("^اخفاء الازرار . 🕷$"))
async def down(client, message):
          m = await message.reply(" **- تم اخفاء الازرار بنجاح . 🐰\n\n- لاظهار كيب الارشادات /ARN   \n. 🕷**\n\n- لاظهار كيب الاعضاء والتسليه  /AFYN  \n. 🕷**", reply_markup= ReplyKeyboardRemove(selective=True))



@app.on_message(filters.regex("يـوتيوب. 📽"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/9082f22163efb73912bab.jpg",
        caption=f"""**يتم استخدام هذا الامر لعرض تحميل من اليوتيوب**\n**استخدم الامر بهذا الشكل** `تنزيل` ** او ** `يوتيوب` ** كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("᥉᥆υᖇᥴᥱ ᥲ️ᖇꪀ᥆ρ", url=f"https://t.me/N_G_12"),
            ]
         ]
     )
  )