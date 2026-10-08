

def linear_search(arr,target,index=0):
    if index==len(arr):
        return -1
    if arr[index]==target:
        return index
    return linear_search(arr,target,index+1)

arr=[1,2,3,4,5,6,7]
target=8
result=linear_search(arr,target)
if result==-1:
    print("Element not found in the array ")
else:
    print("Element found at index:",result)