"""
Link to question: https://codeforces.com/problemset/problem/2047/A
"""

"""
- Thinking of square numbers 
- If the net sum is square then we have a day where she is happy 


1) take the first number for the test cases 
2) then from the first number entered you would have to note down how many days you take for the each layer 
3) add the numbers of each day into the sum ==> if the sum is a square then increment 1 to show that she is happy 
"""

# break down the strings into 1 2 3 4 54 5 54 etc etc and check for squares 

def happy(ith_days: int) -> int: 

    sum = 0 
    current_no = ""
    ith_days += " "

    happy_days = 0

    for char in ith_days: 

        if char != " ": 
            current_no += char
        else: 
            sum += int(current_no)
            current_no = ""

            square = sum ** 0.5
            even = sum /2 

            if square.is_integer() and even.is_integer() is False: 
                happy_days += 1
    
    print(happy_days)

#take the test cases as an input: 
tests = int(input())
for _ in range(tests): 
    days = int(input())
    
    ith_day_str = str(input())
    happy(ith_day_str)




        
