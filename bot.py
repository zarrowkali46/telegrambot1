import os
import json
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import nest_asyncio

nest_asyncio.apply()

# Load bot token from Railway environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Load videos from videos.json
with open("videos.json", "r", encoding="utf-8") as f:
    videos = json.load(f)

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 হ্যালো! আমি র‍্যান্ডম ভিডিও বট। /video লিখে ভিডিও নাও!")

# Command: /video
async def send_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = random.choice(videos)
    await update.message.reply_text(f"🎬 {video}")

# Bot setup
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("video", send_video))

print("✅ Bot is running...")
app.run_polling()
