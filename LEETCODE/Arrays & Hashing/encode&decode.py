"""
Step 1: Explain the question back to the interviewer: 

Would I be correct to say that:
1) Encode function turns a list of strings into a singular string 
2) Decode function turns a singular string to a list of strings
"""

"""
Step 2: Make any clarifications:

Would it be correct to say that all the characters are alphanumeric? 
=> They are all the 256 ASCII values 
"""

"""
Step 3: Make test cases: 

Encode => Decode
1) ["Nathan", "Lam] => ["Nathan", "Lam"]
2) [""] => [""]
3) ["", ""] => [""] ??
4) ["", "Nathan"] => ["Nathan"]??
"""

"""
Step 4: Write Pseudocode: 

Encode: O(N)
For item in list
    For letter in item:
        convert to ascii number 
    at the end of the item add 257 or -1 (out of ASCII range)

Decode: O(N)
For letter in string:  
    if within range 0-256: 
        convert ascii to letter 
        add to empty string
    else:
        add the current string into the list 
        empty the string so we have fresh string 

"""

def encode(strs: list) -> str: 

    return_str = ""
    
    for item in strs: 
        for letter in item: 
            char = str(ord(letter))

            if len(char) == 3: 
                return_str += char
            elif len(char) == 2:
                return_str = return_str + "0" + char
            else: 
                return_str = return_str + "00" + char
        return_str += "###"
    
    return return_str

def decode(s: str) -> list:
    
    return_lst = []
    item = ""

    for idx in range(0, len(s), 3):

        ascii_num = s[idx: idx + 3]
        try: 
            item += chr(int(ascii_num))
        except: 
            return_lst.append(item)
            item = ""
    
    return return_lst

"""
Revised => Time & Space complexity was the same but not the MOST efficient solution
Best approach is to note the length of each of the words and then count the words from the string 
"""

class Solution:
    
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res

"""
This approach is more efficient as it does not store 3 characters per letter -> memory
And on the decode side it does not need to iterate over thrice as many characters
"""
