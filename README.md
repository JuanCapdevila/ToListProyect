# ToListProyect

**Python Challenge de Chaindots - To Do List**

**Descripción** <br>
Se ha desarrollado una aplicación To-Do List para que los usuarios puedan gestionar sus tareas pendientes. La aplicación permite agregar nuevas tareas, especificando su categoría, prioridad y, si es necesario, una fecha límite. También se pueden modificar, eliminar y actualizar el estado (finalizado) de las tareas existentes.

**Requisitos previos** <br>
Los requisitos para el proyecto son tener un navegador web como Google Chrome y tener instalado Python en el sistema operativo. El proyecto fue desarrollado utilizando Python 3.11.2, aunque se puede utilizar otra versión siempre y cuando sea compatible con la versión de Django==4.2.

**Instalación** <br>
Para poder correr el proyecto de manera local, hay que seguir los siguientes pasos: <br>

Dirijirse a esta URL https://github.com/JuanCapdevila/ToListProyect, en el select "Code" de color verde, se puede hacer un git clone mediante la URL del proyecto
o descargar el archivo .ZIP

Una vez con la carpeta del proyecto en el sistema operativo, como **recomendación** crear una carpeta en donde guardaremos el proyecto. Dentro de esta carpeta, se debe crear otra llamada "entorno", donde se creará el entorno virtual. Para crear el entorno virtual, abrimos la terminal en la ubicación de la carpeta "entorno" y ejecutamos el siguiente comando: 'python -m venv myvenv', donde 'myvenv' es el nombre que le daremos al entorno virtual. Es importante tener instalado virtualenv en el sistema operativo.

Una vez creado el entorno virtual, volvemos un directorio atras y hacemos click secundario en la carpeta del proyecto y seleccionamos "Abrir con visual studio code"
o el editor de codigo que utilice con frecuencia.

De manera tal que tiene que quedar dicha estructura

ToListProyect <br>
└───challengetolist <br>
└───controllers <br>
└───static <br>
└───tolist <br>
.gitignore <br>
.db3.sqlite3 <br>
.manage.py <br>
.requerimientos.txt  <br>

Abrimos una terminal, volvemos un directorio atras, entramos a la carpeta enotrno y ejecutamos el siguiente comando para ACTIVAR nuestro entorno virtual
"myvenv\Scripts\activate" te das cuenta que el entorno esta activo cuando delante del path de la terminal se visualiza entre parentesis y de color (nombre_entorno)

Una vez con el entorno activado, volvemos al path del proyecto hasta quedar con la estructura mencionada anteriormente

Ahora, tenemos que instalar los requerimientos en el entorno [El entorno sirve para que los requerimientos del proyecto se instalen de manera aislada y no se instalen
en el sistema operativo, de tal forma que si tenemos varios proyectos con los mismos requerimientos pero diferentes versiones, no generen conflicto]

Ejecutamos los siguientes comandos, instalaremos mediante PIP.

Instalamos / Actualizamos en caso de lo que se requiera <br>
"python -m pip install --upgrade pip"

Y ahora instalamos los requerimientos <br>
"pip install -r requerimientos.txt"

Una vez finalizada la instalacion, ya podemos correr el proyecto mediante el siguiente comando : python manage.py runserver para levantarlo de modo normal
sino se puede levantar el modo debug mediante un archivo launch.json

Se creará un carpeta en el directorio C:\\ para el almacenado de logs. Con una estructura de una carpeta para cada mes por año [formato AAAAMM] y dentro
un archivo .txt en donde se graban los logs, con una estructura de "ToList_{numero_del_mes}_log.txt"

El proyecto esta corriendo una vez que se visualice en la consola lo siguiente <br>

Watching for file changes with StatReloader <br>
Performing system checks... <br>

System check identified no issues (0 silenced). <br>
April 29, 2023 - 18:11:05 <br>
Django version 4.2, using settings 'challenge_tolist.settings' <br>
Starting development server at http://127.0.0.1:8000/ <br>
Quit the server with CTRL-BREAK. <br>

Ingresando a la URL indicada **AGREGANDO AL PATH /proyect** se visualizará el login. De manera que quedaría asi el path **http://127.0.0.1:8000/proyect**

Y de esta forma se puede crear una cuenta para poder loguearse en el sistema y comenzar a utilizarlo. <br>
**Recomendacion** en caso de tener problemas con archivos static, realizar un CTRL+FN+F5 para actualizar el cache del navegador, y si el problema persiste, revisar el path indicado para los static en el archivo settings.py.

**Uso** <br>
El sistema cuenta con una interfaz bastante intuitiva mediante nombres e iconos para la referencia.
Una vez logueado, se redirecciona a la pantalla principal, y en el sidebar seleccionando "Tareas" se dirijirá al listado de tareas en donde se podrá agregar nuevas y realizar una gestión completa de las mismas.

**Tecnologias utilizadas** <br>
Python 3.11.2 <br>
Django 4.2 <br>
JavaScript <br>
HTML <br>
CSS <br>

**Librerias** <br>
Bootstrap 5 <br>
Jquery 3.6 <br>
FontAwesome 6.2 <br>
Toastr <br>
Datatable y sus complementos
