import threading

import time

import random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from AccessData import AccessData 
from MockStructs import PIDValues, GroundStationData, PIDController, GroundStationPIDSetResponse, GroundStationData, Header, SensorData


class MockGroundReceiveWorker():
    def __init__(self, ground_station_data=None, pid_set_response=None):
        self.payload = ground_station_data
        self.pid_set_response = pid_set_response
        self.lock = threading.Lock()
        self.is_running = False
    
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
                'lat' : 5,#driver_packet.data.latitude, # double
                'lon' : driver_packet.data.longitude, # double
                'alt' : random.randint(0,12), #driver_packet.data.altitude, # float
            },  
            'climb_rate': driver_packet.data.climb_rate, # float
            'heading': driver_packet.data.heading, # float
            'air_speed': driver_packet.data.air_speed, # float
            'ground_speed': driver_packet.data.ground_speed, # float
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
            
            ### this is header stuff:
            'flag': AccessData(msg=driver_packet.header.flag, start_index=0).get_data(data_type="B"), # int
            'length': AccessData(msg=driver_packet.header.length, start_index=0).get_data(data_type="H"), # short
            'type': AccessData(msg=driver_packet.header.type, start_index=0).get_data(data_type="B"), # int
        }

    def __decode_pid_set_response(self, driver_packet):
        self.pid_set_response = {
            "flag": AccessData(msg=driver_packet.header.flag, start_index=0).get_data(data_type="B"), # int
            "length": AccessData(msg=driver_packet.header.length, start_index=0).get_data(data_type="H"), # short
            "type": AccessData(msg=driver_packet.header.type, start_index=0).get_data(data_type="B"), # int
            "controller_number": AccessData(msg=driver_packet.controller_number, start_index=0).get_data(data_type="B"), # int
            "controller": [  # list of 6 dicts each with three floats (P, I, D)
                    {
                        "P": driver_packet.controller.axes[i].P, 
                        "I": driver_packet.controller.axes[i].I, 
                        "D": driver_packet.controller.axes[i].D 
                    } for i in range(0,6)
                ],
            "crc": AccessData(msg=driver_packet.crc, start_index=0).get_data(data_type="f"), # float
        }

    def __gen_mock_packet(self):
        if random.randint(0,1) == 1:
            header = Header(b'\x00', b'\x00\x01', b'\x01')
            sensor_data = SensorData(random.randint(0,12), random.randint(0,12), random.randint(0,12), random.randint(0,12), random.randint(0,12), random.randint(0,12), 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0)
            motor_outputs = b'\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01'
            battery_voltages = b'\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00'
            controller_values = b'\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01'
            crc = b'\x00\x01\x00\x01\x00\x01'
            return GroundStationData(header=header, motor_outputs=motor_outputs, data=sensor_data, battery_voltages=battery_voltages, controller_values=controller_values, crc=crc)
        else: 
            header = Header(b'\x00', b'\x00\x01', b'\x01')
            controller_number = b'\x00'
            crc = b'\x00\x01\x00\x01\x00\x01'
            pid_values = [PIDValues(1.0 + i, 2.0 + i, 3.0 + i) for i in range(0, 6)]
            controller = PIDController(pid_values)
            return GroundStationPIDSetResponse(header, controller_number, controller, crc)
        
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
        
    def getMotorInfo(self):
        if self.payload is None:
            return None
        else:
            return self.payload["motor_outputs"]
        
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
        
    def getThrottleInfo(self):
        if self.payload is None:
            return None
        else:
            return self.payload["throttle"]
        
    def getFullPayload(self):
        if self.payload is None:
            return None
        else:
            return self.payload
        

    def receive(self):
        while self.is_running:
            time.sleep(0.1)
            mock_packet = self.__gen_mock_packet()
            self.__decode(mock_packet)

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

def test_data_getter_classes():
    """
    run `python MockGroundReceive.py` to test these classes
    """
    receiver = MockGroundReceiveWorker()
    receiver.start()
    imuDataGetter = IMUData(receiver)
    rotationInfoGetter = RotationInfo(receiver)
    batterVoltageGetter = BatteryVoltages(receiver)
    throttleInfoGetter = ThrottleInfo(receiver)
    coordinatesGetter = Coordinates(receiver)
    droneInfoGetter = DroneInfo(receiver)

    while True:
        print(imuDataGetter.getData())
        print(rotationInfoGetter.getData())
        print(rotationInfoGetter.getData())
        print(batterVoltageGetter.getData())
        print(throttleInfoGetter.getData())
        print(coordinatesGetter.getData())
        print(droneInfoGetter.getData())

        time.sleep(0.1)

if __name__ == "__main__":
    test_data_getter_classes()

class GroundReceive(QThread):
    """
    replace "from ground_receive import GroundReceive" with "from MockGroundReceive import GroundReceive" to run gui with mock driver
    """
    new_data = pyqtSignal(dict)
    receiver = MockGroundReceiveWorker()
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
        

