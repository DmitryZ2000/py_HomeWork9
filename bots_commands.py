from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'/hi\n/help\n/game\n/sum_complex x ix y iy')

async def game_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text('Хватит играть - идт работать')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg1 = update.message.text
    item = msg1.split() #На выходе 3 элемента    
    x_real = int(item[1])
    x_complex = int(item[2])
    y_real = int(item[3])
    y_complex = int(item[4])
    await update.message.reply_text(f'{x_real} + {x_complex}i + {y_real} + {y_complex}i = {x_real + y_real }+{x_complex + y_complex}i') 

async def sub_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg1 = update.message.text
    item = msg1.split() #На выходе 3 элемента    
    x_real = int(item[1])
    x_complex = int(item[2])
    y_real = int(item[3])
    y_complex = int(item[4])
    await update.message.reply_text(f'{x_real} + {x_complex}i - ({y_real} + {y_complex}i) = {x_real - y_real }+{x_complex - y_complex}i')

async def mul_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg1 = update.message.text
    item = msg1.split() #На выходе 3 элемента    
    x_real = int(item[1])
    x_complex = int(item[2])
    y_real = int(item[3])
    y_complex = int(item[4])
    await update.message.reply_text(f'({x_real} + {x_complex}i) * ({y_real} + {y_complex}i) = \
        {x_real * y_real  - x_complex * y_complex}+{x_real * y_complex + x_complex * y_real}i')

async def dev_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg1 = update.message.text
    item = msg1.split() #На выходе 3 элемента    
    x_real = int(item[1])
    x_complex = int(item[2])
    y_real = int(item[3])
    y_complex = int(item[4])
    await update.message.reply_text(f'({x_real} + {x_complex}i) / ({y_real} + {y_complex}i) = \
        {(x_real * y_real  + x_complex * y_complex) / (y_real**2 + y_complex**2)} + \
            {(x_complex * y_real - x_real * y_complex)/(y_real**2 + y_complex**2)}i')  