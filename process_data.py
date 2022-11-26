FILENAME = "text_log.txt"

file = open(FILENAME, "r")

data = file.read()
data_arr = data.split("\n")

delete_list = []

for i in range(0, len(data_arr)):
    if data_arr[i][-2:] == "0a" or data_arr[i][-2:] == "0d" or data_arr[i][-2:] == ": ":
        delete_list.append(i)
    elif data_arr[i][-2:] == "30":
        data_arr[i] = data_arr[i][0:-2] + "00"


for i in range(0, len(delete_list)):
    data_arr.pop(delete_list[i] - i)

# look for start delimiters

found_delimiter = False
delimeter_start_index = 0

print("before while loop")
while not found_delimiter and delimeter_start_index < len(data_arr):
    # print("in while loop") # working
    fail = True
    if data_arr[delimeter_start_index][0:2] == "00":
        fail = False
        print("found shit")
        i = 14 + delimeter_start_index
        print("i", i)
        print("len(data_arr)", len(data_arr))
        while i <= len(data_arr):
            print("i: " + str(i))
            if data_arr[i][0:2] != "00":
                fail = True
                break
            print("adding i")
            i += 14
    if fail == False:
        found_delimiter = True
    else:
        delimeter_start_index += 1
        fail = False

print("delimeter_start_index: ", delimeter_start_index)
print("found_delimiter: ", found_delimiter)

            




print("data_arr: ", data_arr)