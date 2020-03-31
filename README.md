
#UDP-CAN-data-transfer
# TCP-CAN
if we need to run the app and no real device the so we have to init virtual on ubuntu :
1- open terminal and write this command:
-- sudo apt-get install can-utils   //this just for one time
-- sudo modprobe vcan              // this also one time
-- sudo ip link add dev vcan0 type vcan  // this each time we want to use the app
-- sudo ip link set up vcan0                     // this each time we want to use the app
-- to run it "cangen vcan0 -v"                 // when we want to run the simulation
======================================================================================
// To run the app:
1- run the server ==> python3 Server.py portNumber (ex:python3 Server.py 5555)
2- run the client ==> python3 Client.py serverIP portNumber (ex:python3 Client.py 127.0.0.1 5555)
3- run the write.py to start writing from can interface to the file ==> python3 write.py vcan0
//if we use real CAN BUS device then ==> python3 write.py vcan

==============================

