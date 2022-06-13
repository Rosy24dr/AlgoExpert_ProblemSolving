def find_minimum(array):
    minimum = array[0]

    for num in array:
        if num < minimum:
            minimum = num
    return minimum

print(find_minimum([1,2,3,4]))