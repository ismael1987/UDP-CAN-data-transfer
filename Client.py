#author: Honna Gowri Manjunath honna.manjunath@colorado.edu
#Course: ITP - Network Engg track

import socket     #Importing socket library to create socket, send and receive data between client and server
import sys        #Importing sys library to take user input from command prompt
import os         #Importing os library to get the path of the file and to check if the file exists
cs=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #Creating the socket
Server_IP=sys.argv[1]       #Reading the user input of the Server IP and storing it in Server_IP
Server_port=sys.argv[2]     #Reading the user input of the server port and storing it in Server_port

'''
Printing the options for users to select
'''

print('*' *50)    
print("Kindly enter the command from the below options")
print("\n1)Get:Enter 1 \n2)Put:Enter 2 \n")
print( '*' *50)

'''
get_input function
This function when called gets the user input files from the server and stores it at the client as Received_<file name>
'''
def get_input():
    file_name=input("Please enter the desired file name: ") #Request the user for the input of the desired file
    cs.sendto(file_name.encode(),(Server_IP,int(Server_port))) #Send the file name to the server
    #data=''
    #while data=='':
    (line,address)=cs.recvfrom(1024) #Receive the data from the server
    message=line.decode() #Store the data in a variable to check if the file exists at the server end
    if (message=="doesn't exist"):
        print("File doesn't exist") 
    else:
        (contents,address)=cs.recvfrom(1024) #Receive the file size that the server is sending
        fSize=contents.decode()
        #print("File name received "+filename)
        print("File size received "+fSize)
        #rfile=open('Received_'+ file_name,'ab') #Open a file
        Leftover=0
        while 1:
            print("Incoming client data")
            rfile=open('Received_'+ file_name,'ab')
            (line,Address)=cs.recvfrom(1024) #Receive the data from client end
            rfile.write(line) #Write the data into the file
            cs.sendto("ACK".encode(),Address) #Send acknowledgment that the data has been received
            print("ACK Sent")
            Leftover=Leftover+1024 #Increment the amount if data that needs to be received.
            print(Leftover)
        rfile.close()
    
        

 

'''
Main program
'''

while(1):
    option=input("Enter the desired option: ")
    cs.sendto(option.encode(),(Server_IP,int(Server_port))) #Sending the user option to Server 
    if(option=='1'):
        get_input()
    
    
   
     
