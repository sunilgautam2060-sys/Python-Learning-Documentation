
def reverse_string(s):
    
    if len(s)==1:
        return s

    last_character=s[-1]

    answer= last_character + reverse_string(s[:-1])

    return answer        


print(reverse_string("Hello World"))        

