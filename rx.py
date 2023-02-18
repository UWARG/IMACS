from ground_receive import GroundReceive

from common.comms.modules.generic_comms_device import GenericCommsDevice

# Replace below with the name of the port the receiver RFD is connected to
PORT = "COM5"

import sys
import time

if __name__ == "__main__":
    r = GenericCommsDevice(PORT, 115200)
    while True:

        time.sleep(0.1)

        result, out = r.receive()
        print(result)
        if not result:
            #sys.exit(-1)
            continue

        print(type(out))
        print(out.header.type)
        print(out.arm)




# if __name__ == "__main__":

#     r = 

#     receiver = GroundReceive(None, None, PORT)

#     receiver.receive()
