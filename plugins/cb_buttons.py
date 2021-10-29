from translation import Translation

import pyrogram

from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.help_text import help, start, about

@Client.on_callback_query()
async def button(bot, update):
    if update.data == "start":
        await update.message.edit_text(
            text=Translation.START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton("HELP", callback_data = "help"),
                        InlineKeyboardButton("ABOUT", callback_data = "about"),
                        InlineKeyboardButton("CLOSE", callback_data = "close")
                ]
            ]
        ))
    
    if update.data == "help":
        await update.message.edit_text(
            text=Translation.HELP_TEXT,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('BACK', callback_data = "start")
                ]
            ]
        ))
        
    if update.data == "about":
        await update.message.edit_text(
           text=Translation.ABOUT_TEXT,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('BACK', callback_data = "start")
                ]
            ]
        ))
        
    if update.data == "close":
        await update.message.delete()
        try:
            await update.message.reply_to_message.delete()
        except:
            pass
   
