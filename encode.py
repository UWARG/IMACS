import binascii

TEST = ['SENT FROM B']

def encode(msg):

    encoded_msg = binascii.hexlify(b'SENT FROM B')
    encoded_msg = str(encoded_msg, 'ascii')
    encoded_msg = encoded_msg.upper()

    res = []
    for x in encoded_msg: 
        if not res or len(res[-1])==2: res += [x]
        else: res[-1] += x

    return ' '.join(res)

__name__ = '__encode__'
if __name__ == '__encode__':
    for msg in TEST: print(encode(msg))