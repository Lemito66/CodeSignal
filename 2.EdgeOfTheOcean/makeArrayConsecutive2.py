"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed. 
"""

def make_array_consecutive2(statues: list) -> int:
    """ count = 0
    for i in range(min(statues), max(statues)):
        if i not in statues:
            count += 1
    return count """
    return statues[-1] - statues[0] - len(statues) + 1 

print(make_array_consecutive2([6, 2, 3, 8])) # 8-2-4+1 = 3