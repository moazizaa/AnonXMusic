from pyrogram import filters

from AnonXMusic import YouTube, app
from AnonXMusic.utils.channelplay import get_channeplayCB
from AnonXMusic.utils.decorators.language import languageCB
from AnonXMusic.utils.stream.stream import stream
from pyrogram import filters
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus, ChatType
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.utils.database import set_cmode
from AnonXMusic.utils.decorators.admins import AdminActual
import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram import filters, Client
from AnonXMusic import app
from config import BANNED_USERS


REPLY_MESSAGE = "**صلي علي اشرف خلق الله 🥹✨**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("السورس"),
    ],
    [
        ("افتار شباب"),
        ("افتار بنات")
    ],
    [
        ("استوريهات. 🥹")
    ],
    [
        ("النقشبندي"),
        ("قران")
    ],
    [
        ("فيلم")
    ],
    [
        ("اقتباسات"),
        ("هيدرات")
    ],
    [
        ("غنيلي. 🎙")
    ],
    [
        ("صوره"),
        ("انميي")
    ],
    [
        ("متحركه. 🎬")
    ],
    [
        ("تويت"),
        ("صراحه")
    ],
    [
        ("الالعاب")
    ],
    [
        ("كتابات")
    ],
    [
        ("اذكار")
    ],
    [
        ("حساب العمر"),
        ("ابراج")
    ],
    [
        ("يـوتيوب. 📽")
        
    ],
    [
        ("لو خيروك"),
        ("انصحني")
    ],
    [
        ("بوت حذف")
        
    ],
    [
        ("حساب العمر"),
        ("ابراج")
    ],
    [
       ("انصحني")
        
    ],
    [
        ("اخفاء الازرار")
    ]
]

  resize_keyboard=True
)

@app.on_message(filters.command(["/start"], ""))
async def for_users (app,m):
   if check(m.from_user.id):
     kep = ReplyKeyboardMarkup([["《صنع بوت》", "《حذف بوت》"], ["البوتات المصنوعه"], ["تعطيل المجاني", "تفعيل المجاني"], ["تعطيل التواصل", "تفعيل التواصل"], ["السورس"], ["الغاء"]], resize_keyboard=True)
     return await m.reply_photo(
        photo=f"https://telegra.ph/file/2514530559cc173845e3f.jpg",
        caption=f"""[ ●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━● •](https://t.me/UIU_II)\n\n**اهـلا يـنـجـم.؟ **\n**مـرحبآ بـك انــا بــوت اقـوم بــتـشـغـيـل الاغــانــي فـي الـمـڪـالـمـه الـصـوتـية .🤔❤**\n**يمكنني التشغيل بصوت رائع وبدون اي مشاكل او تقطيع في الاغنيه**\n**اضفني الى مجموعتك وارفعني رول بشڪل مع ڪامل الصلاحيات صحيح**\n**لمعرفة استخدامي بشڪل صحيح اضغط علي زر الاوامر. 🤔💕**\n
اضغط(/sezar)لاظهار كيب المطور ✨
[ ●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━● •](https://t.me/UIU_II)""", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مطور السورس. ⚡", url=f"https://t.me/c_a_s_e_r_h"),
            ],[
                    InlineKeyboardButton(
                        "قناة السورس⚡", url=f"https://t.me/UIU_II"),
            ],[
                    InlineKeyboardButton(
                        " اضغط هنا لاضافتي الي مجموعتك🤖", url=f"https://t.me/SILA_11bot?startgroup=true"),
            ], 
            ]
        ),
    )
    

@app.on_message(filters.regex("اخفاء الازرار"))
async def down(client, message):
          m = await message.reply(" **- تم اخفاء الازرار بنجاح **\n\n- لاظهار كيب الاعضاء والتسليه  /start  \n. **", reply_markup= ReplyKeyboardRemove(selective=True))



@app.on_message(filters.regex("يـوتيوب. 📽"))
async def reply_to_HEY(client, message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/520cb8756d31bb3184de2.jpg",
        caption=f"""**يتم استخدام هذا الامر لعرض تحميل من اليوتيوب**\n**استخدم الامر بهذا الشكل** `تنزيل` ** او ** `يوتيوب` ** كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ՏΌႮᎡᏟᎬ ͲΝͲ", url=f"https://t.me/TNT_source"),
            ]
         ]
     )
  )
