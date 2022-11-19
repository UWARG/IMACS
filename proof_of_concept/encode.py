import struct

AIR_GROUND_PAYLOAD_TEST_MESSAGE = {
    'time': 1,
    'payload_type': 1,
    'crc': 1,
    'gps_data': {
        'lat': 1.0,
        'lon': 1.0,
        'alt': 1.0,
    },
    'imu_data': {
        'yaw': 1.0,
        'pitch': 1.0,
        'roll': 1.0,
    },
    'motor_outputs': [1,2,3,4,5,6,7,8,9,10,11,12]
}

def encode(msg):

    encoded_msg = payload_to_bytes(msg)
    res = b'\x7e\x00\x19\x10\x01\x00\x13\xa2\x00\x41\xb1\x6d\x1c\xff\xfe\x00\x00' + encoded_msg + b'\xd1'

    return res

def payload_to_bytes(payload):
    encoded_payload = b''
    for value in payload.values():
        if type(value) == dict:
            encoded_payload += payload_to_bytes(value)
        elif type(value) == list:
            for v in value:
                encoded_payload += value_to_bytes(v)
        else:
            encoded_payload += value_to_bytes(value)
       
    return encoded_payload

def value_to_bytes(value):
    if type(value) == float:
        return struct.pack('<f', value)
    elif type(value) == int:
        return bytes([value])
    else:
        raise Exception('Unknown type')

if __name__ == '__main__':
    print("ENCODED MESSAGE", encode(AIR_GROUND_PAYLOAD_TEST_MESSAGE))