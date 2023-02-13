#need to install libscrc using pip
#can check the library is working by
#python -m libscrc.testcrc64
#python -m libscrc.testmodbus
import libscrc

crc32 =libscrc.crc32(b'1234')

print(crc32)

