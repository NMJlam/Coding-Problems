"""
Link: https://codeforces.com/problemset/problem/2049/A
"""

"""
HAD TO READ EDITORIAL: https://codeforces.com/blog/entry/137273
"""

"""
Case 1: when the array has all zeros
    return 0 
- This is because the array has all zeros as intended. 

Case 2: when there exists a contiguous array of non-zero elements
    return 1 
- For the contiguous array of non-zero numbers you call mex() once, to get zero
- That zero will replace the contiguous array and now the array will have all zeros as there is only 1 contiguous array

Case 3: when there might exist multiple contiguous arrays of non-zero elements and zeros are interleaved
    return 2 
- Call mex() once on the whole array to get a non-zero number
- Call mex another time on the non-zero number to finally get zero 
"""

def solve(): 

    arr_len = int(input())

    arr = str(input())
    lst = arr.split(" ")

    n = len(lst)
    i = 0 
    cont_arr = 0 

    while i < n: 

        if int(lst[i]) != 0: 

            cont_arr += 1

            while i < n and int(lst[i]) != 0: 
                i += 1
        
        i += 1

    if cont_arr == 0: 
        print(0)
    elif cont_arr == 1: 
        print(1)
    else: 
        print(2)

test_cases = int(input())
for _ in range(test_cases): 
    solve()


