from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *


async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    some_string = update.message.text
    exp = some_string.split()
    result = eval(exp[1])
    await update.message.reply_text(f'Result of {exp[1]} is {result}')

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi - is greeting\n/time - time now\n/help - commands\n'
                                    f'/sum - enter two numbers splitted by space to get sum\n'
                                    f'/calc - enter expression to calc')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 321
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')