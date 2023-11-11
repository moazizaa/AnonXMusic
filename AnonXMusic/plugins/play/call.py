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

@app.on_message(filters.voice_chat_started)
async def stcall(client: Client, message: Message): 
      Startt = "تم بدأ محادثه صوتيه"
      await message.reply_text(Startt)

@app.on_message(filters.voice_chat_ended)
async def encall(client: Client, message: Message): 
      Enddd = "تم إغلاق المحادثه الصوتيه"
      await message.reply_text(Enddd)

@app.on_message(filters.voice_chat_members_invited)
async def zoharyy(client: Client, message: Message): 
           text = f"- قام {message.from_user.mention}\n - بدعوة : "
           x = 0
           for user in message.voice_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} ")
           except:
             pass
