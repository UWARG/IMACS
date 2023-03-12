import time
import threading

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from AccessData import AccessData 
from common.comms.modules.generic_comms_device import GenericCommsDevice
from common.comms.modules.TelemMessages.GroundStationData import GroundStationData
from common.comms.modules.TelemMessages.GroundStationPIDSetResponse import GroundStationPIDSetResponse


class GroundReceiveWorker():
    def __init__(self, ground_station_data=None, pid_set_response=None, port="/dev/ttyUSB0", baudrate=115200):
        self.payload = ground_station_data
        self.pid_set_response = pid_set_response
        self.lock = threading.Lock()
        self.is_running = False
        self.receiver = GenericCommsDevice(port=port, baudrate=baudrate)

    
    def receive(self):
        while self.is_running:
            time.sleep(0.1)
            msg_info = self.receiver.receive()
            if msg_info[0]:
                self.__decode(msg_info[1])
    
    def __decode(self, driver_packet):
        if type(driver_packet) == GroundStationData:
            self.__decode_ground_station_data(driver_packet)
        elif type(driver_packet) == GroundStationPIDSetResponse:
            self.__decode_pid_set_response(driver_packet)
        else:
            raise Exception("Unknown packet type")

    def __decode_ground_station_data(self, driver_packet):
        motor_outputs_retriever = AccessData(msg=driver_packet.motor_outputs, start_index=0)
        battery_voltage_retirever = AccessData(msg=driver_packet.battery_voltages, start_index=0)
        controller_values_retriever = AccessData(msg=driver_packet.controller_values, start_index=0)

        self.payload = {
            'motor_outputs': [motor_outputs_retriever.get_data(data_type="B") for i in range(0, 12)], # list of 12 ints
            'gps_data': {
                'lat' : driver_packet.data.latitude, # double
                'lon' : driver_packet.data.longitude, # double
                'alt' : driver_packet.data.altitude, # float
            },  
            'climb_rate': driver_packet.data.climb_rate, # float
            'heading': driver_packet.data.heading, # float
            'air_speed': driver_packet.data.air_speed, # float
            'ground_Speed': driver_packet.data.ground_speed, # float
            'imu_data':{
                'roll': driver_packet.data.roll, # float
                'pitch': driver_packet.data.pitch, # float
                'yaw': driver_packet.data.yaw, # float
            },
            'roll_rate': driver_packet.data.roll_rate, # float
            'pitch_rate': driver_packet.data.pitch_rate, # float
            'yaw_rate': driver_packet.data.yaw_rate, # float
            'battery_voltages': [battery_voltage_retirever.get_data(data_type="B") for i in range(0, 13)], # list of 13 ints
            'controller_voltages':  [controller_values_retriever.get_data(data_type="B") for i in range(0, 16)], # list of 16 ints
            'flag': driver_packet.header.flag, #AccessData(msg=driver_packet.header.flag, start_index=0).get_data(data_type="B"), # int
            'length': AccessData(msg=driver_packet.header.length, start_index=0).get_data(data_type="H"), # short
            'type': driver_packet.header.type #AccessData(msg=driver_packet.header.type, start_index=0).get_data(data_type="B"), # int
        }

    def __decode_pid_set_response(self, driver_packet):
        self.pid_set_response = {
            "flag": driver_packet.header.flag, #AccessData(msg=driver_packet.header.flag, start_index=0).get_data(data_type="B"), # int
            "length": AccessData(msg=driver_packet.header.length, start_index=0).get_data(data_type="H"), # short
            "type": driver_packet.header.length, #AccessData(msg=driver_packet.header.type, start_index=0).get_data(data_type="B"), # int
            "controller_number": driver_packet.controller_number, #AccessData(msg=driver_packet.controller_number, start_index=0).get_data(data_type="B"), # int
            "controller": [  # list of 6 dicts each with three floats (P, I, D)
                    {
                        "P": driver_packet.controller.axes[i].P, 
                        "I": driver_packet.controller.axes[i].I, 
                        "D": driver_packet.controller.axes[i].D 
                    } for i in range(0,6)
                ],
            #"crc": AccessData(msg=driver_packet.crc, start_index=0).get_data(data_type="f"), # float
        }

    def getCoordinates(self):
        if self.payload is None:
            return None
        else:
            return {
                "latitude": self.payload["gps_data"]["lat"],
                "longitude": self.payload["gps_data"]["lon"],
            }
    def getDroneInfo(self):
        if self.payload is None:
            return None
        else:
            return {
                "altitude": self.payload["gps_data"]["alt"],
                "ground_speed": self.payload["ground_speed"],
                "battery": self.payload["battery_voltages"][0],
                "airspeed": self.payload["air_speed"],
            }
        
    def getBatteryInfo(self):
        if self.payload is None:
            return None
        else:
            return self.payload["battery_voltages"]
        

    def getMotorOutputs(self):
        if self.payload is None:
            return None
        else:
            return self.payload["motor_outputs"]
        
    def getRotationInfo(self):
        if self.payload is None:
            return None
        else:
            return {
                "roll": self.payload["roll_rate"],
                "pitch": self.payload["pitch_rate"],
                "yaw": self.payload["yaw_rate"],
            }
        
    def getIMUData(self):
        if self.payload is None:
            return None
        else:
            return self.payload["imu_data"]
        
    def getFullPayload(self):
        if self.payload is None:
            return None
        else:
            return self.payload
        
    def start(self):
        self.is_running = True
        # start a new thread for the receive function
        self.receive_thread = threading.Thread(target=self.receive)
        self.receive_thread.start()
        
    def stop(self):
        self.is_running = False
        # wait for the receive thread to finish
        self.receive_thread.join()
