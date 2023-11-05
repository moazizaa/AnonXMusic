
import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram import filters, Client
from AnonXMusic import app
from config import OWNER_ID

@app.on_message(filters.command(['✨بوت','بوت'], prefixes=""))
async def Italymusic(client: Client, message: Message):
    me = await client.get_me()
    bot_username = me.username
    bot_name = me.first_name
    italy = message.from_user.mention
    button = InlineKeyboardButton("اضف البوت الي مجموعتك🏅", url=f"https://t.me/{bot_username}?startgroup=true")
    keyboard = InlineKeyboardMarkup([[button]])
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if user_id == 1183747742:
             rank = "⋆ المبرمج مصطفي العزايري..🙂♥️"
        elif user_id == OWNER_ID:
             rank = "⋆ صاحب البوت ومطوري حبيبي..🙂♥️"
        elif member.status == 'creator':
             rank = "⋆ صاحب الجروب حبيب الكل..🙂♥️"
        elif member.status == 'administrator':
             rank = "⋆ مشرف الجروب الغالي..🙂♥️"
        else:
             rank = "لاسف انت عضو فقير🥺💔"
    except Exception as e:
        print(e)
        rank = "مش عرفنلو مله ده😒"
    async for photo in client.get_chat_photos("me", limit=1):

                    await message.reply_photo(photo.file_id,       caption=f"""⋆ اسمي الكيوت ⇇: {bot_name} 🥹♥️""", reply_markup=keyboard)


