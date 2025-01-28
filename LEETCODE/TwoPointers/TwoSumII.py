"""
Talked with Anthony
"""

"""
Pseudo code 

lo = 0 
hi = len(list)

while lo is not equal to high: 

    sum = list[lo] + list[hi]
    if the target < sum: 
        move up lo 
    elif target > sum: 
        move down hi 
    else:
        return true 
return false
"""

def twoSum(numbers: list[int], target: int) -> list[int]:

    lo = 0 
    hi = len(numbers) - 1

    while lo != hi: 

        sum = numbers[lo] + numbers[hi]
        print(sum)

        if sum < target: 
            lo += 1 
        elif sum > target:
            hi -= 1
        else:
            return [lo + 1, hi + 1]
    
    return False 
