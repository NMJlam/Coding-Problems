"""
Link: https://codeforces.com/problemset/problem/2060/C
"""

tests = int(input()) 

for _ in range(tests): 
    
    nk = str(input()).split(" ")
    n, k = int(nk[0]), int(nk[1])
    
    arr = str(input()).split(" ")
    arr_no = [int(x) for x in arr] 
    arr_no.sort()
    
    a = 0 
    b = n - 1 
    score = 0 
    
    while a < b: 
        
        sum = arr_no[a] + arr_no[b]
        
        if sum == k:
            score += 1
            
            a += 1 
            b -= 1 
        
        elif sum > k:

            b -= 1
        
        else:
            a += 1
            
    
    print(score)
        
        