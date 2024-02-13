import logging
from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

BOT_TOKEN = "6512203812:AAFTZDsjqVAfZnqOjP7CpyvJwqcPgu2rf7U"

CHANNEL_ID = -1002048478233 

GROUP_ID = -4122888958 


async def forward_message(update: Update, context: Application):
    message = update.effective_message
    if message.chat_id == CHANNEL_ID:
        await message.forward(chat_id=GROUP_ID)


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))
    application.run_polling()


if __name__ == "__main__":
    main()
