import serial

BAUDRATE = 9600
BYTE_SIZE = 8
TIMEOUT = 2

FILENAME = "text_log.txt"

file = open(FILENAME, "a")

rfd = serial.Serial(port="/dev/cu.usbmodem14101", baudrate=BAUDRATE, bytesize=BYTE_SIZE, timeout=TIMEOUT, stopbits=serial.STOPBITS_ONE)

while True:
    if rfd.read(1) == b'\x7e':
        file.write(rfd.read(6))

file.close()