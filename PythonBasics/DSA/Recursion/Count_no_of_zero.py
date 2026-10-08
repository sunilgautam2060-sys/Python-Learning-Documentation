


def count_zero(n, count=0):
    if n==0:
        return count
    else:
        if n%10==0:
            count+=1
        return count_zero(n//10,count)

count=count_zero(100200300)
print("The number of zeros in the given number is:", count) 


