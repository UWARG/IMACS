import random

from structs import GroundStationData, SensorData, PIDValues, PIDController, GroundStationPIDSetResponse, Header

class GroundReceive():
    def __init__(self, ground_station_data=None, pid_set_response=None):
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
        self.payload = {
            'motor_outputs' : driver_packet.motor_outputs,
            'gps_data': {
                'Latitude' : driver_packet.data.latitude,
                'Longitude' : driver_packet.data.longitude,
                'Altitude' : driver_packet.data.altitude,
            },  
            'climb_rate': driver_packet.data.climb_rate,
            'track': None,
            'heading': driver_packet.data.heading,
            'air_speed': driver_packet.data.air_speed,
            'ground_Speed': driver_packet.data.ground_speed,
            'imu_data':{
                'roll': driver_packet.data.roll,
                'pitch': driver_packet.data.pitch,
                'yaw': driver_packet.data.yaw,
            },
            'roll_rate': driver_packet.data.roll_rate,
            'pitch_rate': driver_packet.data.pitch_rate,
            'yaw_rate': driver_packet.data.yaw_rate,
            'Battery_Voltages': driver_packet.battery_voltages,
            'Controller_Values':  driver_packet.controller_values,
        }
    def __decode_pid_set_response(self, driver_packet):
        self.ground_station_pid_set_response_payload = {
            "flag": driver_packet.header.flag,
            "length": driver_packet.header.length,
            "type": driver_packet.header.type,
            "controller_number": driver_packet.controller_number,
            "controller": [ {"P": driver_packet.controller.axes[i].P, "I": driver_packet.controller.axes[i].I, "D": driver_packet.controller.axes[i].D } for i in range(0,6)],
            "crc": driver_packet.crc,
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

    def mock_receive(self):
        while True:
            if random.randint(0, 1000000) == 1:
                mock_packet = self.__gen_mock_packet()
                self.__decode(mock_packet)
                print(self.ground_station_pid_set_response_payload)
                print(self.payload)
        


