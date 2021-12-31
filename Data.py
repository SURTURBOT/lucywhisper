from pyrogram.types import InlineKeyboardButton


class Data:
    START = """
Hello , I am Whisper Bot and I can help you in sending secret messages in groups.
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("📬 Send a secret Message 📬", switch_inline_query="")],
        ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🔒 Send a Secret Message 🔒", switch_inline_query="")
        ],
        [
            InlineKeyboardButton("How to Use Me❔", url="https://teletype.in/@wetemp/wisper"),
        ],
        [InlineKeyboardButton("⚡Bot 🇽  Network⚡", url="https://t.me/BotxNetwork")],
        [InlineKeyboardButton("🛠️ Support Group 🛠️", url="https://t.me/BotxDesk")],
    ]

  
