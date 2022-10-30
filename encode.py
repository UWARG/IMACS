import binascii

TEST = ['SENT FROM B']

def encode(msg):

    encoded_msg = binascii.hexlify(b'SENT FROM B')
    encoded_msg = str(encoded_msg, 'ascii')
    encoded_msg = encoded_msg.upper()

    msg_str = []
    for x in encoded_msg: 
        if not msg_str or len(msg_str[-1])==2: msg_str += [x]
        else: msg_str[-1] += x
    msg_str = ' '.join(msg_str)

    res = ['7E','00 19','10','01','00 13 A2 00 41 B1 6D 1C','FF FE', '00', '00', msg_str, 'D1'] #note: other properties currently harcoded

    return ' | '.join(res)

__name__ = '__encode__'
if __name__ == '__encode__':
    for msg in TEST: print(encode(msg))