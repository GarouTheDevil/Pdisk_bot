import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import pyrogram
import os
import sqlite3
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message

from translation import Translation


@Client.on_message(pyrogram.filters.command(["help"]))
async def help(bot, update):
            await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton("BACK", callback_data = "start")
                ]
            ]
        )
    )       

@Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
            await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton("HELP", callback_data = "help")
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )

@Client.on_message(pyrogram.filters.command(["about"]))
async def about(bot, update):
            await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton("BACK", callback_data = "start")
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )
