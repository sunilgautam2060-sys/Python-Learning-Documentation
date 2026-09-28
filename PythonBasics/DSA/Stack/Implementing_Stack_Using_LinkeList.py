
#creating node.
class node:
    #constructor.
    def __init__(self,data):
        self.data=data
        self.next=None

#creating stack. 
class stack:
    
    #whever i will create object of class stack,this constructor will run,
    #its task is to make empty stack.
    def __init__(self):
        self.top=None


    #check if stack is empty.   
    def isempty(self):

        if self.top==None:
            return True

        return False
    
    
    #Add element.
    def push(self,data):
       
        new_node=node(data)
        new_node.next=self.top
        self.top=new_node


    #see top element.
    def peek(self):
        if self.isempty()==True:
            return "stack empty"

        else:
          return self.top.data


    #remove top element.
    def pop(self):

        if self.isempty()==True:
            return "stack is empty"

        else:
          self.top=self.top.next
    

    #print all elements in stack.
    def traversal(self):
        temp=self.top

        while temp!=None:
            print(temp.data)
            temp=temp.next


    #count elements.
    def size(self):

        if self.isempty():
            return 0
        
        temp=self.top
        count=0

        while temp!=None:
            count+=1
            temp=temp.next

        return count
        


s=stack()
s.push(2)
s.push(3)
print("stack:")
s.traversal()

print("Top:",s.peek())
print("Size:",s.size())

s.pop()

print("After Pop:")
s.traversal()

