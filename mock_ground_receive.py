import random
from AccessData import AccessData 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from structs import GroundStationData, SensorData, PIDValues, PIDController, GroundStationPIDSetResponse, Header

class GroundReceive(QThread):
    new_data = pyqtSignal(dict)
    def __init__(self, ground_station_data=None, pid_set_response=None):
        super(QThread, self).__init__()
        self.payload = ground_station_data
        self.pid_set_response = pid_set_response

    def receive(self):
        return self.mock_receive(self)
    
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
            'motor_outputs': [motor_outputs_retriever.get_data(data_type="B") for i in range(0, 12)], # list of 12 ints, motor page
            'gps_data': {
                'lat' : driver_packet.data.latitude, # double, map
                'lon' : driver_packet.data.longitude, # double, map
                'alt' : driver_packet.data.altitude, # float, home
            },  
            'climb_rate': driver_packet.data.climb_rate, # float, home
            'heading': driver_packet.data.heading, # float, home
            'air_speed': driver_packet.data.air_speed, # float, planning home
            'ground_speed': driver_packet.data.ground_speed, # float, home
            'imu_data':{
                'roll': driver_packet.data.roll, # float, home
                'pitch': driver_packet.data.pitch, # float, home
                'yaw': driver_packet.data.yaw, # float, not sure where
            },
            'roll_rate': driver_packet.data.roll_rate, # float , motor
            'pitch_rate': driver_packet.data.pitch_rate, # float , motor
            'yaw_rate': driver_packet.data.yaw_rate, # float , motor
            'battery_voltages': [battery_voltage_retirever.get_data(data_type="B") for i in range(0, 13)], # list of 13 ints, [0] is show in home
            'controller_voltages':  [controller_values_retriever.get_data(data_type="B") for i in range(0, 16)], # list of 16 ints, none
            'flag': AccessData(msg=driver_packet.header.flag, start_index=0).get_data(data_type="B"), # int, none
            'length': AccessData(msg=driver_packet.header.length, start_index=0).get_data(data_type="H"), # short, none
            'type': AccessData(msg=driver_packet.header.type, start_index=0).get_data(data_type="B"), # int, none
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
            sensor_data = SensorData(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0)
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

    def run(self):
        self.threadActive = True
        while self.threadActive:
            if random.randint(0, 1000000) == 1:
                mock_packet = self.__gen_mock_packet()
                self.__decode(mock_packet)
            if self.pid_set_response != None:
                print(self.pid_set_response)
            if self.payload != None:
                self.new_data.emit(self.payload)
        


