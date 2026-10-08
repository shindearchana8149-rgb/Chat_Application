import socket, threading
HOST=input("Server IP [127.0.0.1]: ") or "127.0.0.1"
s=socket.socket(); s.connect((HOST,5000))
def receive():
    while True:
        try: print("\n"+s.recv(1024).decode(),end="> ")
        except: break
threading.Thread(target=receive,daemon=True).start()
name=input("Name: ")
while True:
    msg=input("> ")
    if msg.lower()=="quit": break
    s.send(f"{name}: {msg}".encode())
