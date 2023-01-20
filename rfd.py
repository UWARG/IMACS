import serial

class GenericCommsDevice():

    ser = None

    def __init__(self, port, baudrate):
        ser = serial.Serial(port=port, baudrate=baudrate, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

    def write(byteA)




rfd = serial.Serial(port="COM7", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
rfd2 = serial.Serial(port="COM6", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

while(True):
    data = [0x7e]
    print("byte sent",data[0].hex())
    rfd2.write(bytearray(data))

    readByte = rfd.read()
    print("byte read",readByte.hex())