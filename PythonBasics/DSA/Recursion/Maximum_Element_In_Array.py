
arr=[1,2,3,8,5,6,7]

def maximum_element(arr,n):

    #base-case: if the array size is 1,than maximum element is a[0] that is know.
    if n==1:
        return arr[0]

    #for each array ,take first element and compare it with ,
    #the maximum element of the rest of the array.
    first_element=arr[0]

    answer=maximum_element(arr[1:],n-1)

    #return maximum of first element and
    #the maximum element of the rest of the array.
    return max(first_element, answer)

    
print(maximum_element(arr,len(arr)))
