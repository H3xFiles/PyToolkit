import socket
import _thread
import time

ip = "127.0.0.1"
index = 0
open_ports = []
port_to_check=[21,22,23,25,53,80,110,111,135,139,143,389,443,445,587,1015,1352,1433,1723,3306,3389,5060,5900,6001,8080]
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
    while index < len(port_to_check):
        _thread.start_new_thread(portscanner,(ip,port_to_check[index]))
        _thread.start_new_thread(portscanner,(ip,port_to_check[index+1]))
        _thread.start_new_thread(portscanner,(ip,port_to_check[index+2]))
        _thread.start_new_thread(portscanner,(ip,port_to_check[index+3]))
        _thread.start_new_thread(portscanner,(ip,port_to_check[index+4]))
        index +=5
       
        time.sleep(1)
          
except:
    print("Something went very wrong")

print("Port opens:")
for ports in open_ports: 
    print("{} open".format(ports))
  
  