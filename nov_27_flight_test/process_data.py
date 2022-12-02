import math

FILENAME = "nov_27_test_2.txt"
file = open(FILENAME, "r")


data = file.read()
data_arr = data.split("\n")

delete_list = []
processed_data = []
missing_data = 0

pd_index = 0
byte_string = b''
for i in range(0, len(data_arr)):
    if "b'\\r'" in data_arr[i]:
        processed_data.append(byte_string)
        pd_index += 1
        delete_list.append( "\"" + str(i) + "\"")
        byte_string = b''
    elif "b'\\n'" in data_arr[i]:
        pass
    else:
        if data_arr[i][-3:] == "b''":
            missing_data += 1
        byte = bytes(data_arr[i][-2:-1], 'utf-8')
        byte_string += byte


MULTIPLIER = 19
payloads = {} # key is the start index, value is payload length
checked = []
index_of_split = [0, 0, 0]
for i in range(1, len(processed_data)):
    if processed_data[i-1] == b'0' and processed_data[i] == b'0':
        msg_length = 1
        for j in range(i, math.floor((len(processed_data))/21)):
            if (i) in checked:
                continue
            if not processed_data[j*MULTIPLIER-2] == b'0' or not processed_data[j*MULTIPLIER-1] == b'0':
                if msg_length > 1:
                    payloads[str(i)] = msg_length
                msg_length = 1
                break
            else:
                checked.append(i+j)
                msg_length += 1

print("payloads_sequences", payloads)
                

import matplotlib.pyplot as plt

def plot_empty(data_arr):
    x = []
    y = []
    # dont hard code this lol
    START_TIME = 1669572416
    END_TIME = 1669573549
    empty_bytes_count = 0
    empty = []
    for i in range(0, len(data_arr)):
        if str(b'') in data_arr[i]:
            empty_bytes_count += 1
            empty.append(1)
            split = data_arr[i].split(":")
            if split in x:
                print("already here")
                y[x.index(split[0])] += 1
            else:
                x.append(split[0])
                y.append(1)
        else:
            empty.append(0)

    print("Number of empty bytes:", empty_bytes_count)
    print("Number of bytes received", len(data_arr))
    print("Time interval (s):", END_TIME - START_TIME)
    print("Time interval (min):", round((END_TIME - START_TIME)/60, 2))
    print("Bytes per second:", len(data_arr)/(END_TIME - START_TIME))
    print("Empty bytes per second:", round(empty_bytes_count/((END_TIME - START_TIME)), 2))
    print("Empty bytes per minute:", round(empty_bytes_count/((END_TIME - START_TIME)/60),2))
    print(len(x))
    
    # print("shape of empty", len(empty), len(i in range(0, len(data_arr))))
    plt.ylim([0.5, 1.5])
    plt.locator_params(axis='x', nbins=5)
    plt.locator_params(axis='y', nbins=1)
    plt.scatter(range(0, len(data_arr)), empty)
    plt.show()

plot_empty(data_arr)


