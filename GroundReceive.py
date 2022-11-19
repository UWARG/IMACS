
import struct
class GroundReceive():
    def init(self):
        pass

    def __decode(self, msg):

        # Flag
        if not msg[0] == b'\x7e'[0]:
            raise Exception('Invalid start byte')
        # msg[1] is length of bytes in message
        # msg[2] is type of msg
        if msg[1] is 1:
            return self.__movement_request(payload=msg[2:]) # this just returns null
        elif msg[2] is 2:
            return self.__relative_movement_command(payload=msg[2:])
        elif msg[2] is 7:
            return self.__decode_ground_station_data(payload=msg[2:])
        elif msg[2] is 8:
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
            # 'heading': struct.unpack()
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

    def receive(self):
        while True:
            # read from serial port and decode data
            pass
            

class AccessData():
    def init(self, msg, start_index=0):
        self.__index = start_index
        self.__msg = msg
        return

    def get_data(self, data_type):
        if data_type is "uint8_t":
            start_index = self.__index
            self.__index += 1
            # This is incorrect
            return self.__msg[start_index:self.__index]
        elif data_type is "f":
            length = 4
        elif data_type is "d":
            length = 8
        else:
            raise Exception("Invalid Datatype")
    
        start_index = self.__index
        self.__index += length
        return struct.unpack(data_type, self.__msg[start_index:self.__index])[0],
