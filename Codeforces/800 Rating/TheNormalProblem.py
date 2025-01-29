"""
Link to question: https://codeforces.com/problemset/problem/2044/B
"""

"""
Naive Approach 
"""

def convert(a: str) -> str: 
    
    b = ""
    
    for idx in range(len(a)-1, -1, -1): 
        letter = a[idx]

        if letter == "p":
            b += "q"
        elif letter == "q":
            b += "p"
        else: 
            b += letter 
    
    return b 


# when the input has successive rows you can take multiple inputs at a time by using 2 input functions
t = int(input()) 

for _ in range(t): 

    a = input() 
    print(convert(a))


    






            