# SPANISH
# Proyecto IoT de Sensor de Temperatura

Este proyecto consiste en un sistema IoT que monitorea y envía datos de temperatura y humedad. Utiliza sensores conectados a un microcontrolador, gestionando el flujo de datos de manera eficiente.

## 🚀 Características
- Monitoreo en tiempo real de temperatura y humedad.
- Envío de alertas vía Telegram si la temperatura cae por debajo de un umbral definido.
- Manejo de errores para asegurar una comunicación confiable.

## 🛠️ Tecnologías Usadas
- **Ballerina** como intermediario para el envío de datos a otros servicios.
- **API de Telegram** para notificaciones de alerta.
- **Python** para el procesamiento de datos.
- **Arduino** para la lectura de datos desde los sensores.

## ⚙️ Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias usando pip. Asegúrate de tener `pip` instalado y ejecuta:

   - Para **Windows**:
     ```bash
     pip install -r requirements.txt
     ```

   - Para **Linux/macOS**:
     ```bash
     pip3 install -r requirements.txt
     ```
     o
     ```bash
     python3 -m pip install -r requirements.txt
     ```

3. Crea un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:

   ```env
   # SENSOR
   PUERTO_SERIE=nombre_del_puerto
   BAUDIOS=velocidad_del_sensor

   # BOT DE TELEGRAM
   BOT_TOKEN=tu_token_de_telegram
   CHAT_ID=tu_chat_id

   # SERVICIO
   BALLERINA_SERVICE=url_del_endpoint_de_ballerina
🔐 Descripción de Variables de Entorno
PUERTO_SERIE: Puerto serie al que está conectado el sensor.

BAUDIOS: Velocidad de comunicación del sensor.

BOT_TOKEN: Token del bot de Telegram.

CHAT_ID: ID del chat que recibirá las alertas.

BALLERINA_SERVICE: URL del endpoint de Ballerina que procesará los datos.

⚠️ Nota de Seguridad
Evita compartir públicamente el contenido del archivo .env, ya que puede contener información sensible que comprometa tu sistema.

🤖 Configuración del Bot de Telegram
Usa BotFather en Telegram para crear y gestionar tu bot.

Obtén el token del bot y colócalo en tu archivo .env.

Para obtener tu chat ID, utiliza el bot UserInfoBot. Este bot te proporcionará tu ID de chat, el cual debes incluir como parámetro en tu .env.

🐘 Integración con Ballerina
Asegúrate de iniciar el servicio de Ballerina antes de ejecutar el script de Python, ya que este está diseñado para enviarle datos a dicho servicio.

📡 Uso
El sistema enviará alertas por Telegram cuando la temperatura sea inferior a 20°C.
Los datos también se envían a Ballerina para su procesamiento adicional o integración con otros servicios.

⚠️ Advertencia
Este proyecto está diseñado con fines educativos, para aprender sobre IoT y flujos de datos.
No se recomienda su uso en entornos profesionales, ya que requiere medidas de seguridad adicionales y podría no cumplir con estándares de producción.

# ENGLISH

# IoT Temperature Sensor Project

This project consists of an IoT system that monitors and sends temperature and humidity data. It uses sensors connected to a microcontroller, managing the data flow efficiently.

## 🚀 Features
- Real-time monitoring of temperature and humidity.
- Sends alerts via Telegram if the temperature drops below a defined threshold.
- Error handling to ensure reliable communication.

## 🛠️ Technologies Used
- **Ballerina** as an intermediary for sending data to other services.
- **Telegram API** for alert notifications.
- **Python** for data processing.
- **Arduino** for reading sensor data.

## ⚙️ Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using pip. Make sure you have `pip` installed and run:

   - For **Windows**:
     ```bash
     pip install -r requirements.txt
     ```

   - For **Linux/macOS**:
     ```bash
     pip3 install -r requirements.txt
     ```
     or
     ```bash
     python3 -m pip install -r requirements.txt
     ```

3. Create a `.env` file in the root directory of the project with the following environment variables:

   ```env
   # SENSOR
   PUERTO_SERIE=your_serial_port
   BAUDIOS=sensor_baud_rate

   # TELEGRAM BOT
   BOT_TOKEN=your_telegram_bot_token
   CHAT_ID=your_chat_id

   # SERVICE
   BALLERINA_SERVICE=ballerina_endpoint_url
🔐 Environment Variables Description
PUERTO_SERIE: The serial port where the sensor is connected.

BAUDIOS: The communication speed of the sensor.

BOT_TOKEN: Telegram bot token.

CHAT_ID: Chat ID that will receive the alerts.

BALLERINA_SERVICE: URL of the Ballerina endpoint that will process the data.

⚠️ Security Note
Avoid sharing the content of your .env file publicly, as it may contain sensitive information that could compromise your system.

🤖 Telegram Bot Setup
Use BotFather on Telegram to create and manage your bot.

Retrieve the bot token and place it in your .env file.

To obtain your chat ID, use UserInfoBot. This bot will provide your chat ID, which you must include in your .env.

🐘 Ballerina Integration
Make sure to start the Ballerina service before running the Python script, as the script is designed to send data to this service.

📡 Usage
The system will send Telegram alerts when the temperature drops below 20°C.
Data is also sent to Ballerina for additional processing and potential integration with other services.

⚠️ Disclaimer
This project is intended for educational purposes to learn about IoT systems and data flow.
It is not recommended for professional environments, as it still requires initial security measures and may not meet all production standards.
