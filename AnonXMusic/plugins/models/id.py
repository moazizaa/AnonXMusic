from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types
from AnonXMusic import app
import random

iddof = []
@app.on_message(
    filters.command(["قفل الملصقات","تعطيل الملصقات"],"")
 
   
)
async def block_stickers(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in iddof:
            return await message.reply_text(f"يا {message.from_user.mention} الملصقات مقفله من قبل")
        iddof.append(message.chat.id)
        return await message.reply_text(f"تم قفل الملصقات \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")
    
@app.on_message(
    filters.command(["فتح الملصقات","تفعيل الملصقات"],"")
 
   
)
async def block_stickers(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in ["creator", ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in iddof:
            return await message.reply_text(f"يا {message.from_user.mention} الملصقات مقفله من قبل")
        iddof.append(message.chat.id)
        return await message.reply_text(f"تم قفل الملصقات \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")
    




@app.on_message(filters.command(["ايدي","الايدي","ا"], ""))
async def iddd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"""☠️ ¦𝙽𝙰𝙼𝙴 :{message.from_user.mention}\n🥰 ¦𝚄𝚂𝙴𝚁 :@{message.from_user.username}\n😍 ¦𝙸𝙳 :`{message.from_user.id}`\n💕 ¦𝙱𝙸𝙾 :{usr.bio}\n❤ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n😎 ¦𝙸𝙳.𝙲𝙷𝙰𝚃 :`{message.chat.id}`""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )



iddof = []
@app.on_message(filters.command(["قفل جمالي","تعطيل جمالي"], ""))
async def lllock(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in ["creator", "administrator"]:
      if message.chat.id in iddof:
        return await message.reply_text("جمالي معطل من قبل✅")
      iddof.append(message.chat.id)
      return await message.reply_text(" تم تعطيل جمالي بنجاح✅🔒")
   else:
      return await message.reply_text("لازم تكون ادمن يبني علشان اسمع كلامك")

@app.on_message(filters.command(["فتح جمالي","تفعيل جمالي"], ""))
async def idljjopen(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in ["creator", "administrator"]:
      if not message.chat.id in iddof:
        return await message.reply_text("جمالي مفعل من قبل✅")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم فتح جمالي بنجاح ✅🔓")
   else:
      return await message.reply_text("لازم تكون ادمن يبني علشان اسمع كلامك")




@app.on_message(filters.command(["جمالي"], ""))
async def idjjdd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = ["0","10", "15","20", "25","30","35", "40","45", "50","55", "60"," 66", "70","77", "80","85", "90","99", "100","1000" ]
    ik = random.choice(i)
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"نسبه جمالك يا مز انت \n│ \n└ʙʏ: {ik} %😂❤️", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
       

