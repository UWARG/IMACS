import libscrc


class GenericCommsDevice():

    def __init__(self, port, baudrate):
        self.ser = serial.Serial(port=port, baudrate=baudrate, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

    def checkCRC(self, b):
        return libscrc.crc32(b)

    def transmit(b):
        ser.write(b)
    def recieve():
        
        readByte = rfd.read()
        if readByte == 0x7e:
            # start of new message
            
        self.currentMessage.append(readByte)
        
        