import google.generativeai as genai

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from loguru import logger

from config import settings

from commands import start, analysis, handle_message_unique
import util.geminiHandler as gemini_util



def main():
    logger.info('Starting seuJOB Assistant.')
    
    logger.info('Bot instance created.')
    
    try:
        bot = ApplicationBuilder().token(settings.BOT_TOKEN).build()
        logger.info('Bot instance created.')

    except Exception as e:    
        bot = None
        logger.error(f'An error occurred while creating the bot instance. {e}')
    
    try:
        genai.configure(api_key=settings.GEMINI_API_KEY)
        logger.info('Gemini API configured.')
        gemini_connection = True
    except Exception as e:
        logger.error(f'An error occurred while configuring the Gemini API. {e}')
        gemini_connection = False
            
    if bot and gemini_connection:
        try:
            logger.info("Adding commands to bot...")
            
            model = gemini_util.getModel(genai)
            
            bot.add_handler(
                CommandHandler(["start", "help"], start)
            )
            
            bot.add_handler(
                MessageHandler(filters.Document.ALL, analysis(model))
            )
            
            bot.add_handler(
                MessageHandler(filters.TEXT and ~filters.COMMAND, 
                    handle_message_unique(gemini_util.getModel(genai)))
            )
            
        except Exception as e:
            logger.error(f'An error occurred while adding bot commands. {e}')

        logger.info("Starting bot...")
        bot.run_polling()
        
    model = gemini_util.getModel(genai)
    
    logger.info('Commands added.')
    logger.info('Running...')
    bot.run_polling()

if __name__ == '__main__':
    main()
