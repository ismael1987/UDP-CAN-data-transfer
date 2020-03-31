#author: Honna Gowri Manjunath honna.manjunath@colorado.edu
#Course: ITP - Network Engg track
import time
import socket    #Importing socket library to create socket, send and receive data between client and server
import sys  #Importing sys library to take user input from command prompt
import os  #Importing os library to get the path of the file and to check if the file exists
ss=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Creating a socket for communication
Server_port=int(sys.argv[1]) #Taking the porting on which the server should listen
if (int(sys.argv[1])>5000):  #Applying a condition to take in only ports greater than 5000 
    ss.bind(('',Server_port)) #If the port is above 5000 bind it to the socket with the condition to accept any IP
    print(" Server Binded on port : "+ str(Server_port))
else:
    print("Port number should be greater than 5000")
    exit()
'''
get_input function
To send the file to the client when evoked
'''
def get_input():
    (filename,(IP,Port))=ss.recvfrom(1024) #Receive the filename from the client
    fname=filename.decode()
    address=(IP,Port)
    c=os.path.isfile(fname) #Check if the file exists
    if(c==True):
        print("file exist")
        ss.sendto("exist".encode(),address)
        fileSize=os.path.getsize(fname)
        #packet=fname + ' '+str(fileSize)
        ss.sendto(str(fileSize).encode(),address) #Send the file size.
        fopen=open(fname,'rb')#Open the file
        Leftover=0
        #ss.settimeout(7)
        while 1:
            where = fopen.tell()
            line = fopen.readline()
            if not line:
              time.sleep(1)
              fopen.seek(where)
              print("same siaze")

            else:
             #data=fopen.read(1024)
             #print("Data Sent")
             ss.sendto(line,address)  #Send the data.
             ACK="Not delivered"
             while ACK == "Not delivered":
                try:
                    print("Waiting for ACK")
                    data=ss.recv(1024)
                    ACK=data.decode()
                except socket.timeout(7):
                    ss.sendto(data,address)  #Resend the data to the server
             Leftover=Leftover+ len(line)
             print("ACK Received")
             print(Leftover)
        #file=fopen.read(1024)
        #ss.sendto(file,address) #Send the next set of data to the client if ack is received.
    else:
        print("no such file")
        ss.sendto("doesn't exist".encode(),address)
        #fopen=open('Errormessage.txt','rb') 
        #file=fopen.read(8)
        #ss.sendto(file,address) #Send across the data stating the file doesn't exist
    ss.settimeout(70)



 

'''
Main function 
'''       

while(1):         
    (usero,address)=ss.recvfrom(8) #Receive the option from the client end 
    option=usero.decode()
    print(option)
    if(option=='1'):
        get_input()
  
    
