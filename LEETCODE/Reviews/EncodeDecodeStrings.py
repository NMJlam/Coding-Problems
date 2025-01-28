def encode(strs: list[str]) -> str: 

    output = ""
    for string in strs: 
        output += "#" + str(len(string)) + string
    return output 

def decode(s: str) -> list[str]: 

    i = 0
    output_lst = []

    while i < len(s):
        j = i 

        while s[j] != "#": 
            j += 1

        str_len = int(s[i:j])

        word = s[i + 2 : j + 1 + str_len]
        output_lst.append(word)

        i = j + str_len + 1
    
    return output_lst


