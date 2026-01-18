import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

from settings import MONGO_URI, DB_NAME, COLLECTION_NAME
from app.services.car_service import get_all_available_cars


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    user_text = update.message.text
    print("📩 User:", user_text)

    cars = get_all_available_cars()

    if not cars:
        await update.message.reply_text("❌ No cars found in database.")
        return

    await update.message.reply_text(
        f"✅ DB connected. {len(cars)} cars available.\n"
        f"Next step: RAG search 🚀"
    )


def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()
