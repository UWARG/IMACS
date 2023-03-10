import serial
import time
from common.comms.modules import TelemMessages
from common.comms.modules.generic_comms_device import GenericCommsDevice

sender = GenericCommsDevice('COM4', 115200) 

alt = 5.0
control = 5

while True:
    msg = TelemMessages.GroundStationData()
    pid_msg = TelemMessages.GroundStationPIDSetResponse()
    msg.data.altitude = alt
    alt = alt + 1
    pid_msg.controller_number = control
    if control < 225:
        control = control + 1
    print("sending data")
    sender.transmit(msg)
    sender.transmit(pid_msg)
    time.sleep(0.1)
