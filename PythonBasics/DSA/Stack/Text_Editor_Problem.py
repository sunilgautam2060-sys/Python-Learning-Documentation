#In this problem, we have text:sunil and we pass the string of (u and r)
#string 'u' means (undo) remove last element and string 'r' means (redo) append previous undo string 

#we use two stack here: undo and redo ,we append the text to undo stack which is "sunil"
#we traverse through the string i.e "uuuur" than if 'u'comes we define logic 
#if 'r' comes we define logic.


class solution:
    def text_editor(self,string):

        text="sunil"
        undo=[]
        redo=[]

        #adding the text to the stack undo.
        for i in text:
            undo.append(i)

        #traversing the string of 'u' and 'r' combination.
        for i in string:

            #if 'u' comes.
            if i == "u":
                data=undo.pop()
                redo.append(data)

            #if 'r' comes.
            else:
               data=redo.pop()
               undo.append(data) 


        #this logic is to print the final result stored in undo stack .
        result=""
        while len(undo)>0: #run while loop until the stack is not empty.
             result=undo.pop()+result    

        print(result)     


s=solution()        
s.text_editor("uuurr")


