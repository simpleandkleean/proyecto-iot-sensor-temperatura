# Proyecto IoT de Sensor de Temperatura

Este proyecto consiste en un sistema IoT que monitorea y envía datos de temperatura y humedad. Utiliza sensores conectados a un microcontrolador, gestionando el flujo de datos de manera eficiente.

## Características
- Monitoreo de temperatura y humedad en tiempo real.
- Envío de alertas a través de Telegram si la temperatura cae por debajo de un umbral.
- Gestión de errores para asegurar la fiabilidad de la comunicación.

## Tecnologías Usadas
- Ballerina como intermediario para el envío de datos a otros servicios.
- Telegram API para el envío de alertas.
- Python para el procesamiento de datos.
- Arduino para la lectura de datos de los sensores.

## Instalación
1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias utilizando pip. Asegúrate de tener `pip` instalado y ejecuta:
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
   ```plaintext
   # SENSOR
   PUERTO_SERIE=nombre_del_puerto
   BAUDIOS=velocidad_del_sensor

   # BOT TELEGRAM
   BOT_TOKEN=tu_token_de_telegram
   CHAT_ID=tu_chat_id

   # SERVICIO
   BALLERINA_SERVICE=url_del_endpoint_de_ballerina

   

Descripción de las Variables

- PUERTO_SERIE: El puerto serie donde está conectado el sensor.

- BAUDIOS: La velocidad de comunicación del sensor.

- BOT_TOKEN: El token del bot de Telegram.

- CHAT_ID: El ID del chat que recibirá las alertas.

- BALLERINA_SERVICE: La URL del endpoint de Ballerina que procesará los datos.

Nota de Seguridad:
Evita compartir el contenido del archivo .env públicamente, ya que puede contener información sensible que podría facilitar vulneraciones al sistema.

Bot de Telegram:
Utiliza BotFather en Telegram para crear y gestionar tu bot. Una vez creado, obtén el token del bot y colócalo en tu archivo .env.

Para obtener tu chat ID, busca el bot llamado UserInfoBot en Telegram. Este bot te facilitará tu ID de chat, que deberás pasar como parámetro en tu archivo .env, ya que será la cuenta de Telegram que recibirá las alertas.

Ballerina:
Asegúrate de arrancar el servicio de Ballerina antes de ejecutar el script de Python, ya que el script está diseñado para enviar datos a este servicio.

Uso:
El sistema enviará alertas a través de Telegram cuando la temperatura sea inferior a 20°C.

Los datos se envían a Ballerina para su procesamiento adicional y posible envío a otros servicios.

Advertencia:
Este proyecto está diseñado con fines educativos para aprender sobre el funcionamiento de IoT y el flujo de datos. No se recomienda su uso en entornos profesionales, ya que aún se requieren medidas de seguridad iniciales y podría no cumplir con todas las necesidades de producción.

Contribuciones:
¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, por favor, abre un issue o envía un pull request.

Licencia:
Este proyecto está bajo la MIT License. Consulta el archivo LICENSE para más detalles.
