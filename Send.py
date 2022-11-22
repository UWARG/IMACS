import struct

# must encode messages sent to air AND ground
# should not depend on state therefore all methods are static
class Send():
    def init(self):
        pass

    # this method is equivalent to "payload_to_bytes()" method from Proof of Concept
    @staticmethod
    def __encode(payload):
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
    
    @staticmethod
    def send(payload, type):
        encoded_payload = Send.__encode(payload)
        # should this include the length of bytes in info or entire frame?
        length = len(encoded_payload) # + 8 # 8 bytes for length and type and start and end 
        wrapped_payload = b'\x7e' + struct.pack("H", length) + struct.pack("B", type) + encoded_payload + b'\xd1' # last should be crc
        
        print("wrapped_payload")
        return wrapped_payload
        # should actually send payload thru rfds
        