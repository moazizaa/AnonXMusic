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
        ("فيلمك. 🎥")
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
        ("الالعاب. 🐰")
    ],
    [
        ("نكته"),
        ("كتبات")
    ],
    [
        ("اذكار. 💎")
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
       ("انصحني. 🥲")
        
    ],
    [
        ("اخفاء الازرار . 🕷")
    ]
]

@app.on_message(filters.regex("^/AFYN"))
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
