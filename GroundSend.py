import struct

# must encode messages sent to air
class GroundSend():
    def init(self):
        pass

    # this method is equivalent to "payload_to_bytes()" method from Proof of Concept
    def __encode(self, payload):
        encoded_payload = b''
        for value in payload.values():
            if type(value) == dict:
                encoded_payload += self.__encode(value)
            elif type(value) == list:
                for v in value:
                    encoded_payload += self.__value_to_bytes(v)
            else:
                encoded_payload += self.__value_to_bytes(value)
        
        return encoded_payload

    def __value_to_bytes(self, value):
        if type(value) == float:
            return struct.pack('f', value)
        elif type(value) == int:
            return bytes([value])
        else:
            raise Exception('Unknown type')

    def send(self, payload):
        pass
        
