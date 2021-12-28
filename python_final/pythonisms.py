from time import time

def add_2(arr) :
    """
    this function tackes array as input and add 2 to each element of the array 
    output -> arr with increase 2 in each element
    """
    arr2 = []
    for item in arr :
        arr2.append(item+2)
    return arr2

def timer (function):
    t1 = time()
    function()
    t2 = time()
    execution_time = t2-t1
    print (f"this function takes {execution_time:.4f}s")


def convert_to (arr , to_type):
    """
    this function covert array to other data type 
    input -> arr = list , to_type = "set", "str"
    """

    if to_type == "str":
        arr = str(arr)
    if to_type == "set":
        arr= set(arr)
    return arr


if __name__ == "__main__":
    arr =convert_to(arr=[1,2,3,4,5], to_type="set")
    print (arr)
    arr = add_2([1,2,3,4,5])
    print(arr)
    print("______________")
    @timer
    def print_from_0_10():
        for i in range(11):
            print (i )
    print("______________")
    string = "bla bla bla"
    print ("string_length: ",string.__len__())
    print()