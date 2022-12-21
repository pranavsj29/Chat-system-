import socket
# import threading

# from grpc import server
# HOST = "127.0.0.1"
# PORT = 1234 # You can use any port between 0 to 65535
# LISTENER_LIMIT=5
# # main function
# def main():
   
#     # creating the socket class object
#     # AF_INET : we are going to use IPv4 addresses
#     #SOCK_STREAM : we are using tcp packet for communication
#     server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
#     #Creating a try catch block
#     try:
#         server.bind((HOST,PORT))
#         print(f"Running the server on {HOST} {PORT}")
#     except:
#         print(f"unable to bind to host{HOST} and port {PORT}")

#     #Set server limit
#     server.listen(LISTENER_LIMIT)

#     #this while loop will keep listeing to client connection
#     while(1):

#         client,address = server.accept()
#         print("successfully connected to client {address{0}{address{1}}")

# if __name__=='__main__':
#     main()
s =socket.socket()
print('socket creatd')
s.bind(('localhost',9999))
s.listen(3)
print('wating for connection')

while(True):
    c,addr= s.accept()
    print("connected with",addr)

    c.send('Welcomw')

    c.close()