import serial
import time
from common.comms.modules import TelemMessages
from common.comms.modules.generic_comms_device import GenericCommsDevice

sender = GenericCommsDevice('COM4', 115200) 

while True:
    msg = TelemMessages.GroundStationData()
    msg.data.altitude = 5.0
    print("sending data")
    sender.transmit(msg)
    time.sleep(0.1)
