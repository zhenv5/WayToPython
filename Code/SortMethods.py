
def insert_sort(lists):
    for i in range(1,len(lists)):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j], lists[j+1] = key, lists[j]
            j -= 1
    # lists is a mutable variable, has been changed
    return lists

def quicksort(array):
    """
    quick sort with Python
    """
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


array = [-1,2,98,23,4,12,2,434,45,12,34,2323]
#print quicksort(array)
insert_sort(array)
print array
