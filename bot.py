import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# قراءة التوكن من المتغيرات
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("❌ BOT_TOKEN غير موجود في المتغيرات")

# الردود (عدّليها كما تشتي)
REPLIES = {
    "السلام عليكم": "وعليكم السلام ورحمة الله 🌸",
    "مرحبا": "أهلاً وسهلاً 🤍",
    "كيفك": "تمام الحمدلله 😊",
    "زواج": "💍 مرحباً بك، اكتب (تسجيل) للبدء",
    "تسجيل": "✍️ أرسل اسمك + عمرك + بلدك"
}

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    for key, reply in REPLIES.items():
        if key in text:
            await update.message.reply_text(reply)
            return

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
    print("🤖 البوت شغال...")
    app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
