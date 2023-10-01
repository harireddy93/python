import array

def arra_insertion(arr,arr_index,arr_value):
    return arr.insert(arr_index,arr_value)

a = array.array("i",[1,2,3,4])

print(a)

arra_insertion(a,2,8)
print(a)