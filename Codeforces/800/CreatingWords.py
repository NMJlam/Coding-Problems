"""
Very Easy implementation question. 

Strings are immutable 
Ways switch letters of a string: 
- list and swap 
- slicing 
"""


tests = int(input())
for _ in range(tests): 
    words = str(input())
    output = words[4] + words[1:4] + words[0] + words[5:7]
    print(output)
            
    
    