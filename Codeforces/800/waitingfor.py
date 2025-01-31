"""
Link: https://codeforces.com/problemset/problem/2038/J
"""

"""
1) Keep track of the people who arrive, as buses arrive subtract the people 
2) If at least 1 free seat print yes, else no 
"""

def str_reader(input_string: str) -> (str, int): 
    number = ""
    for i in range(len(input_string)): 
        if input_string[i].isnumeric(): 
            number += input_string[i]
    return ( input_string[0], int(number) )

"""
Program: 
"""

test_cases = int(input())
people = 0 
seats = 0 

for _ in range(test_cases): 

    event = str(input())
    event, num = str_reader(event)

    if event == "P": 
        people += num

    else: 
        seats = num 
        
        if seats > people:
            people = 0 
            print("yes")
        
        else: 
            people -= seats
            print("no")


    


    
        


