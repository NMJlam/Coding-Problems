"""
https://codeforces.com/problemset/problem/2051/B
"""

"""
Brute force:
"""

# tests = int(input())

# for _ in range(tests):
    
#     distances = str(input()).split(" ")
#     arr = [int(dist) for dist in distances]
    
#     target = arr[0]
#     travelled = 0 
    
#     i = 1
#     count = 0 
    
#     while travelled < target: 
    
#         travelled += arr[i]
#         i += 1 
#         count += 1
    
#         if i >= len(arr):
#             i = 1 
    
#     print(count)

"""
O(1) Solution: 
"""

tests = int(input())

for _ in range(tests):
    
    
    distances = [int(dist) for dist in str(input()).split(" ")]

    total = sum(dist for dist in distances)
    target = distances[0]
    
    day3dist = total - target
    remainder = target % day3dist
    days = (target // day3dist) * 3 
    
    if remainder == 0: 
        print(days)
    elif distances[1] >= remainder:
        print(days + 1)
    elif distances[1] + distances[2] >= remainder:
        print(days + 2)
    else: 
        print(days + 3)





        




