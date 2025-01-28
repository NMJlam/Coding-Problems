"""
1) Explain question back: 
So what you would like me to do is to make a stack class which supports a getMin() function which returns
the minimum element within a stack?

Push, pop and top are all the same as a regular stack class performing operations in O(1) time. 
getMin() is also in O(1) time 
"""

"""
2) Clarification:
- Can I assume that there will only be numbers as inputs? - yes 
- Would you want me to return an error, if they call the methods on the stack but it is empty? - no (only non-empty stacks)
"""

"""
3) Pseudocode:

def __init__() 
    make an empty list 

def push(int):
    append to self.emptylist

def pop():
    emptylist.pop()

def top(): 
    return emptylist[-1]

def getMin(): 
    .... 
"""

"""
Gave up after 20 mins of thinking 
Anthony explained the solution. Code is below: 
"""

class MinStack(object):

    def __init__(self):
        self.topStack = []
        self.minStack = []
        self.min = float('inf')
        

    def push(self, val):

        self.topStack.append(val)

        if not self.minStack or val < self.minStack[-1]: 
            self.minStack.append(val)
        else: 
            self.minStack.append(self.minStack[-1])
        

    def pop(self):

        self.topStack.pop()
        self.minStack.pop()

    def top(self):

        return self.topStack[-1]
        

    def getMin(self):

        return self.minStack[-1]




