import random

from structs import GroundStationData, SensorData

class GroundReceive():
    def __init__(self, ground_station_data=None, pid_set_response=None):
        self.payload = ground_station_data
        self.pid_set_response = pid_set_response

    def receive(self):
        raise Exception("deprecated -- use 'mock_receive' instead")
        # Mocks actual data coming from RFD
        # this is old, use the "mock_receive" function instead
        while True:
            if random.randint(0, 100000) == 1:
                TEST_PAYLOAD = {
                    'motor_outputs': [random.random() * 10 for i in range(0,12)],
                    'gps_data': {
                        'lat': random.random() * 10,
                        'lon': random.random() * 10,
                        'alt': random.random() * 10,
                    },
                    'climb_rate': random.random() * 10,
                    'track': random.random() * 10,
                    'heading': random.random() * 10,
                    'air_speed': random.random() * 10,
                    'ground_speed': random.random() * 10,
                    'imu_data': {
                        'yaw': random.random() * 10,
                        'pitch': random.random() * 10,
                        'roll': random.random() * 10,
                    },
                    'roll_rate': random.random() * 10,
                    'pitch_rate': random.random() * 10,
                    'yaw_rate': random.random() * 10,
                    'batery_voltages': [random.random() * 10 for i in range(0, 13)],
                    'pitch_rate': [random.random() * 10 for i in range(0, 13)],
                }
                print("new test payload", TEST_PAYLOAD)
                self.payload = TEST_PAYLOAD
    
    def __decode(self, driver_packet):
        if type(driver_packet) == GroundStationData:
            self.__decode_ground_station_data(driver_packet)
        elif type(driver_packet) == SensorData:
            self.__decode_sensor_data(driver_packet)
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
    def __decode_sensor_data(self, driver_packet):
        self.sensor_data_payload = {
            "flag": driver_packet.header.flag,
            "length": driver_packet.header.length,
            "latitude": driver_packet.header.latitude,
            "controller_number": driver_packet.controller_number,
            "controller": driver_packet.controller,
            "crc": driver_packet.crc,
        }

    def __gen_mock_packet(self):
        flag = random.randint(0, 1)
        if flag == 0:
            return GroundStationData()
        else: 
            return SensorData()

    def mock_receive(self):
        while True:
            if random.randint(0, 100000) == 1:
                mock_packet = self.__gen_mock_packet()
                self.__decode(mock_packet)

