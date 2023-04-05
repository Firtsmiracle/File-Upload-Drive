import os
import io
import hashlib
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload, MediaIoBaseUpload

# ID de la carpeta de destino en Google Drive
FOLDER_ID = "Ingresa el ID de la carpeta Drive"

# Credenciales de servicio de Google Drive
SCOPE = ["https://www.googleapis.com/auth/drive.file"]
CREDENCIAL_JSON = "Ingresa la ruta del archivo .json"
creds = None
creds = service_account.Credentials.from_service_account_file(CREDENCIAL_JSON, scopes=SCOPE)

def create_folder_if_not_exists(folder_name, folder_id):
    #Esta función crea una carpeta en el Drive si es que no existe y devuelve el ID de la carpeta
    try:
        drive_service = build("drive", "v3", credentials=creds)
        query = "mimeType='application/vnd.google-apps.folder' and trashed=false and name='{0}' and '{1}' in parents".format(folder_name, folder_id)
        results = drive_service.files().list(q=query, fields="nextPageToken, files(id)").execute()
        items = results.get("files", [])
        if items:
            return items[0]["id"]
        else:
            file_metadata = {"name": folder_name, "parents": [folder_id], "mimeType": "application/vnd.google-apps.folder"}
            folder = drive_service.files().create(body=file_metadata, fields="id").execute()
            return folder.get("id")
    except HttpError as error:
        print("Error al crear la carpeta: ", error)
        return None


def check_file_exists_in_folder(file_name, folder_id):
    #Esta función omprueba si un archivo ya existe en una carpeta del Drive
    try:
        drive_service = build("drive", "v3", credentials=creds)
        query = "trashed=false and name='{0}' and '{1}' in parents".format(file_name, folder_id)
        results = drive_service.files().list(q=query, fields="nextPageToken, files(id)").execute()
        items = results.get("files", [])
        if items:
            return True
        else:
            return False
    except HttpError as error:
        print("Error buscando el archivo: ", error)
        return False


def upload_file(file_path, file_name, folder_id):
    #Esta función sube un archivo a el Drive si no existe.
    if not check_file_exists_in_folder(file_name, folder_id):
        try:
            drive_service = build("drive", "v3", credentials=creds)
            file_metadata = {"name": file_name, "parents": [folder_id]}
            media = MediaFileUpload(file_path, resumable=True)
            file = drive_service.files().create(body=file_metadata, media_body=media, fields="id").execute()
            print("El archivo {0} se ha subido correctamente a Google Drive.".format(file_name))
        except HttpError as error:
            print("Error en la subida del archivo {0}: {1}".format(file_name, error))
    else:
        print("El archivo {0} ya existe en Google Drive.".format(file_name))


def upload_folder(folder_path, folder_id):
    #Subimos una carpeta a el Drive
    folder_name = os.path.basename(folder_path)
    folder_id = create_folder_if_not_exists(folder_name, folder_id)
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            # Verificamos si el archivo ya existe en Drive
            try:
                drive_service = build("drive", "v3", credentials=creds)
                query = "trashed = false and name = '{0}' and parents in '{1}'".format(item, folder_id)
                existing_files = drive_service.files().list(q=query, fields="files(id)").execute().get("files", [])
                if existing_files:
                    print("El archivo {0} ya existe en Google Drive".format(item))
                else:
                    upload_file(item_path, item, folder_id)
            except HttpError as error:
                print("Error al verificar si el archivo {0} ya existe en Google Drive: {1}".format(item, error))
        elif os.path.isdir(item_path):
            upload_folder(item_path, folder_id)


if __name__ == "__main__":
    PATH = "Ingresa la ruta de donde se subiran los archivos y carpetas Ejemp: Linux - /home/user o Windows - C:\Windows\User"
    upload_folder(PATH, FOLDER_ID)
