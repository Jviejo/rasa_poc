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
## antes de crear el entorno virtual debemos de tener instalado la version de python deseada
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