import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

    
    client.connect(("127.0.0.1", 5000))

    messaggio = input("Inserisci un messaggio: ")
    client.sendall(messaggio.encode())

    risposta = client.recv(1024)
    print("Risposta del server:", risposta.decode())