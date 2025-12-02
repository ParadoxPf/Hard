import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import *
from database import add_user
from helper import get_metadata, save_thumbnail
from shortener import shorten_link

app = Client("merge_paradox_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Force-subscribe check
async def check_fs(message):
    if FS_CHANNEL_ID:
        try:
            member = await app.get_chat_member(FS_CHANNEL_ID, message.from_user.id)
            if member.status in ["kicked"]:
                await message.reply_text(f"Please join {FS_CHANNEL_ID} first.")
                return False
        except:
            await message.reply_text(f"Please join {FS_CHANNEL_ID} first.")
            return False
    return True

@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    if not await check_fs(message):
        return
    await add_user(message.from_user.id)
    text = f"👋 Hello {message.from_user.first_name}!\n\nI am Merge_Paradox_Bot.\nSend me any file to rename, extract metadata, and shorten links."
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Help", callback_data="help")],
        [InlineKeyboardButton("Updates", url="https://t.me/YourChannel")]
    ])
    await message.reply_text(text, reply_markup=buttons, disable_web_page_preview=True)

@app.on_message(filters.document | filters.video | filters.audio)
async def rename_file(client, message):
    if not await check_fs(message):
        return

    file_path = await message.download(file_name=os.path.join("downloads", message.document.file_name))
    metadata = get_metadata(file_path)
    short_link = shorten_link(f"file://{os.path.abspath(file_path)}")

    await message.reply_text(f"✅ File renamed & ready!\nMetadata: {metadata}\nShort Link: {short_link}")

@app.on_message(filters.command("admin") & filters.user(ADMINS))
async def admin_panel(client, message):
    await message.reply_text("✅ Admin Access Granted.\nYou can manage users and view stats.")

app.run()
