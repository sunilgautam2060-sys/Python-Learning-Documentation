


List=[2,5,7,11,13,39] #given list.

required=int(input("Enter the required four integer sum ")) #enter the required sum you want to check.

i=0 #initializing outermost loop i with 0.

n=len(List) #length of list.

isfound=False #Flag initializing with False , used below to break from the nested loops.

while i<=n-4 :#outermost loop starts from 0 ends at n-4.

  j=i+1 #after each i , j will be i+1.

  while j<=n-3:#inside the i , there is another loop for j , j will be traversing from (i+1) 
               #to n-3 for each value of i.

    
     k=j+1 #initializing k ,


     l=n-1 #initializing l ,

     while k<l:#for each outermost i and foreach j afterward, the loop will run with condition k<l.
          
         sum=List[i]+List[j]+List[k]+List[l] #calculating sum with present i,j,k,l.
             
         if sum>required: #if this case satisfies only than l=l-1.
             
          l=l-1
             
             
         elif sum<required: #the situation can satisfies this aswell .than k=k+1.
          k=k+1
             
         else:

          #the case can only have 3 possibilities either greater than ,smaller than.
          # or equal to ,if equals than print the numbers.
          print("The Four Integers Are: {} {} {} {}".format(List[i],List[j],List[k],List[l]))

          isfound=True #This flag is introduced to break from the nested loops since we are inside
                       # layers of the loops break will only break one loop so flag is declared.
          
          break    # this is all to break the while k<l: loop
             
     if isfound==True: #this is all to break the outer loop j.
      break    

     j=j+1#increament to regulate the loop.

  if isfound==True:#this is all to break the outermost loop i.
   break

  i=i+1 #increamenting outermost loop i .


if isfound==False:#if no integers founds only than .
  print("There is No integers ")

          