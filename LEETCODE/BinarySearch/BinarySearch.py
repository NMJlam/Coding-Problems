
def fast_search(nums: list[int], target:int ) -> int:

    lo = 0 
    hi = len(nums) - 1
    mid = (lo + hi) // 2

    if nums[lo] == target: 
        return lo 
    elif nums[hi] == target: 
        return hi 

    while True: 

        if target < nums[mid]: 
            hi = mid
        elif target > nums[mid]: 
            lo = mid
        elif target == nums[mid]: 
            return mid 
        
        mid = (lo + hi) // 2
        
        if hi == mid or lo == mid: 
            return -1 


def binary_search(nums: list[int], target: int) -> int: 
    
    lo = 0 
    hi = len(nums) - 1
    
    while lo < hi: 

        mid = (lo + hi) // 2

        if nums[mid] <= target:
            lo = mid
        else: 
            hi = mid 
    
    if nums[lo] == target: 
        return lo 
    else:
        return -1 
