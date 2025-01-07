import socket
import threading

def manejarCliente(cliente_socket,addr):
    datos = []
    try:
        while True:
            if len(datos) == 0:
                cliente_socket.send(b"Login: ")
                dataCliente = cliente_socket.recv(1024).decode('utf-8').lower().strip()
            elif len(datos) == 1:
                cliente_socket.send(b"Passwd: ")
                dataCliente = cliente_socket.recv(1024).decode('utf-8').lower().strip()
            if dataCliente == "exit":
                cliente_socket.send("Sesion cerrada.\n".encode('utf-8'))
                break          
            datos.append(dataCliente)
            if len(datos) == 2:
                if validarUsuario(user=datos[0],password=datos[1]):
                    cliente_socket.send("Sesion Iniciada.\n".encode('utf-8'))
                    datos.clear()
                else:
                    datos.clear()
                    cliente_socket.send("Usuario y constraseña incorrectos.\n".encode('utf-8'))
    except:
        print("ERROR AL CONECTAR")

    finally:
        cliente_socket.close()
        

def iniciarTelnet():
    host = "0.0.0.0"
    port = 23
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((host,port))
        s.listen()
        print("\nServidor escuchando\n")
        while True:
            clienteSocket,addr = s.accept()
            print(f"\nConexion aceptada con la direccion IP: {addr[0]} PORT: {addr[1]}\n")
            hilo = threading.Thread(target=manejarCliente,args=(clienteSocket,addr))
            hilo.start()
    except Exception as error:
        print(f"ERROR AL INICIAR: {error}")
    finally:
        s.close()


def validarUsuario(user:str,password:str):
    with open("credenciales.txt","r") as fichero:
        datos = fichero.read().split()
        valido = True if user == datos[0] and password == datos[1] else False
        return valido
        
        

if __name__ == '__main__':

    iniciarTelnet()