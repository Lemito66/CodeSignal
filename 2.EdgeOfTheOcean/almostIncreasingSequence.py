"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing. 
"""

def almost_increasing_sequence(sequence: list) -> bool:
    count = 0
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            count += 1
            if i > 0 and i < len(sequence)-2 and sequence[i-1] >= sequence[i+1] and sequence[i] >= sequence[i+2]:
                return False
    return count <= 1

#print(almost_increasing_sequence([1, 3, 2])) # True
print(almost_increasing_sequence([1, 3, 2, 1])) # False
