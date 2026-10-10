

List=[1,2,3,4,5,6,7,8,9]

def print_list_reverse(List,index=0):
    if index==len(List):
        return
    print_list_reverse(List,index+1)
    print(List[index],end=" ")

print_list_reverse(List)    