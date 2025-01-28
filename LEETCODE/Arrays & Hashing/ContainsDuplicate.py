"""
1) Explain the question back: 
Returns True only when a value is encountered twice in the array, if no duplicates then
returns False. 

2) Clarification: 

Typical cases: 
input: [1,2,3,3] ==> True

Edge Cases
input: [1] ==> False 
input: [] ==> False 

Invalid Input: 
input: ["hello", "nathan"] => Invalid? 

Assumptions: 
- Can I always assume a list of integers (What if there are strings, tuples etc.)
- What if the list is empty 

3) Test cases: 

Input: [1,2,2,3,3,3] => True
Input: [2,2] => True  
Input: [1,2,3] => False 
Input: [] => False 
Input: [1] => False 
Input: ["nathan", "andrew", "john"] => TypeError 


4) Pseudocode: 

If we care about input validation: 

    check over every single elemnt and check if it is an integer - Does not impact the time complexity of O(N), where N is the number of elements 

If care more about efficiency over space:
    hashSet = {}
    visitedelem = []

    for num in input: 
        add to hash set
        add to visitedelem 

        if len(hashset) != len(visitedelem): 
            return True 
    return False 

Complexity: 
    Time: O(N), N is the number of integers 
    Space: O(N), makes an list of elements and a hashset 

==> Time here is more efficient as we have an immediate exit condition when we encounter a duplicate, so we do not need to iterate over the whole array


If care more about space over efficiency:
    hashset = {} 
    num_num = len(input)

    for num in input: 
        add to hashet 
    if num_num != len(hashset)
        return True 
    else: 
        return False 

Complexity
    Time: O(N)
    Space: O(N)

==> Space here is more efficient as we do not create a separate list for visited elements

"""

##### Code1 #####
def ContainsDuplicate1(input: list[int]) -> bool : 

    for num in input: 
        if type(num) != int: 
            return TypeError

    visited_set = set() 
    visited_list = []

    for num in input: 

        visited_list.append(num)
        visited_set.add(num)

        if len(visited_set) != len(visited_list):
            return True 
    return False

##### Code2 #####
def ContainsDuplicate2(input: list[int]) -> bool: 

    for num in input: 
        if type(num) != int: 
            return TypeError
    
    visited_set = set() 
    input_len = len(input)

    for num in input: 

        visited_set.add(num)

    if len(visited_set) != input_len:
        return True 
    
    return False

