# File-Upload-Drive

Script en `python3` que se encarga de automatizar la subida de archivos y carpetas de una ruta especifica de tu sistema a una carpeta alojada en tu cuenta de Google Drive personal aprovechando el uso de la `API` y haciendolo mas rapido y comodamente desde consola.

* El script realiza la subida de archivos en la estructura que se encuentren localmennte y una vez ejecutado valida si los archivos o carpetas ya existen de tal modo que no subira copias infinias innecesarias, sino unicamente los archivos o carpetas nuevas que se actualizen.

* El script imprimira un mensaje validando que se haya subido los archivos correctamente y des mismo modo si los archivos ya existen

# Instalación
```
git clone https://github.com/Firtsmiracle/File-Upload-Drive-Api
cd File-Upload-Drive-Api
pip3 install -r requirements.txt
```
# Requisitos
* Para usar este script deberas realizar los siguentes pasos:

## OBTENR CREDENCIALES DE LA API

1- Obvimante deberas contar con una cuenta google-drive

2- Una vez loegado deberas habilitar la API en la consola de desarrolladores de Google Cloud Platform:

* https://console.cloud.google.com/flows/enableapi?apiid=drive.googleapis.com&hl=es-419

Te pedira que crees un proyecto el cual es un proceso sencillo

Una vez crees el proyecto:

3- Debes dirigirte a la opcion `APIs y Servicios > Credenciales`

4- Lo siguiente sera buscar la opcion `Administrar cuentas de Servicio`, una vez ahi, vamos a la opción `Crear cuenta de Servicio` y rellenas los campos segun el formulario, despues `Crear y continuar`

5- Ahora seleccionaremos en rol - `Editor` y listo.

Finalmente Seleccionamos la cuenta de servicio y nos vamos a la opcion `Claves > Agregar Clave` y creamos una clave en formato `.JSON` con un nombre descriptivo como `credencial.json`, en realidad puede tener el nombre que quieras.
  
## CREACION DE CARPETA EN GOOGLE DRIVE:

1. Creamos una carpeta en nuestro Google Drive con el nombre que queramos:
     
2. Obtenemos el `ID` de la carpeta, eso lo podemos hacer fácil, primero creamos una carpeta y una vez ingresemos en la carpeta, en la url visulizaremos "https://drive.google.com/drive/my-drive/ID_CARPETA".
    
3. Guardamos el ID de la carpeta
    
> Una vez tengamos el archivo `credencial.json`, y el `ID_CARPETA` debemos abrir el script e introducirlos en esta parte del codigo:

![](https://github.com/Firtsmiracle/File-Upload-Drive-Api/blob/main/introducir_requerimientos.PNG)

Si el archivo `credencial.json` esta en la misma ruta que el script solo especificar el nombre - de lo contrario si se debe introducir la ruta.

> Por ultimo debemos introducir la ruta desde donde el script subira los archivos o carpetas que contenga

![](https://github.com/Firtsmiracle/File-Upload-Drive-Api/blob/main/introducir_ruta.PNG)

Si estas en una maquina Windows en la ruta debes especificar el patron clasico : `C:\Users\Carpeta`

Si lo usas en una maquina Linux en la ruta deberas especificar el patron: `/home/user/carpeta/`


# Modo de Uso

```
python3 fileDriveUploader.py
```








