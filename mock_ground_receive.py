import random
from AccessData import AccessData 
from rfd_driver.generic_comms_device import GenericCommsDevice
from rfd_driver.TelemMessages.GroundStationData import GroundStationData
from rfd_driver.TelemMessages.GroundStationPIDSetResponse import GroundStationPIDSetResponse


class GroundReceive():
    def __init__(self, ground_station_data=None, pid_set_response=None, port="/dev/ttyUSB0", baudrate=115200):
        self.payload = ground_station_data
        self.pid_set_response = pid_set_response
        self.receiver = GenericCommsDevice(port=port, baudrate=baudrate)

    def receive(self):
        while True:
            self.__decode(self.receiver.receive())
    
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
