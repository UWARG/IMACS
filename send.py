import libscrc

def prep_crc(input_bytes) -> int:
    crc32 = libscrc.crc32(input_bytes)
    return crc32

def test_crc():
    test_cases = bytearray([0XFF, 0X11])
    print(".bss section")
    for value in test_cases:
        print(hex(value))
    crc_byte_array = bytearray((prep_crc(test_cases)).to_bytes(4,'big'))
    print("crc section")
    for value in crc_byte_array:
        print(hex(value))
    print("merge together")
    test_cases += (crc_byte_array)
    for value in test_cases:
        print(hex(value))

test_crc()
