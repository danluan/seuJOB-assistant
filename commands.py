from telegram import Update
from telegram.ext import ContextTypes
from loguru import logger
import os
import re

import util.geminiHandler as gemini_util

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Olá! 👋 Sou o SeuJOB, seu assistente virtual para análise de currículos. Estou aqui para te ajudar a criar um currículo incrível e aumentar suas chances de conseguir o emprego dos sonhos. 💼 Me envie seu currículo e eu te darei dicas de melhorias e uma nota de 0 a 5. 😉")

def analysis(model):

    async def downloader(update, context):
        chat_id = update.effective_chat.id
        file_name = update.message.document.file_name
        
        logger.info(f'CHAT {chat_id} : Document received')
        if file_name.split('.')[-1] != 'pdf':
            await context.bot.send_message(chat_id=chat_id, text='Desculpe, no momento só posso analisar documentos em PDF :( \n Quem sabe no futuro não poderei ver outros tipos de documentos? ;)')
            return
        
        file = await context.bot.get_file(update.message.document)
        
        os.makedirs(f'temp/{chat_id}', exist_ok=True)
        await file.download_to_drive(f'temp/{chat_id}/{file_name}')
        
        logger.info(f'CHAT {chat_id} : Document saved')
        
        await context.bot.send_message(chat_id=chat_id, text='Documento recebido. Vou analisar e te retorno em breve.')
        
        logger.info(f'CHAT {chat_id} : Requesting analysis from Gemini API')
        response = gemini_util.pdf_analysis(f'temp/{chat_id}/{file_name}', model)
        
        logger.info(f'CHAT {chat_id} : Sending analysis from Gemini API')
        try:
            await context.bot.send_message(chat_id=chat_id, text=response, parse_mode='markdown')
        except Exception as e:
            print(f"Erro ao enviar mensagem: {str(e)}")
            await context.bot.send_message(chat_id=chat_id, text="Desculpe, houve um erro ao processar sua mensagem. Tente novamente.")

        os.remove(f'temp/{chat_id}/{file_name}')
        logger.info(f'CHAT {chat_id} : Temporary document deleted')
        
    return downloader
        
def handle_message_unique(model):
    
    async def handle_message(update, context):   
        chat_id = update.effective_chat.id
        logger.info(f'CHAT {chat_id} : Message received')
        
        prompt_parts = [
        update.message.text,
        ]

        response = model.generate_content(prompt_parts)
        
        await update.message.reply_text(text = response.text, parse_mode='Markdown')
    
    return handle_message
