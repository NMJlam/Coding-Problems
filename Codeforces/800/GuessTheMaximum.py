"""
Problem Link: https://codeforces.com/problemset/problem/1979/A
"""

"""
Takeaway: To find the min-max of a sequence of subarrays you just need to iterate over adjacent elements. hello
"""



tests = int(input())

for _ in range(tests): 
    
    arr_len = int(input())
    arr_str = str(input())
    
    arr_lst = arr_str.split(" ")
    
    min_max = float("inf")
    for i in range(arr_len-1): 
        
        j = i + 1 
        
        maxi = max( int(arr_lst[i]), int(arr_lst[j]) )
        
        min_max = min( maxi, min_max)
    
    print(min_max - 1)