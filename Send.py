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
            return bytes(value)
        else:
            raise Exception('Unknown type')
    
    @staticmethod
    def send(payload):
        encoded_payload = Send.__encode(payload)
        print(encoded_payload)
        # should actually send payload thru rfds
        
