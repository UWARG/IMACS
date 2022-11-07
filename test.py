import pytest

from encode import encode
from decode import decode

@pytest.mark.parametrize(
    "test_message",
    [
        (
            {
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
        )
    ]
)
def test_encode_decode(test_message):
    encoded_message = encode(test_message)
    assert decode(encoded_message) == test_message

@pytest.mark.parametrize(
    "test_message",
    [
        (
            b'~\x00\x19\x10\x01\x00\x13\xa2\x00A\xb1m\x1c\xff\xfe\x00\x00\x01\x01\x01\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x00\x00\x80?\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\xd1'
        )
    ]
)
def test_decode_encode(test_message):
    decoded_message = decode(test_message)
    assert encode(decoded_message) == test_message
