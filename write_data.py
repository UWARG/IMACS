# ls -l /dev/cu.usb*

import serial
import calendar
import time

BAUDRATE = 115200
BYTE_SIZE = 8
TIMEOUT = 2

FILENAME = "text_log.txt"
PORT = "/dev/cu.usbmodem14101"

file = open(FILENAME, "a")

rfd = serial.Serial(port=PORT, baudrate=BAUDRATE, bytesize=BYTE_SIZE, timeout=TIMEOUT, stopbits=serial.STOPBITS_ONE)



while True:
    timestamp = calendar.timegm(time.gmtime())
    first_hex = rfd.read(2).hex()
    second_hex = rfd.read(2).hex()

    file.write(str(timestamp) + ": " + str(first_hex) + " " + str(second_hex) + "\n")
    print(str(first_hex) + " " + str(second_hex))

file.close()

# later, code should do file comparisons