

from math import log10

def Rev(n):
    if n%10==n:
        return n
    else:
        power=int(log10(n))
        return (n%10)*pow(10,power)+Rev(n//10)

def is_palindrome(n):
    return n==answer

answer=Rev(12345)  
print("The reverse of the number is:", answer)
print(is_palindrome(12345))


