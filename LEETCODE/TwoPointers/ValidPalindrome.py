"""
1) Explain the question back: 
I need to write a program that is able to return True or False based on whether a string is a palindrome and palindrome
is a string which is spelt the same forward and backwards.
"""

"""
2) Clarification: 
- Would it be correct to assume that a palindrome has a point of symmetry? 
        Say "nahan" has a letter of symmetry around "h" and "naan" has a point of symmetry in the centre. 
- So I need to remove every single non alphabetical character and convert them into a lower case?
"""

"""
3) Test Cases: 
Input: "N" 
Output: True

Input: "#"
Output: True 

Input: "A man, a plan, a canal: Panama"
Output: True

Input: "Pretty and, cute"
Output: False

Input: "Pretty and CUTE, "
Output: False
"""

"""
4) Pseudo code: #### TALK ABOUT THE SAME COMPLEXITY ####

end = last index of string 

for start in range( len of string) 
    
    if start same as end: ---> During iteration 
        end move down 1 
        start move up 1 
    
    elif end - start < 0: ---> When they cross over terminate
        return True

    else: 
        return False

time complexity: O(N)
aux space complexity: O(N)
"""

def isPalindromePrev(s: str) -> bool: 

    letters = "" ## This makes the complexity O(N)
    for char in s: 
        if char.isalnum():
            letters += char.lower()

    if len(letters) <= 1:
        return True

    start = 0
    end = len(letters) - 1

    while True: 

        if letters[start] == letters[end]: 
            end -= 1
            start += 1
        elif letters[start] != letters[end]:
            return False
        
        if end - start < 0:
            return True

"""
Revised space complexity from O(N) to O(1)
"""

def isPalindrome(s: str) -> bool: 

    i, j = 0, len(s) - 1 # sets the pointers i & j 

    while i < j: # if at any time the pointers overlap then we need to terminate 

        while not s[i].isalnum(): # because you are trying to find the next alnum char, you could pass the second pointer if no alnum chars exist. This results in Index out of range error as the second pointer is initialised to the end
            i += 1 # increments the pointer

        while not s[j].isalnum():
            j -= 1
        
        if s[i].lower() != s[j].lower(): # checks the "sameness" of the alnum characters, if no same then palindrome
            return False

        i += 1 # increments the pointers, after the "sameness", allowing us to check the next characters. 
        j -= 1

    return True # if the loop is able to fully complete then we have symmetry, hence there is a palindrome


print(isPalindrome(";;"))