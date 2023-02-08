import struct

class AccessData():
    def __init__(self, msg, start_index=0):
        self.__index = start_index
        self.__msg = msg
        return

    def get_data(self, data_type):
        if data_type == "B":
            length = 1
        elif data_type == "f":
            length = 4
        elif data_type == "H":
            length = 2
        elif data_type == "d":
            length = 8
        else:
            raise Exception("Invalid Datatype")
    
        start_index = self.__index
        self.__index += length
        unpacked_data = struct.unpack(data_type, self.__msg[start_index:self.__index])[0]
        return unpacked_data

