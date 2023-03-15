import serial
import time
from common.comms.modules import TelemMessages
from common.comms.modules.generic_comms_device import GenericCommsDevice

sender = GenericCommsDevice('COM4', 115200) 

alt = 5.0
control = 5
motor_outputs = [0] * 12
longitude=48.0
latitude=-72.0



while True:
    msg = TelemMessages.GroundStationData()
    pid_msg = TelemMessages.GroundStationPIDSetResponse()
    msg.data.altitude = alt
    alt = alt + 1
    

    for i in range(0, 12):
        motor_outputs[i] += i
        motor_outputs[i] %= 256

    msg.motor_outputs = motor_outputs
    longitude+=0
    latitude+=0
    msg.data.latitude=latitude
    msg.data.longitude=longitude

    pid_msg.controller_number = control
    if control < 225:
        control = control + 1
    print("sending data")
    sender.transmit(msg)
    sender.transmit(pid_msg)
    time.sleep(0.5)
