from http import client
import socket
# import threading

# HOST = "127.0.0.1"
# PORT = 1234



# def main():
#     #creating a socket object
#     client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
#     #connect to the server
#     try:

#         client.connect((HOST, PORT))
#         print("Sucessfully connected to Server ")
#     except:
#         print(f"Unable to connect to server {HOST}{PORT}")

# if __name__=='__main__':
#     main()

c= socket.socket()
c.connect(("localhost",9999))
print(c.recv(1024))