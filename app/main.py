import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

from app.config.settings import MONGO_URI, DB_NAME, COLLECTION_NAME ,TELEGRAM_TOKEN
from app.filters.parser import parse_filters
from app.services.car_service import search_cars

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    user_text = update.message.text
    print("📩 User:", user_text)

    #  Parse filters
    filters_extracted = parse_filters(user_text)
    print(" Filters:", filters_extracted)

    #  Retrieve from MongoDB
    cars = search_cars(filters_extracted)

    if not cars:
        await update.message.reply_text("❌ No matching cars found.")
        return

    # 3️⃣ Send results
    for car in cars:
        await update.message.reply_text(
            f"🚗 {car['brand'].title()} {car['model'].title()} {car['variant']}\n"
            f"📅 Year: {car['year']}\n"
            f"🎨 Color: {car['color']}\n"
            f"⛽ Fuel: {car['fuel']}\n"
            f"🛣️ KM: {car['km']}\n"
            f"💰 Price: ₹{car['price']:,}"
        )

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()
