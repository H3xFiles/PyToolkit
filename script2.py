import socket
import _thread
import time

ip = "127.0.0.1"
open_ports = []
def portscanner(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print("connecting to ip {} at port {} ... ".format(ip, port))
        s.connect((ip, port))
        print("The port {} open".format(port))
        open_ports.append(port)
        s.close()
    except socket.error as e:
        s.close()
try:
    for index in range(1,65535,5):
        _thread.start_new_thread(portscanner,(ip,index))
        _thread.start_new_thread(portscanner,(ip,index+1))
        _thread.start_new_thread(portscanner,(ip,index+2))
        _thread.start_new_thread(portscanner,(ip,index+3))
        _thread.start_new_thread(portscanner,(ip,index+4))
        index +=5
        time.sleep(1)
          
except:
    print("Something went very wrong")

print("Port opens:")
for ports in open_ports: 
    print("{} open".format(ports))
  
  