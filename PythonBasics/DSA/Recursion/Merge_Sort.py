

arr=[5,4,3,2,1,6,7,8,9,10]

def merge_sort(arr):

    #base-case:
    if len(arr)==1:
        return arr

    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    #recursive calls.
    left_array=merge_sort(left)
    right_array=merge_sort(right)

    #merge and sort the two halves.
    #return the merged and sorted array to where it was called.
    #that function is merge_sort.
    
    result_array=merge(left_array,right_array)
    return result_array


#merge function to merge and  sorted two arrays into one sorted array.
def merge(left,right):

    result=[]
    i=j=0
    n=len(left)
    m=len(right)

    while i<n and j<m:

        if left[i]<right[j]:
            result.append(left[i])
            i+=1

        else:
            result.append(right[j])
            j+=1


    while i<n:
        result.append(left[i])
        i+=1

    while j<m:
        result.append(right[j])
        j+=1

    #return the merged and sorted array.to where it was called.
    return result        

    
print(merge_sort(arr))  # Output: [1, 2, 3, 4, 5]

