from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bots_commands import *

app = ApplicationBuilder().token("5647698789:AAHMOn6pQG9vG_2mGCh5iG7IKPXAYXnSiic").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("calc", calc_command))


app.run_polling()

