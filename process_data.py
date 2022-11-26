FILENAME = "text_log.txt"

file = open(FILENAME, "r")

data = file.read()
data_arr = data.split("\n")
print(data_arr)

delete_list = []

for i in range(0, len(data_arr)):
    if "b'\\r'" in data_arr[i] or "b'\\n'" in data_arr[i]:
        delete_list.append(i)

print("data_arr: ", data_arr)
print("delete_list: ", delete_list)
for i in range(0, len(delete_list)):
    data_arr.pop(delete_list[i] - i)

# look for start delimiters

found_delimiter = False
delimeter_start_index = 0

print("data_arr: ", data_arr)

print("before while loop")
while not found_delimiter and delimeter_start_index < len(data_arr) - 1:
    # print("in while loop") # working
    fail = True
    if data_arr[delimeter_start_index][0:2] == "00" and data_arr[delimeter_start_index + 1][0:2] == "00":
        fail = False
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