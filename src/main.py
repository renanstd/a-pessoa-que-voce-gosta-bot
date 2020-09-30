from settings import BOT_TOKEN
from telegram.ext import Updater, MessageHandler, Filters


updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def answer(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text
    )

message_handler = MessageHandler(Filters.all, answer)

dispatcher.add_handler(message_handler)

updater.start_polling()
