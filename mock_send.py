import struct

class Send():
    @staticmethod
    def __encode(payload, type=None):
        encoded_payload = b''
        for value in payload.values():
            if type(value) == dict:
                encoded_payload += Send.__encode(value)
            elif type(value) == list:
                for v in value:
                    encoded_payload += Send.__value_to_bytes(v)
            else:
                encoded_payload += Send.__value_to_bytes(value)
        
        return encoded_payload

    @staticmethod
    def __value_to_bytes(value):
        if type(value) == float:
            return struct.pack('f', value)
        elif type(value) == int:
            return struct.pack("B", value)
        else:
            raise Exception('Unknown type')

    def send_gui_mock(self, payload, type):
        # for gui team to mock sending data from gui
        encoded_payload = Send.__encode(payload, type)
        length = len(encoded_payload) # + 8 # 8 bytes for length and type and start and end 
        wrapped_payload = b'\x7e' + struct.pack("H", length) + struct.pack("B", type) + encoded_payload + b'\xd1' # last should be crc
        print("Payload encoded and wrapped")
        return wrapped_payload
        
        