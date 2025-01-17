import ftplib

# Nos muestre el mensaje de bienvenida del servidor
def bienvenida(ftp):
    welcomeMessage = ftp.getwelcome()
    print(welcomeMessage)

def listarDirectorio(ftp):
    # Listar el contenido del directorio
    print(ftp.dir())


# Seguidamente un menú para realizar las siguientes acciones:
def menu():
    pass


# Subir un archivo en modo binario y nos solicite la ruta local. El archivo se almacenará en el servidor con el mismo nombre. Debe mostrar el progreso de la subida.
def subirArchivo():
    pass

# Descargar un archivo del servidor. Debe mostrar el progreso de la descarga.
def descargarArchivo():
    pass

# Eliminar un archivo del servidor
def eliminarArchivo():
    pass

# Salir y desconectar el cliente.
def cerrar():
    pass

if __name__ == '__main__':
    #creadenciales FTP, la contraseña la cambian cada cierto tiempo
    FTP_HOST = "ftp.dlptest.com"
    FTP_USER = "dlpuser"
    FTP_PASS = "rNrKYTX9g7z3RgJRmxWuGHbeu"

    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    ftp.encoding = "utf-8"

    bienvenida(ftp)

    menu = """1. Listar directorio.
    2. Subir archivo en modo binario.
    3. Descargar archivo.
    4. Eliminar archivo.
    5. Salir y desconectarse."""

    