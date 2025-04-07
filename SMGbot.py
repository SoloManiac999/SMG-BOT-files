from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = '7017774446:AAEV10gaZClV9JIj_tyB7sJEPI9PZi0PsJA'  # Replace with your actual bot token

# Example game data (you can add more)
games = {
    'PC': ['GTA V', 'Minecraft', 'Call of Duty', 'Cyberpunk 2077'],
    'Mobile': ['PUBG Mobile', 'Clash of Clans', 'Asphalt 9', 'Free Fire'],
    'PSP': ['God of War', 'Naruto Shippuden', 'Tekken 6', 'GTA: Vice City Stories'],
    # Add more platforms and games as needed
}

def start(update: Update, context: CallbackContext):
    user_firstname = update.message.from_user.first_name
    text = f"""
Hello {user_firstname}!  
Welcome to *Solo Maniac Games Bot*  
Your one-stop shop for downloading epic game files!  
We’ve got games for *Mobile, PC, PSP, PS1, PS2, PS3, PS4, PS5* and much more!  
Let’s load up and play — where legends are made!  
*Choose your platform below!*

Game on!  
"""

    keyboard = [[InlineKeyboardButton("🎮 Menu", callback_data='menu')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(text, parse_mode='Markdown', reply_markup=reply_markup)

def menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("💻 PC", callback_data='platform_PC')],
        [InlineKeyboardButton("📱 Mobile", callback_data='platform_Mobile')],
        [InlineKeyboardButton("🎮 PSP", callback_data='platform_PSP')],
        # Add more platforms here...
    ]
