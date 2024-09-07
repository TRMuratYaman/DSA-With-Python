
# Arrays are actually defined through a list data structure in Python .

# accessing value of an array.
arr = [1,2,3]
print(arr[0])
print(arr[2])

if 1 in arr: print(True)

for i in arr:
    if arr == 1:
        print(True)
    break

# adding value into an array.
num_arr = [4, 5, 6]
num_arr.insert(1, 7) #  insert() method adds only a single element to the list and inserts it at a specific position.
print(num_arr)
num_arr.append(8) # append() method adds a list as a single element to the list
print(num_arr)
num_arr.extend([9, 10]) # extend() method extends the list, that is, appends each element individually to the end of the existing list.
print(num_arr)

# removing value from an array
num_arr.remove(4)
print(num_arr)

