

def search(List,target,start,end):
    if start>end:
        return -1

    mid=start+(end-start)//2

    if List[mid]==target:
        return mid
    elif List[mid]>target:
        return search(List,target,start,mid-1)
    else:
        return search(List,target,mid+1,end)


List=[1,2,5,10,66,78,87]
target=66
start=0
end=len(List)-1

print(search(List,target,start,end) ) 

    