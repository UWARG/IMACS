class GenericCommsDevice():

    ser = None

    def __init__(self, port, baudrate):
        ser = serial.Serial(port=port, baudrate=baudrate, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)