class DroneInfo:
    def __init__(self, groundReceiverWorker):
        self.groundReceiverWorker = groundReceiverWorker

    def getData(self):
        return self.groundReceiverWorker.getDroneInfo()
    
class Coordinates:
    def __init__(self, groundReceiverWorker):
        self.groundReceiverWorker = groundReceiverWorker

    def getData(self):
        return self.groundReceiverWorker.getCoordinates()


class ThrottleInfo:
    def __init__(self, groundReceiverWorker):
        self.groundReceiverWorker = groundReceiverWorker

    def getData(self):
        return self.groundReceiverWorker.getMotorOutputs()

class BatteryVoltages:
    def __init__(self, groundReceiverWorker):
        self.groundReceiverWorker = groundReceiverWorker

    def getData(self):
        return self.groundReceiverWorker.getBatteryInfo()

class RotationInfo:
    def __init__(self, groundReceiverWorker):
        self.groundReceiverWorker = groundReceiverWorker

    def getData(self):
        return self.groundReceiverWorker.getRotationInfo()

class IMUData:
    def __init__(self, groundReceiverWorker):
        self.groundReceiverWorker = groundReceiverWorker

    def getData(self):
        return self.groundReceiverWorker.getIMUData()

class FullPayload:
    def __init__(self, groundReceiverWorker):
        self.groundReceiverWorker = groundReceiverWorker

    def getData(self):
        return self.groundReceiverWorker.getFullPayload()
    
class MotorInfo: 
    def __init__(self, groundReceiverWorker):
        self.groundReceiverWorker = groundReceiverWorker

    def getData(self):
        return self.groundReceiverWorker.getMotorOutputs()
    

def test_data_getter_classes():
    """
    run `python ground_receive.py` to test these classes with RFD
    """
    receiver = GroundReceiveWorker()
    receiver.start()
    imuDataGetter = IMUData(receiver)
    rotationInfoGetter = RotationInfo(receiver)
    batterVoltageGetter = BatteryVoltages(receiver)
    throttleInfoGetter = ThrottleInfo(receiver)
    coordinatesGetter = Coordinates(receiver)
    droneInfoGetter = DroneInfo(receiver)
    motorInfoGetter = MotorInfo(receiver)

    while True:
        print(imuDataGetter.getData())
        print(rotationInfoGetter.getData())
        print(rotationInfoGetter.getData())
        print(batterVoltageGetter.getData())
        print(throttleInfoGetter.getData())
        print(coordinatesGetter.getData())
        print(droneInfoGetter.getData())
        print(motorInfoGetter.getData())

        time.sleep(0.1)

if __name__ == "__main__":
    test_data_getter_classes()

class GroundReceive(QThread):
    """
    Make sure GroundReceive is being imported from the correct file
    """
    new_data = pyqtSignal(dict)
    receiver = GroundReceiveWorker(port="COM5")
    def run(self, receiver=receiver):
        self.threadActive = True
        # Mocks actual data coming from RFD
        while self.threadActive:
            receiver.receive()
            self.payload = receiver.payload
            if self.payload is not None:
                self.new_data.emit(self.payload)

    def __init__(self, receiver=receiver):
        super().__init__()
        self.receiver.start()
        self.receiver = receiver
        self.fullPayloadGetter = FullPayload(self.receiver)

    def run(self):
        print("running")
        self.threadActive = True
        # Mocks actual data coming from RFD
        while self.threadActive:
            time.sleep(0.1)
            payload = self.fullPayloadGetter.getData()
            if(payload != None):
                self.new_data.emit(payload)
        
