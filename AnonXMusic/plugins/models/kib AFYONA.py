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
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
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

