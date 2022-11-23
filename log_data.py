import logging
import serial

BAUDRATE = 9600
BYTE_SIZE = 8
TIMEOUT = 2

logging.basicConfig(filename="log.txt", level=logging.DEBUG)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

rfd = serial.Serial(port="/dev/cu.usbmodem14101", baudrate=BAUDRATE, bytesize=BYTE_SIZE, timeout=TIMEOUT, stopbits=serial.STOPBITS_ONE)

while True:
    if rfd.read(1) == b'\x7e':
        logging.info(rfd.read(6))