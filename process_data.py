import math

FILENAME = "nov_27_test_2.txt"

file = open(FILENAME, "r")

data = file.read()
data_arr = data.split("\n")

delete_list = []
processed_data = []
missing_data = 0

# gonna try changing array in bytes
pd_index = 0
byte_string = b''
for i in range(0, len(data_arr)):
    if "b'\\r'" in data_arr[i]: # or "b'\\n'" in data_arr[i]:
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
length_of_data = 0
index_of_split = [0, 0, 0]
for i in range(0, len(processed_data) - 1):
    if processed_data[i] == b'0' and processed_data[i+1] == b'0':
        for j in range(i+1, math.floor((len(processed_data))/21)):
           
            if not processed_data[j*MULTIPLIER-1] == b'0' or not processed_data[j*MULTIPLIER] == b'0':
                if i == 36 or not i ==36:
                    print(processed_data[j*MULTIPLIER-40:j*MULTIPLIER+23])
                    print("at (i-1)*MULTIPLIER-1, (i-1)*MULTIPLIER, (i-1)*MULTIPLIER_1", processed_data[(j-1)*MULTIPLIER-1], processed_data[(j-1)*MULTIPLIER], processed_data[(j-1)*MULTIPLIER+1])
                    print("at i*MULTIPLIER-1, i*MULTIPLIER, i*MULTIPLIER+1: ", processed_data[j*MULTIPLIER-1], processed_data[j*MULTIPLIER], processed_data[j*MULTIPLIER+1])
                    print("at (i+1)*MULTIPLIER-1, (i+1)*MULTIPLIER, (i+1)*MULTIPLIER_1", processed_data[(j+1)*MULTIPLIER-1], processed_data[(j+1)*MULTIPLIER], processed_data[(j+1)*MULTIPLIER+1])
                    check_split = j*MULTIPLIER + i
                    if index_of_split[0] < check_split:
                        index_of_split[0] = check_split
                        index_of_split[1] = j
                        index_of_split[2] = i
                break
            else:
                if(j>2):
                    if i ==36:
                        print("check", processed_data[(j-1)*MULTIPLIER-1], processed_data[(j-1)*MULTIPLIER])
                if i == 36 or not i ==36:
                    length_of_data += 1
                    print("Stuff around:", processed_data[j*MULTIPLIER-3:j*MULTIPLIER+3])
                    print("actual stuff", processed_data[j*MULTIPLIER-1], processed_data[j*MULTIPLIER])
                    # print("good")
                    print("i", i)

print("length of data", length_of_data)
print("len(processed_data)/length_of_data", len(processed_data)/length_of_data )
print("len(processed_data)", len(processed_data))
print("index of split", index_of_split)

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



# start_index = 

# ok start at first one and see how many separate packets are sent and the length of each


# now find start delim then make array of tuples
found_delimeter = False
start_delim = 0
for i in range(0, len(processed_data) - 1):
    if processed_data[i] == b'0' and processed_data[i + 1] == b'0':
        found_delimeter = True
        start_delim = i
        fail = False
        for j in range(i, math.floor(len(processed_data)/16)):
            print("J: " + str(j))
            print(processed_data[j * 18])
            print(processed_data[j * 18 + 1])
            print(processed_data[j * 18 + 2])
            if processed_data[j * 18] != b'0' and processed_data[j * 18 + 1] != b'0':
                print(processed_data[j * 18])
                print(processed_data[j * 18 + 1])
                fail = True
                found_delimeter = True
                break

# # print("found delimeter", found_delimeter)
# # print("start delimeter", start_delim)
