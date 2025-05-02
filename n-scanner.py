from art import *
import socket 
import sys 
import time
import threading 

usage = "python3 n-scanner.py Start End"

print("-"*60)
tprint("N-Scanner")
print("(a python port scanner) ")
print("    made by Khubaib")
print("-"*60)
print("=> To use this tool write \n=> 'python3 port_scan.py ip-address start-from end-to'")

flag = 1;

if(len(sys.argv) != 4):
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution Error")
    sys.exit()

Start = int(sys.argv[2])
End = int(sys.argv[3])

print("[-] Scanning target ",target)

def scan_port(port):
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((target,port))
    if(not conn):
        print("Yayy! Port {} is OPEN".format(port))
        flag = 0;
    s.close()


for port in range(Start , End +1 ):
    thread = threading.Thread(target = scan_port, args = (port,))
    thread.start()

if(flag == 1):
    print("Sorry but there are no open ports in your network",target)
