import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai

openai.api_key = os.environ['6163269434:AAEvXKbI7MvJeeBFn0Ct3aJcdZMjCkpF7NU']

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá! Eu sou um bot baseado na OpenAI. Como posso ajudá-lo?")

def echo(update, context):
    response = openai.Completion.create(
        engine="davinci", prompt=update.message.text, max_tokens=1024, n=1, stop=None, temperature=0.5,
    )
    message = response.choices[0].text.strip()
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    updater = Updater(os.environ['RQJB57WNTYMNJAZR4UXD3E3QOCPPAOMB'], use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_webhook(listen="0.0.0.0", port=int(os.environ.get('PORT', 5000)), url_path=os.environ['RQJB57WNTYMNJAZR4UXD3E3QOCPPAOMB'])
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(os.environ['chatgpt09'], os.environ['RQJB57WNTYMNJAZR4UXD3E3QOCPPAOMB']))
    updater.idle()

if __name__ == '__main__':
    main()
