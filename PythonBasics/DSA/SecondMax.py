List=[14,43,12,15,78,22]
Secondmax= 0
Max=List[0]
n=len(List)

for i in range(1,n):
    if List[i]>Max:
        Secondmax=Max
        Max=List[i]#Accumulates the maximum number in Max Variable.


    elif List[i]>Secondmax:
            Secondmax=List[i]

print("Maximum is : " , Max)
print("Second Maximum is : " , Secondmax)



