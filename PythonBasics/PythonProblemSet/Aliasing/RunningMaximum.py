
list=[7,9,2,10]
RunningMaximum=[]
Maximum=0
for num in list:
    if num>Maximum:
        Maximum=num
        RunningMaximum.append(Maximum)
print("Running Maximum List : " , RunningMaximum )        
