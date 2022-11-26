import math

FILENAME = "text_log.txt"

file = open(FILENAME, "r")

data = file.read()
data_arr = data.split("\n")
print(data_arr)

delete_list = []

processed_data = []

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
        byte = bytes(data_arr[i][-2:-1], 'utf-8')
        byte_string += byte


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
            print(processed_data[j * 16])
            print(processed_data[j * 16 + 1])
            print(processed_data[j * 16 + 2])
            if processed_data[j * 16] != b'0' and processed_data[j * 16 + 1] != b'0':
                print(processed_data[j * 16])
                print(processed_data[j * 16 + 1])
                fail = True
                found_delimeter = True
                break

print("found delimeter", found_delimeter)
print("start delimeter", start_delim)
