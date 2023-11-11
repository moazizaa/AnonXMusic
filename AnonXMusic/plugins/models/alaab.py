import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from typing import Union
from AnonXMusic import app
import re
import sys

GAME_MESSAGE = "──── 「 سورس العزايزي 」────\n\n★¦ مرحبا بك عزيزي:\n★¦في قسم العاب cr\n\n──── 「 سورس العزايزي 」────"
GAME_BUTTONS = [
    [ 
        InlineKeyboardButton ('العاب 3D ', callback_data= 'GAME1'),
        InlineKeyboardButton ('cr cr', callback_data= 'GAME2'),
        ],[
        InlineKeyboardButton ('──── 「 سورس العزايزي 」────', url =f"https://t.me/BANDA1M")              
                 ],[
                InlineKeyboardButton(
                        "◁", callback_data="close"),
               ],
          ]
@app.on_message(
    filters.command(["الالعاب","العاب"],"")
)
async def zohary(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/86eb759b32ead328e198a.jpg",
        caption= GAME_MESSAGE,
        reply_markup=InlineKeyboardMarkup(GAME_BUTTONS)
    ) 

@app.on_callback_query()
async def callback_query(client, CallbackQuery):
          if CallbackQuery.data == "GAME1":
            
             GAME1_MESSAGE = "──── 「 سورس العزايزي 」────\n\nمرحبا بك في قسم العاب star 3D\n\n──── 「 سورس العزايزي 」────"

             GAME1_BUTTONS = [
                 [
                    InlineKeyboardButton(
                        "°فلابي بيرد°", url=f"http://t.me/awesomebot?game=FlappyBird"), 
                    InlineKeyboardButton (
                        "°تبديل النجوم°", url=f"http://t.me/gamee?game=Switchy"),
                ],[
                    InlineKeyboardButton (
                        "°موتسيكلات°" , url=f"http://t.me/gamee?game=motofx"),
                    InlineKeyboardButton (
                        "°اطلاق النار°" , url=f"http://t.me/gamee?game=NeonBlaster"),
                ],[
                    InlineKeyboardButton (
                        "°كرة القدم°" , url=f"http://t.me/gamee?game=Footballstar"),
                    InlineKeyboardButton (
                        "°تجميع الالوان°" , url=f"http://t.me/awesomebot?game=Hextris"),
                ],[        
                    InlineKeyboardButton (
                        "°المجوهرات°" , url=f"http://t.me/gamee?game=DiamondRows"),
                    InlineKeyboardButton (
                        "°ركل الكرة°" , url=f"http://t.me/gamee?game=KeepitUP"),
                ],[        
                    InlineKeyboardButton (
                        "°بطولة السحق°" , url=f"http://t.me/gamee?game=SmashRoyale"),
                    InlineKeyboardButton (
                        "°2048°" , url=f"http://t.me/awesomebot?game=g2048"),
                ],[        
                    InlineKeyboardButton (
                        "°كرة السلة°" , url=f"http://t.me/gamee?game=BasketBoy"),
                    InlineKeyboardButton (
                        "°القط المجنون°" , url=f"http://t.me/gamee?game=CrazyCat"),
                ],[
                    InlineKeyboardButton (
                        "◁" , callback_data= 'GAME')
                  ],
             ]
             await CallbackQuery.edit_message_text( 
                 GAME1_MESSAGE ,
                 reply_markup = InlineKeyboardMarkup(GAME1_BUTTONS) 
              )
          elif CallbackQuery.data == "GAME":
               
               RETURN_GAME = "──── 「 سورس العزايزي 」────\n\n★¦مرحبا بك في قسم العاب cr\n★¦اختار ما تشاء من الالعاب مسليه وستمتع بها\n\n──── 「 سورس العزايزي 」────" 

               RETURN_BUTTON = [
                    [ 
                      InlineKeyboardButton ('★¦العاب 3D', callback_data= 'GAME1'),
                      InlineKeyboardButton ('★¦العاب cr', callback_data= 'GAME2')
                      ],[
        InlineKeyboardButton ('「 سورس العزايزي 」', url =f"https://t.me/BANDA1M")              
                 ],[
                InlineKeyboardButton(
                        "◁", callback_data="close"),
               ],
          ]
     
               await CallbackQuery.edit_message_text( 
                 RETURN_GAME ,
                 reply_markup = InlineKeyboardMarkup(RETURN_BUTTON) 
                    )
          elif CallbackQuery.data == "GAME2":
               
               SOURCE_GAME = "──── 「 سورس العزايزي 」────\n\n★¦العاب cr\n★¦كت\n★¦تويت\n★¦اسال\n★¦اصراحه\n\n──── 「 سورس العزايزي 」────." 

               SORGAM_BUTTON = [
                    [ 
                      InlineKeyboardButton ('──── 「 سورس العزايزي 」────', url =f"https://t.me/BANDA1M")
                      ],[
                         InlineKeyboardButton ('◁', callback_data= 'GAME')
                    ]
               ]    
               await CallbackQuery.edit_message_text( 
                 SOURCE_GAME ,
                 reply_markup = InlineKeyboardMarkup(SORGAM_BUTTON) 
                    )
    
