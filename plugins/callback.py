import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from .commands import start
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
OWNER_ID = os.environ.get("OWNER_ID")


@Client.on_callback_query(filters.regex('^help$'))
async def help_cb(c, m):
    await m.answer()

    # help text
    help_text = """**Kamu butuh bantuan?? 😎**

Kirimkan saja saya file, saya akan menyimpan file dan memberi Anda tautan yang dapat dibagikan


**Anda juga dapat menggunakan saya di Channel 😉**

Jadikan saya admin di Channel Anda dengan izin edit. Itu cukup sekarang lanjutkan mengunggah file di Channel anda, Dan saya akan mengedit semua postingan dan menambahkan tautan yang dapat dibagikan lewat tombol"""
    # creating buttons
    buttons = [
        [
            InlineKeyboardButton('🎛 BERANDA 🎛', callback_data='home'),
            InlineKeyboardButton('📖 TENTANG 📖', callback_data='about')
        ],
        [
            InlineKeyboardButton('⛔ TUTUP ⛔', callback_data='close')
        ]
    ]

    # editing as help message
    await m.message.edit(
        text=help_text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@Client.on_callback_query(filters.regex('^close$'))
async def close_cb(c, m):
    await m.message.delete()
    await m.message.reply_to_message.delete()


@Client.on_callback_query(filters.regex('^about$'))
async def about_cb(c, m):
    await m.answer()
    owner = await c.get_users(int(OWNER_ID))
    bot = await c.get_me()

    # about text
    about_text = f"""--**DETAIL SAYA:**--

🤖    :  {bot.mention(style='md')} 
💬   : [CHANNEL](https://t.me/tergantungmoodku)
📄   : [SUPORT](https://t.me/kenkanasw)
"""

    # creating buttons
    buttons = [
        [
            InlineKeyboardButton('🎛 BERANDA 🎛', callback_data='home'),
            InlineKeyboardButton('📝BANTUAN 📝', callback_data='help')
        ],
        [
            InlineKeyboardButton('⛔ TUTUP ⛔', callback_data='close')
        ]
    ]

    # editing message
    await m.message.edit(
        text=about_text,
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex('^home$'))
async def home_cb(c, m):
    await m.answer()
    await start(c, m, cb=True)
