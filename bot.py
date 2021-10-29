from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "2003563595:AAFeAMyuDBxPeNlqYelw7H1c_bthh_balLA")

API_ID = int(os.environ.get("API_ID", 5658727))

API_HASH = os.environ.get("API_HASH", "42e0eda86eaf00f747c68665f4f63322")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "pdisk",
        bot_token=TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
    )
    app.run()
