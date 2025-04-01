import os
import logging
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# === Google Sheets setup ===
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("playmap-bot-key.json", scope)
client = gspread.authorize(creds)
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1VY_4vuwW63RLgAvvRg3Ehk7zpou1_scoG8oSHOXV1Es/edit").sheet1

# === Telegram Bot setup ===
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [KeyboardButton("🔍 Знайти локацію поблизу")],
        [KeyboardButton("➕ Додати новий майданчик")],
        [KeyboardButton("🌟 Найкращі місця"), KeyboardButton("👤 Мій профіль")]
    ]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    await update.message.reply_text(
        "Привіт! Я PlayMap бот. Обери, що хочеш зробити:",
        reply_markup=reply_markup
    )

# Тимчасова заглушка для додавання локації (буде замінено на покрокове додавання)
async def add_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sheet.append_row(["001", "Майданчик біля школи", "Дитячий", "50.4501", "30.5234", "Так", "Ні", "Так", "", "2025-04-02", update.effective_user.first_name])
    await update.message.reply_text("✅ Локацію додано до Google Таблиці!")

def main():
    application = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("додати майданчик|➕"), add_location))
    application.run_polling()

if __name__ == '__main__':
    main()
