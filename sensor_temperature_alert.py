import os
from dotenv import load_dotenv
import requests
import serial
import time
import asyncio
import math
from telegram import Bot
import logging
from error_handlers import handle_telegram_error,handle_error_ballerina

load_dotenv()

#SENSOR
PUERTO_SERIE = os.getenv("PUERTO_SERIE_DISPOSITIVO_SENSOR")  
BAUDIOS = os.getenv("VEL_DISPOSITIVO")

#BOT TELEGRAM
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID") 

#SERVICIO
BALLERINA_SERVICE = os.getenv("BAL_URL")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)

datos_sensores = {}




async def enviar_alerta(etiqueta, valor):
     if etiqueta =="Temperatura" and valor <20:
                     mensaje = f"⚠️ ¡Alerta! {etiqueta} ha bajado a {valor:.2f}°C"
                     try:
                      await bot.send_message(chat_id=CHAT_ID, text=mensaje)
                      logging.info("Mensaje enviado a Telegram:", mensaje)
                     except Exception as e:
                         handle_telegram_error(e)
                      

                

async def enviar_datos_a_ballerina(data):
    
 if datos_sensores:
    try:
        response = requests.post(BALLERINA_SERVICE, json=data)
        if response.status_code in [200, 201]:
            logging.info("Datos enviados correctamente a Ballerina:", response.text)
        else:
            logging.error("Error al enviar datos a Ballerina:", response.status_code, response.text)
     
    except Exception as e:
             handle_error_ballerina(e)



async def procesar_datos(linea, etiqueta, unidad=""):
    if etiqueta in linea:
        parts = linea.split(":")

        if len(parts)>1:
            try:
                valor_str = parts[1].strip()
                if unidad:
                    valor_str = valor_str.replace(unidad, "").strip()
                valor = float(valor_str)
                logging.info(f"{etiqueta} leida: {valor}{unidad}")

                if math.isnan(valor):
                    logging.warning(f"Error: Lectura de {etiqueta} invalida")
                    return
                
                await enviar_alerta(etiqueta, valor)
               

                datos_sensores[etiqueta] = valor
            

            except ValueError:
                logging.error(f"Error: No se pudo convertir {etiqueta} de la línea {linea}.")
                    


async def main():
   
     arduino = serial.Serial(PUERTO_SERIE, BAUDIOS, timeout=1)
     time.sleep(2)  
     logging.info("Esperando datos de Arduino...")
     while True:
         try:
           
             linea = arduino.readline().decode("utf-8").strip()
             logging.info(f"Línea recibida: {linea}")
             if linea:
                await(procesar_datos(linea,"Temperatura","°C"))
                await(procesar_datos(linea,"Humedad","%"))

             if datos_sensores:
                 await enviar_datos_a_ballerina(datos_sensores)
             else:
                logging.info("No se recibieron datos. Esperando...")
            
             await asyncio.sleep(1)
           

         except serial.SerialException as e:
            logging.error("Error de conexión con el puerto serie:", str(e))
            await asyncio.sleep(2)  

         except ValueError as e:
            logging.error("Error al procesar datos:", str(e))

         except Exception as e:
             logging.error("Error inesperado: %s", str(e))


if __name__ == "__main__":
    asyncio.run(main())
