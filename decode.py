TEST = ["7E | 00 19 | 10 | 01 | 00 13 A2 00 41 B1 6D 1C | FF FE | 00 | 00 | 53 45 4E 54 20 46 52 4F 4D 20 42 | D1"]

def decode(msg, BASE=16):

    #preprocess and partition raw string
    msg = msg.split('|')
    msg = [x.strip() for x in msg]
    msg = [x.split(' ') for x in msg]

    if msg[0][0] != '7E': return False #no start delimeter

    #length of message
    length = ''.join(msg[1])
    length = int(length, BASE)

    #other relevant info
    frame_type = msg[2][0]
    frame_id = msg[3][0]
    address_64_bit = msg[4][0]
    address_16_bit = msg[5][0]
    brodcast_radius = msg[6][0]
    options = msg[7][0]

    #decode bytes and return message content
    msg_content = bytes.fromhex(' '.join(msg[8]))
    msg_content = bytes.decode(msg_content)

    res = {
        'length': length,
        'frame_type': frame_type,
        'frame_id': frame_id,
        'address_64_bit': address_64_bit,
        'address_16_bit': address_16_bit,
        'brodcast_radius': brodcast_radius,
        'options': options,
        'msg_content': msg_content,
    }

    return res

__name__ = '__decode__'
if __name__ == '__decode__':
    for msg in TEST: print(decode(msg))

