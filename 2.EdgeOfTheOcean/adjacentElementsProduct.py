"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product. 
"""

def adjacent_elements_product(array: list) -> int:
    max = array[0] * array[1]
    for i in range(len(array)-1):
        if array[i] * array[i+1] > max:
            max = array[i] * array[i+1]
    return max
    #return max([array[i] * array[i+1] for i in range(len(array)-1)])

print(adjacent_elements_product([3, 6, -2, -5, 7, 3])) # 21