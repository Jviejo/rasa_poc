# creacion de un env para aislar en python con 
## en linux
## hay que usar el 3.7 no el 3.8 que es la ultima version
virtualenv -p /usr/bin/python3.7 p37
## para activar el entorno 
source ./p37/bin/activate

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