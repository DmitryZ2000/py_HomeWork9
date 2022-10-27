from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bots_commands import *

app = ApplicationBuilder().token("Your token").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("game", game_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("sub", sub_command))
app.add_handler(CommandHandler("mul", mul_command))
app.add_handler(CommandHandler("dev", dev_command))

print('server started')

app.run_polling()
