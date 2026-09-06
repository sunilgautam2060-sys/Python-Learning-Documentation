

#the logic is same as pivot index firstly we calculate total sum or product
# than traverse each index and calculate left and right sum/product 
#leftproduct=left side product up to index i-1 means if we are at index 5 leftproduct will be ,
#product of element from index0 to index4.
#Rightproduct=totalproduct/leftproduct/currentindexvalue.



List=[1,2,3,4,5,6]

n=len(List)

Total_Product=1
ResultProduct=[]


for i in range(n): #this toolbox calculate total_product of given list.
    Total_Product*=List[i]

for i in range(n):
    if i==0:
      LeftProduct=1  

    else:
        LeftProduct*=List[i-1]

    RightProduct=(Total_Product//LeftProduct)//List[i]

    ResultProduct.append(LeftProduct*RightProduct)

print(ResultProduct)
    