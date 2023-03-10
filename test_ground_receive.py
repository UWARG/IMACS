"""
Run this script `python test_ground_receive.py` to test the ground receive. 

Expected behaviour is for no errors to be output in the terminal and for payloads to be printed
This has not at all been tested with RFDs yet.
"""

from ground_receive import GroundReceive
import time

# Replace below with the name of the port the receiver RFD is connected to
PORT = "COM5"

receiver = GroundReceive(None, None, PORT, 115200)

while True:
    time.sleep(0.1)
    
    receiver.receive()
    print("PAYLOAD", receiver.payload)
    print("pid_set_response", receiver.pid_set_response)

# from ground_receive import GroundReceive

# # Replace below with the name of the port the receiver RFD is connected to
# PORT = "COM5"

# receiver = GroundReceive(None, None, PORT, 115200)

# while True:
#     print(receiver.receiver.ser.read())