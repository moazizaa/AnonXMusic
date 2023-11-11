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





@app.on_message(filters.regex("اخفاء الازرار") & filters.group)
async def down(client, message):
          m = await message.reply("✧ <u> ابشر تم اخفاء الازرار بنجاح</u>\n✧ <b> لو تبي تطلعها مرة ثانية اكتب /free</b>", reply_markup= ReplyKeyboardRemove(selective=True))




REPLY_MESSAGEE = "صلي علي النبي وتبسم..♥️"

REPLY_MESSAGE_BUTTONSS = [

    [
        ("السورس"),
                ("مطور"),
    ],
    [
        ("صور شباب"),
                ("صور بنات"),
                ("صوره"),
    ],
    [
        ("استوري"),
                ("غنيلي"),
                ("متحركه"),
    ],
    [
        ("النقشبندي"),
        ("قران"),
                ("اذكار"),
    ],
    [
        ("افلام"),
                ("اغاني"),
                        ("العاب"),
    ],
    [
            ("خيروك"),
        ("اقتباس"),
               ("انصحني"),
                           ("احكام"),
    ],
    [
            ("رابط الحذف"),
        ("انمي"),
    ],
    [
        ("تويت"),
        ("صراحه"),
            ("نكته"),
        ("كتبات"),
    ],
    [
                ("احسب"),
        ("ابراج"),
    ],
   
    [
        ("اخفاء الازرار"),
    ]
]

  

@app.on_message(filters.regex("^/free"))
async def com(_, message: Message):             
        text = REPLY_MESSAGEE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONSS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

