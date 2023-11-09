import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(filters.command(["السورس", "ياسورس"], ""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/19d68d531fd2f6f96e368.jpg",
caption=f"""⋆ ʷᵉˡᶜᵒᵐᵉ ᵗᵒ ᵗʰᵉ ᵃᶻᵃᶻʸ ˢᵒᵘʳᶜᵉ ⤈⤌""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "قناة السورس", url=f"https://t.me/BANDA1M"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "مبرمج السورس", url=f"https://t.me/php_7"),
                ],
            ]
        ),
    )
