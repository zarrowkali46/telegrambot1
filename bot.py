import json
import random
import nest_asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Fix asyncio event loop for Windows
nest_asyncio.apply()

# Load videos.json
with open("videos.json", "r") as f:
    data = json.load(f)
videos = data["videos"]

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎬 Random Video", callback_data="random")],
        [InlineKeyboardButton("📃 Full List", callback_data="list")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Choose an option:", reply_markup=reply_markup)

# Button handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "random":
        video = random.choice(videos)
        await query.message.reply_video(video["url"], caption=video["title"])
    elif query.data == "list":
        msg = "📃 *All Videos:*\n\n"
        for v in videos:
            msg += f"• [{v['title']}]({v['url']})\n"
        await query.message.reply_text(msg, parse_mode="Markdown")

# Main
if __name__ == "__main__":
    bot_token = "8463311783:AAFopjKN-6gEPH7WqIZIKvELS16cuG17UQY"

    app = ApplicationBuilder().token(bot_token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()  # <-- no asyncio.run()
