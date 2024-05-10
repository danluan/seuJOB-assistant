import google.generativeai as genai

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, ContextTypes

from config import settings
import util.geminiHandler as gemini_util

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Olá {user.first_name}, como posso ajudar?")

async def handle_documents(update: Update, context: ContextTypes.DEFAULT_TYPE):
    document = update.message.document
    if document:
        await update.message.reply_text("Processando arquivo...")
        
        # Obter o objeto File
        file = await context.bot.get_file(document.file_id)
        
        # Baixar o arquivo para o servidor local
        file_path = f"./{document.file_name}"
        await file.download(custom_path=file_path)
        
        # Aqui você pode processar o arquivo como necessário
        # Exemplo: ler o conteúdo se for um arquivo de texto
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
                # Supondo que o arquivo é texto e temos interesse nos primeiros 100 caracteres
                preview = content[:100]
                await update.message.reply_text(f"Conteúdo do arquivo (primeiros 100 caracteres): {preview.decode('utf-8')}")
        except Exception as e:
            await update.message.reply_text("Houve um erro ao processar o arquivo.")
    else:
        await update.message.reply_text("Nenhum documento recebido.")

def handle_message_unique(model):
    
    async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):       
        
        prompt_parts = [
        update.message.text,
        ]

        response = model.generate_content(prompt_parts)
        
        await update.message.reply_text(response.text)
    
    return handle_message
    


def main():
    app = Application.builder().token(settings.BOT_TOKEN).build()

    genai.configure(api_key=settings.GEMINI_API_KEY)

    model = gemini_util.getModel(genai)

    app.add_handler(CommandHandler("start", start))
    # app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message_unique(model)))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_documents))

    app.run_polling()

if __name__ == '__main__':
    main()
