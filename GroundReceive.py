
import struct

from AccessData import AccessData

class GroundReceive():
    def init(self):
        # could define an initial payload if wanted - idk lol
        pass

    def __decode(self, msg):

        # Flag
        if not msg[0] == b'\x7e'[0]:
            pass
        # msg[1 to 4] is length of bytes in message
        # msg[5] is type of msg
        print("msg[0]", msg[0])
        print("msg[1]", msg[1])
        print("msg[2]", msg[2])
        print("msg[3]", msg[3])
        print("msg[4]", msg[4])
        print("msg[5]", msg[5])
        print("msg[6]", msg[6])
        print("msg[7]", msg[7])

        if msg[3] == 1:
            return self.__movement_request(payload=msg[3:]) # this just returns null
        elif msg[3] == 2:
            return self.__relative_movement_command(payload=msg[3:])
        elif msg[3] == 7:
            return self.__decode_ground_station_data(payload=msg[3:])
        elif msg[3] == 8:
            return "payload type 2"
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
    
    def relative_movement_command(self, payload): #temporary public method for testing
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
            # Motor Outputs [ uint8_t ] x 12
            'motor_outputs': [data_retriever.get_data(data_type="uint8_t") for i in range(0,12)],
            'gps_data': {
                'lat': data_retriever.get_data(data_type="f"),
                'lon': data_retriever.get_data(data_type="f"),
                'alt': data_retriever.get_data(data_type="d"),
            },
            # climb rate [float]
            'climb_rate': data_retriever.get_data(data_type="f"),
            # track [float]
            'track': data_retriever.get_data(data_type="f"),
            # heading [heading] 
            'heading': struct.unpack(data_type="f"),
            # air speed [float]
            'air_speed': data_retriever.get_data(data_type="f"),
            # ground speed [float]
            'ground_speed': data_retriever.get_data(data_type="f"),
            'imu_data': {
                # roll [float]
                # pitch [float]
                # yaw [float]
                'yaw': data_retriever.get_data(data_type="f"),
                'pitch': data_retriever.get_data(data_type="f"),
                'roll': data_retriever.get_data(data_type="f"),
            },
            # roll rate [float]
            'roll_rate': data_retriever.get_data(data_type="f"),
            # pitch rate [float]
            'pitch_rate': data_retriever.get_data(data_type="f"),
            # yaw rate [float]
            'yaw_rate': data_retriever.get_data(data_type="f"),
            # Battery Voltages [uint8_t] x 13 
            'batery_voltages': [data_retriever.get_data(data_type="uint8_t") for i in range(0, 13)],
            # Note: the first value is the overall voltage
            # The value is a value between 0 and 200 where 0 is 3V and 200 is 5V
            # Controller Values [uint8_t] x 16
            'pitch_rate': [data_retriever.get_data(data_type="uint8_t") for i in range(0, 13)],
        }
        return decoded_payload

    def test_receive(self, msg):
        # allows calling __decode method for testing purposes
        return self.__decode(msg)

    def receive(self):
        PLACEHOLDER = b'~\x00\x19\x10\x01\x00\x13\xa2\x00A\xb1m\x1c\xff\xfe\x00\x00\x01\x01\x01\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\xd1' 
        while True:
            # PLACEHOLDER should read from serial port and decode data
            self.paload = self.__decode(PLACEHOLDER)
            pass