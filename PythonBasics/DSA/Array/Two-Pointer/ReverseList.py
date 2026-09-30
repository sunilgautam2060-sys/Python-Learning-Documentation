
list=[1,2,3,4]
index=0
for num in range(len(list)-1,-1,-1):
     if index<num:
          temp=list[num]
          list[num]=list[index]
          list[index]=temp
          index=index+1

print(list)    
   