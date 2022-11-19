import struct

TEST = b'~\x00\x19\x10\x01\x00\x13\xa2\x00A\xb1m\x1c\xff\xfe\x00\x00\x01\x01\x01\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\xd1' 

def decode(msg):
    if not msg[0] == b'\x7e'[0]:
        raise Exception('Invalid start byte')
    
    # Transit frame decoding not yet implemented

    # Start of payload
    if msg[17] == 1:
        return air_ground_payload(msg[17:])
    else:
        raise Exception('Unknown payload type')

def air_ground_payload(encoded_payload):

    print(encoded_payload[27:])
    # print(struct.unpack('<f', encoded_payload[17:-1]))

    decoded_payload = {
        'time': encoded_payload[0],
        'payload_type': encoded_payload[1],
        'crc': encoded_payload[2],
        'gps_data': {
            'lat': struct.unpack('<f', encoded_payload[3:7])[0],
            'lon': struct.unpack('<f', encoded_payload[7:11])[0],
            'alt': struct.unpack('<f', encoded_payload[11:15])[0],
        },
        'imu_data': {
            'yaw': struct.unpack('<f', encoded_payload[15:19])[0],
            'pitch': struct.unpack('<f', encoded_payload[19:23])[0],
            'roll': struct.unpack('<f', encoded_payload[23:27])[0],
        },
        'motor_outputs': [encoded_payload[i] for i in range(27,39)] 
    }
    return decoded_payload

if __name__ == '__main__':
    print("DECODED MESSAGE:", decode(TEST))
