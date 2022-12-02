# ls -l /dev/cu.usb*
import sys
import serial
import calendar
import time

BAUDRATE = 115200
BYTE_SIZE = 8
TIMEOUT = 2

FILENAME = "nov_27_test_2.txt"
PORT = "/dev/cu.usbmodem14101"

file = open(FILENAME, "a")

rfd = serial.Serial(port=PORT, baudrate=BAUDRATE, bytesize=BYTE_SIZE, timeout=TIMEOUT, stopbits=serial.STOPBITS_ONE)


while True:
    if __name__ == "__main__":
        try:
            timestamp = calendar.timegm(time.gmtime())
            info_pack = str(rfd.read(1))
            # info_pack = info_pack[2:-1]
            # info_pack = str(info_pack).replace("00", "")  # remove delimeter      

            file.write(str(timestamp) + ": " + info_pack + "\n")
            print(info_pack)
        except KeyboardInterrupt:
            print("\nExiting script...")
            file.close()
            sys.exit()
    


# later, code should do file comparisons