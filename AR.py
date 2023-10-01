import array
"""Insert an element into an array to which ever index we need to insert"""
def arra_insertion(arr,arr_index,arr_value):
    return arr.insert(arr_index,arr_value)

a = array.array("i",[1,2,3,4])

"""
Time Complexty : O(n) ( Amount of time taken depends on the array length)
Space complexity  : O(1) ( Amount of space taken in memory only one space is allocated for the array inserted value)
"""

print(a)

arra_insertion(a,2,8)
print(a)


"""
TRAVERSAL OF AN ARRAY
"""

def traversal_array(arr):
    for i in arr:
        print(i)

traversal_array(a)

#print("traversal array : \n  {}".format(traversal_array(a)))

"""
Time Complexty : O(n) ( Amount of time taken depends on the array length)
Space complexity  : O(1) ( Amount of space taken in memory is constant since it always prints)
"""

# Accessing element 
def accessing_element_arr(arr,index):
    if(index >= len(arr)):
        return "Index mentioned as input is out of scope"
    else:
        return arr[index]
    
print("Accessing element : {}".format(accessing_element_arr(a,4) ))


"""
Time Complexty : O(1) ( Amount of time taken is constant as there is no loop)
Space complexity  : O(1) ( Amount of space taken in memory is constant since it always prints)
"""


#SEARCHING AN ELEMENT IN ARRAY

def search_arr(arr,value):
    for i in arr: # this will give you the values in array
        if (i == value):
            return 200
    return -1 # this is kind of edge case handling 

if(search_arr(a,9) == 200):
     print("Element exists")
else:
    print("Element does not exists")

print("Search of an element in array : {}".format(search_arr(a,9) ) )


"""
Time Complexty : O(n) ( Amount of time taken is based on index where the target value is present)
Space complexity  : O(1) ( Amount of space taken in memory is constant since it always prints)
"""


# Deleting an element in array 

print(a)

def delete_element(arr,value):
    if(search_arr(arr,value) == 200):
        arr.remove(value) # This removes  the value are reorders the index from successor indexes 
        return "{} elment has been removed".format(value)
    else:
        return "{} is not present in the array return block".format(value)

    
    

print(delete_element(a,9) )

#print("delete element: ".format(delete_element(a,9)) )

print(a)

"""
Time Complexty : O(n) ( Amount of time taken is based on index where the target value is present and also length of the array as well)
Space complexity  : O(1) ( Amount of space taken in memory is constant since it always prints)
"""



    







