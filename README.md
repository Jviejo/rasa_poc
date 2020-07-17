# creacion de un env para aislar en python con 
## en linux
## hay que usar el 3.7 no el 3.8 que es la ultima version
virtualenv -p /usr/bin/python3.7 p37
## para activar el entorno 
source ./p37/bin/activate
## para desactivar el entorno 
deactivate
## si nos queremos asegurar la version de python despues de activar
python --version
## no debde de dar Python 3.8.2 si hemos creado un entorno con 3.8
## antes de crear el entorno virtual debemos de tener instalado la version de python deseada (https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)
## url para ver las versiones y con el siguiente comando se instala
sudo apt install python3.6

# instalacion de rasa
https://rasa.com/docs/rasa/user-guide/installation/

# instalacion de rasa x
https://rasa.com/docs/rasa-x/installation-and-setup/install/local-mode/

# para ejecutar la pagina web chat.html
1. hay que instalar node si no esta: https://nodejs.org/es/download/package-manager/
2. en linux es interesante usar nvm: gestiones diferentes versiones de node.js
        https://github.com/nvm-sh/nvm
3. instalar: npm i http-server 
4. ejecutar: http-server --cors
5. en el navegador: http://localhost:8081/chat.html

# Lanzar RASA ACTIONS
### cre un servidor que escucha en la url definida en el fichero endpoints.yml
```
action_endpoint:
  url: "http://localhost:5055/webhook"
```
con rasa run actions crea el servidor

# Lanzar rasa x
rasa x --enable-api
Lanza un servidor web para probar el modelo por el puerto 5002

Al activar el api permite escuchar por el puerto 5005. Se puede configurar este puerto

# Configuracion del Widget
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id="webchat"></div>
    <script src="https://cdn.jsdelivr.net/npm/rasa-webchat/lib/index.min.js"></script>
    <script>
         WebChat.default.init({
           selector: "#webchat",
           initPayload: "/pagar",
           customData: {"language": "es"}, // arbitrary custom data. Stay minimal as this will be added to the socket
           socketUrl: "http://localhost:5005",
           socketPath: "/socket.io/",
           title: "Oficina Tributaria",
           subtitle: "Cobro de recibos",
           params: {"storage": "session"} // can be set to "local"  or "session". details in storage section.
         })
       </script>    
</body>
</html>
```

# Fichero credentials
## Se pone info para integraciones
## El apartado socketio de credentials.yml debe de estar

```yml
socketio:
  user_message_evt: user_uttered
  bot_message_evt: bot_uttered
  session_persistence: true
```

# Integración con Telegram
Hay que crear un bot en telegram
https://rasa.com/docs/rasa/user-guide/connectors/telegram/

## hay que agregar estas lineas en el credentials.yml

```yaml
telegram:
  access_token: "access token proporcionado por telegram"
  verify: "jvhrasa_bot"
  webhook_url: "https://f3c75311f0c6.ngrok.io/webhooks/telegram/webhook"

```

# Integración con whatapps a través de twilio
Abrir cuenta en twilio y crear una sandbox definir la redireccion 
https://www.twilio.com/console/sms/whatsapp/sandbox
https://f3c75311f0c6.ngrok.io/webhooks/twilio/webhook a nuestra máquina.
Esto enlace con el rasa x a través del ngrok

```yaml
twilio:
    account_sid: "account code"
    auth_token: "auth token"
    twilio_number: "whatsapp:+14155238886"  # if using WhatsApp: "whatsapp:+440123456789"
```