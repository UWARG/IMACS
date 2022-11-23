
import struct

from AccessData import AccessData

class GroundReceive():
    def __decode(self, msg):
        if not msg[0] == b'\x7e'[0]:
            pass
        if msg[3] == 0:
            return self.__odometry_data(msg[4:])
        elif msg[2] == 1:
            return self.__movement_request(payload=msg[4:]) # this just returns null
        else: 
            raise Exception('Unknown payload type')

    def __odometry_data(self, payload):
        # [ 0 ] [ Sf → TM → Jetson ] Odometry Data 
        data_retriever = AccessData(msg=payload, start_index=0)
        decoded_payload = {
            "gps_data": {
                "lat": data_retriever.get_data(data_type="f"),
                "lon": data_retriever.get_data(data_type="f"),
                "alt": data_retriever.get_data(data_type="d"),
            },
            "climb_rate": data_retriever.get_data(data_type="f"),
            "heading": struct.unpack(data_type="f"),
            "air_speed": data_retriever.get_data(data_type="f"),
            "ground_speed": data_retriever.get_data(data_type="f"),
            "imu_data": {
                "yaw": data_retriever.get_data(data_type="f"),
                "pitch": data_retriever.get_data(data_type="f"),
                "roll": data_retriever.get_data(data_type="f"),
            },
            "roll_rate": data_retriever.get_data(data_type="f"),
            "pitch_rate": data_retriever.get_data(data_type="f"),
            "yaw_rate": data_retriever.get_data(data_type="f"),
        }

        return decoded_payload

    def __movement_request(self, payload):
        # [ 1 ] [ PM → SM → TM → Jetson ] MovementRequest 
        return None
    
    def receive(self):
        PLACEHOLDER = b'~\x00\x19\x10\x01\x00\x13\xa2\x00A\xb1m\x1c\xff\xfe\x00\x00\x01\x01\x01\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\xd1' 
        while True:
            # PLACEHOLDER should read from serial port and decode data
            self.paload = self.__decode(PLACEHOLDER)
            pass
            
