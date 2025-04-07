import logging
import requests
from telegram import error as error



def handle_telegram_error(e):
    if isinstance(e, (error.Forbidden, error.BadRequest, error.NetworkError)):
        logging.error("Error al enviar mensaje a Telegram: %s", str(e))
        
    elif isinstance(e, error.TelegramError):
        logging.error("Error específico de Telegram: %s", str(e))
    else:
        logging.error("Error inesperado al enviar el mensaje a Telegram: %s", str(e))


def handle_error_ballerina(e):
    if isinstance(e, requests.exceptions.RequestException):
        logging.error("Error al enviar de datos a Ballerina:",str(e))
    else:
        logging.error("Se produjo un error al enviar los datos a Ballerina:", str(e))