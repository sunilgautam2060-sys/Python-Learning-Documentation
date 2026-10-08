

def is_sorted(arr,i=0):
    if i==len(arr)-1:
        return True
    if arr[i]>arr[i+1]:
        return False
    return is_sorted(arr,i+1)

arr=[1,7,3,4,5]
print(is_sorted(arr))
