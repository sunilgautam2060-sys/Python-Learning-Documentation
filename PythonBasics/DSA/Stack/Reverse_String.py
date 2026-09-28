

class solution:
    def reverse_string(self,string):
        stack=[]
        for i in string:
            stack.append(i)


        #we are doing inplace reversal.
        for i in range(len(string)):
            string[i]=stack.pop()

        print(string)    


s=solution()

#we are calling using list not string like :"hello" because string are immutable so ,
#in place logic we written will not work.
s.reverse_string(['h','e','l','l','o'])               