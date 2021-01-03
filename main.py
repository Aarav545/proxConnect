import os
import time

print("Hello and welcome to proxConnect. Please make sure you have the password to your proxy ip address otherwise this program will not work \n (or you can use an open one which is fine too)")

time.sleep(1)

ip = input("Please enter the ip address for your proxy")

usr = input("Please enter the username for the ip address")

passw = input("Please enter the password for the ip address (if you do not have one just press enter)")

port = int(input("Please enter the port"))

nport = port + 1

def __connect__ (ip, passw, port, usr):
    os.system("export HTTP_PROXY=" + usr + ":" + passw + "@" + ip + ":" + port)
    os.system("export HTTPS_PROXY=" + usr + ":" + passw + "@" + ip + ":" + nport)
    

__connect__(ip, passw, port, usr)

print("If you knew all the proper information you should be connected!")


