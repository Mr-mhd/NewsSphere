import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler,
)
import requests

# تنظیمات لاگ
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# حالتهای گفتگو
CHOOSE_COUNTRY = 1

# تنظیمات NewsAPI
NEWS_API_KEY = "YOUR_NEWSAPI_KEY"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "سلام! برای دریافت اخبار، دستور /news را ارسال کنید."
    )

# شروع فرآیند دریافت اخبار
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "لطفاً کد ۲ حرفی کشور موردنظر خود را وارد کنید (مثال: us, ir, de, fr):"
    )
    return CHOOSE_COUNTRY

# دریافت کد کشور و نمایش اخبار
async def choose_country(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    country_code = update.message.text.strip().lower()
    
    # دریافت اخبار از NewsAPI
    params = {
        "country": country_code,
        "apiKey": NEWS_API_KEY,
    }
    
    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data["status"] == "ok" and data["totalResults"] > 0:
            articles = data["articles"][:5]  # ۵ خبر اول
            for article in articles:
                title = article.get("title", "بدون عنوان")
                url = article.get("url", "#")
                message = f"📰 {title}\n🔗 {url}"
                await update.message.reply_text(message)
        else:
            await update.message.reply_text("اخباری یافت نشد.")
    
    except Exception as e:
        logger.error(e)
        await update.message.reply_text("خطا در دریافت اخبار!")
    
    return ConversationHandler.END

# لغو گفتگو
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("عملیات لغو شد.")
    return ConversationHandler.END

def main() -> None:
    # جایگزینی با توکن ربات شما
    application = Application.builder().token("YOUR_TELEGRAM_BOT_TOKEN").build()

    # مدیریت گفتگو
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("news", news)],
        states={
            CHOOSE_COUNTRY: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, choose_country)
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("start", start))

    # شروع ربات
    application.run_polling()

if __name__ == "__main__":
    main()
