# FIle-Upload-Drive-Api
Script en python3 que se encarga de automatizar la subida de archivos de una ruta especifica a una carpeta en tu Google Drive personal aprovechand el uso de la api y haciendolo comodamente desde la consola



#Requisitos
* Para usar este script odeberes realizar los siguentes pasos:
OBTENR CREDENCIALES DE LA API
  1- Obvimante deberas contar con una cuenta google-drive
  2- Una vez loegado deberas habilitar la Api en la consola de desarrolladores de Google Cloud Platform:

    * https://console.cloud.google.com/flows/enableapi?apiid=drive.googleapis.com&hl=es-419

  Te pedira que crees un proyecto:

  Una vez crees el proyecto:

  Debes dirigirte a la opcion APIs y Servicios > Credenciales

  Lo siguiente sera buscar la opcion "Administrar cuentas de Servicio", una vez ahi vamos a la opcion "+Crear       cuenta de Servicio" y rellenas los campos segun el formulario, despues Crear y continuar:

  Ahora seleccionaremos en rol - "Editor" y listo.

  Finalmente Seleccionamos la cuenta de servicio y nos vamos a la opcion Claves > Agregar Clave y creamos una       clave en formato .JSON con un nombre descriptivo como "credenciales.json".
  
  CREACION DE CARPETA EN GOOGLE DRIVE:
    1. Creamos una carpeta en nuestro Google Drive con el nombre que queramos:
     
    2. Obtenemos el "ID" de la carpeta, eso lo podemos hacer facil una vez ingresemos en la carpeta, en la url        visulizaremos "https://drive.google.com/drive/my-drive/ID_CARPETA".
    
    3. Guardamos el ID de la carpeta
    
#Instalaciòn

```
git clone https://github.com/Firtsmiracle/FIle-Upload-Drive-Api
cd File-Upload-Drive-Api
pip3 install -r requiriments.txt
```


Una vez tengamos el archivo "credenciales.json", y el ID_CARPETA debemos introducirlo en esta parte del codigo:


En Credenciales Introducimos la ruta del archivo "credenciales.json" y en ID_CARPETA el id correspondiente a nuestra carpeta de nuestro GoogleDrive.


y finalmente modificamos la variable carpeta_local a la ruta de donde subiremos los archivos.


#Modo de Uso

Ejecucion:

python3 FileDriveUpload.py





