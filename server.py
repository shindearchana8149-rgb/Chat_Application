import socket, threading

HOST="0.0.0.0"; PORT=5000
clients=[]

def broadcast(msg,sender=None):
    for c in clients:
        if c is not sender:
            try: c.send(msg)
            except: pass

def client(c):
    while True:
        try:
            msg=c.recv(1024)
            if not msg: break
            broadcast(msg,c)
        except: break
    if c in clients: clients.remove(c)
    c.close()

s=socket.socket(); s.bind((HOST,PORT)); s.listen()
print(f"Chat server on port {PORT}")
while True:
    c,addr=s.accept(); clients.append(c)
    threading.Thread(target=client,args=(c,),daemon=True).start()
