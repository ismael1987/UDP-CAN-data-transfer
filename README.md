# UDP-File-Transfer
#TCP-CAN
#if we need to run the app and no real device the so we have to init virtual on ubuntu : 
# open terminal and write this command: 
1. sudo apt-get install can-utils //this just for one time 
2. sudo modprobe vcan // this also one time 
3. sudo ip link add dev vcan0 type vcan // this each time we want to use the app 
4. sudo ip link set up vcan0 // this each time we want to use the app -- to run it "cangen vcan0 -v"

# To run the app: 
1. run the server ==> python3 Server.py portNumber (ex:python3 Server.py 5555) 
2. run the client ==> python3 Client.py serverIP portNumber (ex:python3 Client.py 127.0.0.1 5555) 
3. run the write.py to start writing from can interface to the file ==> python3 write.py vcan0 
4. if we use real CAN BUS device then ==> python3 write.py vcan

