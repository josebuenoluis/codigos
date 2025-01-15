import ftplib
import os
import sys

def subirArchivo(ftp_cliente: ftplib.FTP) -> None:
    try:
        ruta = input("\nIngrese la ruta local del archivo: ")
        nombre_archivo = os.path.basename(ruta)
        with open(ruta, "rb") as archivo:
            ftp_cliente.storbinary(f"STOR {nombre_archivo}", archivo)
        print(f"\nArchivo '{nombre_archivo}' subido exitosamente.")
    except FileNotFoundError as error:
        print(f"\nError archivo no encontrado. {error}")
    except ftplib.error_temp as error:
        print(f"\nError al eliminar el archivo. {error}")
    except Exception as error:
        print(f"Otro Error: {error}")

def descargarArchivo(ftp_cliente: ftplib.FTP) -> None:
    try:
        nombre_archivo = input("\nIngrese el nombre del archivo a descargar: ")
        with open(nombre_archivo, "wb") as archivo:
            def callback(data):
                print(data)
                archivo.write(data)
                print(f"\rDescargando {nombre_archivo}...", end="")
            ftp_cliente.retrbinary(f"RETR {nombre_archivo}", callback)
        print(f"\nArchivo '{nombre_archivo}' descargado exitosamente.")
    except ftplib.error_perm as error:
        print(f"\nError al descargar el archivo. {error}")
    except Exception as error:
        print(f"Otro Error: {error}")

def eliminarArchivo(ftp_cliente: ftplib.FTP) -> None:
    try:
        nombre_archivo = input("\nIngrese el nombre del archivo a eliminar: ")
        ftp_cliente.delete(nombre_archivo)
        print(f"\nArchivo '{nombre_archivo}' eliminado exitosamente.")
    except ftplib.error_perm as error:
        print(f"\nError al eliminar el archivo. {error}")
    except Exception as error:
        print(f"Otro Error: {error}")


if __name__ == '__main__':
    try:
        HOST = sys.argv[1]
        USER = sys.argv[2].split(":")[0]
        PASSWORD = sys.argv[2].split(":")[1]

        MENU = """
        1. Listar directorio.
        2. Subir archivo en modo binario desde ruta local.
        3. Descargar archivo del servidor.
        4. Eliminar un archivo del servidor.
        5. Salir y desconectarse."""

        ftp = ftplib.FTP(HOST,USER,PASSWORD)

        print(ftp.welcome)

        while True:
            print(MENU)
            user = input("\nIngrese una opción: ")
            match user:
                case "1":
                    ftp.dir()
                case "2":
                    subirArchivo(ftp)
                case "3":
                    descargarArchivo(ftp)
                case "4":
                    eliminarArchivo(ftp)
                case "5":
                    print("\nSaliendo del servidor!\n")
                    ftp.close()
                    break

    except IndexError:
        print("Error, debe pasar los siguientes argumentos <servidor> <usario>:<contraseña>")

    except ftplib.error_perm:
        print("\nError, fallo al iniciar sesiñon.\n")