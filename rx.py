from ground_receive import GroundReceive

# Replace below with the name of the port the receiver RFD is connected to
PORT = "port_name"

receiver = GroundReceive(None, None, PORT)

receiver.receive()