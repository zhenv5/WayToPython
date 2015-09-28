"""
quick sort with Python
"""
def quicksort(array):
    less = []
    greater = []
    if len(array) == 1 or len(array) == 0:
        return array
    pivort = array.pop()
    for item in array:
        if item <= pivort:
            less.append(item)
        else:
            greater.append(item)
    return quicksort(less) + [pivort] + quicksort(greater)


array = [-1,2,4,12,2,434,45,12,34,2323]
print quicksort(array)
