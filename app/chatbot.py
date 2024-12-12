import cohere
from flask import current_app, session
from .models import db, ChatLog

def get_chatgpt_response(prompt):
    try:
        # Obtiene la clave de API de Cohere desde la configuración de Flask
        cohere_api_key = current_app.config['COHERE_API_KEY']
        co = cohere.Client(cohere_api_key)

        # Genera la respuesta desde el modelo de Cohere
        response = co.generate(
            model='command-r-plus-08-2024',
            prompt=prompt,
            max_tokens=150
        )

        # Procesa el texto generado por el modelo
        result = response.generations[0].text.strip()

        # Guarda el prompt y la respuesta en la base de datos
        chat_log = ChatLog(
            prompt=prompt,
            response=result,
            username=session['username']
        )
        db.session.add(chat_log)  # Añade el objeto a la sesión
        db.session.commit()       # Confirma los cambios en la base de datos

        return result
    except Exception as e:
        # En caso de error, revierte cualquier transacción en la base de datos
        db.session.rollback()
        return f"Error en el chatbot: {str(e)}"
