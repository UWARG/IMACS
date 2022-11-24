import struct
import serial
import random # just for mock for gui team

from AccessData import AccessData

PORT = "/dev/cu.usbmodem14101"
BAUDRATE = 9600
BYTE_SIZE = 8
TIMEOUT = 2

class GroundReceive():
    def __init__(self, port=PORT, baudrate=BAUDRATE, byte_size=BYTE_SIZE, timeout=TIMEOUT, stopbits=serial.STOPBITS_ONE):
        self.rfd = "should be set to serial port" # serial.Serial(port=port, baudrate=baudrate, bytesize=byte_size, timeout=timeout, stopbits=stopbits)

    def __decode(self, msg):
        if not msg[0] == b'\x7e'[0]:
            pass
        if msg[3] == 1:
            return self.__movement_request(payload=msg[4:]) # this just returns null
        elif msg[3] == 2:
            return self.__relative_movement_command(payload=msg[4:])
        elif msg[3] == 7:
            return self.__decode_ground_station_data(payload=msg[4:])
        else: 
            raise Exception('Unknown payload type')

    def __movement_request(self, payload):
        # [ 1 ] [ PM → SM → TM → Jetson ] MovementRequest 
        return None
    
    def __relative_movement_command(self, payload):
        # [ 2 ] [ Jetson → TM → SM → PM ] RelativeMovementCommand 
        data_retriever = AccessData(msg=payload, start_index=0)
        decoded_payload = {
            "x": data_retriever.get_data(data_type="f"),
            "y": data_retriever.get_data(data_type="f"),
            "z": data_retriever.get_data(data_type="f"),
            "heading": data_retriever.get_data(data_type="f"),
        }

        return decoded_payload
    
    def __relative_movement_command(self, payload): #temporary public method for testing
        # [ 2 ] [ Jetson → TM → SM → PM ] RelativeMovementCommand 
        data_retriever = AccessData(msg=payload, start_index=0)
        decoded_payload = {
            "x": data_retriever.get_data(data_type="f"),
            "y": data_retriever.get_data(data_type="f"),
            "z": data_retriever.get_data(data_type="f"),
            "heading": data_retriever.get_data(data_type="f"),
        }

        return decoded_payload


    def __decode_ground_station_data(self, payload):       
        # [ 7 ] [ AM → SM → TM → GSPC ] Ground Station Data
        data_retriever = AccessData(msg=payload, start_index=0)
        decoded_payload = {
            'motor_outputs': [data_retriever.get_data(data_type="uint8_t") for i in range(0,12)],
            'gps_data': {
                'lat': data_retriever.get_data(data_type="f"),
                'lon': data_retriever.get_data(data_type="f"),
                'alt': data_retriever.get_data(data_type="d"),
            },
            'climb_rate': data_retriever.get_data(data_type="f"),
            'track': data_retriever.get_data(data_type="f"),
            'heading': struct.unpack(data_type="f"),
            'air_speed': data_retriever.get_data(data_type="f"),
            'ground_speed': data_retriever.get_data(data_type="f"),
            'imu_data': {
                'yaw': data_retriever.get_data(data_type="f"),
                'pitch': data_retriever.get_data(data_type="f"),
                'roll': data_retriever.get_data(data_type="f"),
            },
            'roll_rate': data_retriever.get_data(data_type="f"),
            'pitch_rate': data_retriever.get_data(data_type="f"),
            'yaw_rate': data_retriever.get_data(data_type="f"),
            'batery_voltages': [data_retriever.get_data(data_type="uint8_t") for i in range(0, 13)],
            'pitch_rate': [data_retriever.get_data(data_type="uint8_t") for i in range(0, 13)],
        }
        return decoded_payload

    def receive_mock_gui(self):
        # Mocks actual data coming from RFD
        while True:
            if random.randint(0, 100000) == 1:
                TEST_PAYLOAD = {
                    "x": random.random() * 10,
                    "y": random.random() * 10,
                    "z": random.random() * 10,
                    "heading": random.random() * 10,
                }
                print("new test payload", TEST_PAYLOAD)
                self.payload = TEST_PAYLOAD

    def test_receive(self, msg):
        # allows calling __decode method for testing purposes
        return self.__decode(msg)

    def receive(self):
        while True:
            if self.rfd.read(1) == b'\x7e'[0]:
                length_in_bytes = self.rfd.read(4)
                byte_string = b'\x7e' + length_in_bytes
                length = struct.unpack('I', length_in_bytes)[0]
                
                for i in range(0, length + 1):
                    byte_string += self.rfd.read(1)
                self.payload = self.__decode(byte_string)

