
import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Увімкнення логів
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Обробник команди /start
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

# Головна функція запуску бота
def main():
    # Встав свій токен, отриманий у @BotFather
    application = ApplicationBuilder().token("7662179243:AAG_qeFPmiX_Nipg-nCOudGKGlW4uajmdrA").build()

    application.add_handler(CommandHandler("start", start))

    print("Бот працює. Запусти його через main().")
    application.run_polling()

if __name__ == '__main__':
    main()
