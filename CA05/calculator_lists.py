##########################################
#       Calculator Functions
##########################################

# Function1: add two lists together
# each element of list1 will be added to the corresponding element of list2
def add_lists(list1, list2):
    return map(lambda x, y: x+y, list1, list2)

# Function2: subtract two lists
# each element of list2 will be subtracted from the corresponding element of list1
def subtract_lists(list1, list2):
    return map(lambda x, y: x-y, list1, list2)

# Function3: divide two lists
# each element of list1 will be divided by the corresponding element of list2
def divide_lists(list1,list2):
    return map(lambda x, y: x/float(y) if y!= 0 else 'nan', list1, list2)

# Function4a: original calculator function to multiply two numbers
def multiply(first, second):
    number_types = (int, long, float, complex)
    if isinstance(first, number_types) and isinstance(second, number_types):
        return first * second
    else:
         return 'error'
         
# Function4b: Adapt the above function to work with lists using Map
# each element of list1 will be multiplied by the corresponding element of list2
def multiply_list(list1, list2): 
    return map(multiply, list1, list2)

##########################################
#       Calls
##########################################

print add_lists([2,5,4],[2,3,0])
print subtract_lists([2,5,4,3],[2,3,0,4])
print divide_lists([1,2,3],[2,1,0])

print multiply_list([2,5,4,3],[2,3,0,4])
print multiply_list([2,5,4,3],['mary',3,0,4])

