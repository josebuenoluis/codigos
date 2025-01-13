import socket,threading,time
from datetime import datetime

HOST = ""
PORT = 2000

def fechaHora():
    hora_actual = datetime.now()
    formato = hora_actual.strftime("%d de %B de %Y %H:%M:%S")
    return formato

def fecha():
    hora_actual = datetime.now()
    formato = hora_actual.strftime("%d de %B de %Y")
    return formato

def hora():
    hora_actual = datetime.now()
    formato = hora_actual.strftime("%H:%M:%S")
    return formato

def manejo_cliente(clients, clientaddr):
    global numcliente
    lock.acquire()
    global numcliente
    numcliente += 1
    lock.release()
    clients.sendall(f"Cliente numero {numcliente}\n".encode("utf-8"))
    if clients.recv(1024).decode("utf-8") == "hora":
        clients.sendall(f"Hora {hora()}\n".encode("utf-8"))
    elif clients.recv(1024).decode("utf-8") == "fecha":
        clients.sendall(f"Fecha {hora()}\n".encode("utf-8"))
    elif clients.recv(1024).decode("utf-8") == "fechahora":
        clients.sendall(f"Fecha y Hora {fechaHora()}\n".encode("utf-8"))
    
    clients.close()
    time.sleep(5)

if __name__ == '__main__':
    numcliente = 0
    lock = threading.Lock()
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    while True:
        clients, clientaddr = s.accept()
        threading.Thread(target=manejo_cliente,args=(clients, clientaddr))