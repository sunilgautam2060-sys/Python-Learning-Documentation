
#in queue head node is called as"Front"
#tail node is called "rear"
#enqueue=insert.
#dequeue=delete.

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

#initially,front and rear both are None.
class queue:
    def __init__(self):
        self.front=None
        self.rear=None


    #insertion.
    def enqueue(self,data):
       
        new_node=node(data)

        #this condition ,self.rear tells the queue is empty.
        if self.rear==None:
            self.front=new_node
            self.rear=self.front


        #insertion in queue always from rear.
        else:
            self.rear.next=new_node
            self.rear=new_node


    #deletion always from front in queue.
    def dequeue(self):
       
        if self.front==None:
            return print("empty queue")      

        else:
            self.front=self.front.next


    #isempty is bool function,if self.rear is None it return true
    #if not than it returns false.
    def isempty(self)->bool:
        return self.front==None
    

    def traversal(self):

        temp=self.front

        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next



    def size(self):
        count=0
        temp=self.front

        while temp!=None:
            count+=1
            temp=temp.next

        return count


    def front_item(self):
        
        if self.front==None:
            print('Empty Queue')
            return

       
        return self.front.data


    def rear_item(self):
        
        if self.rear==None:
            print('Empty')
            return

        return self.rear.data


    
q=queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
q.enqueue(20)
q.enqueue(25)
q.enqueue(30)

print("Front Item:",q.front_item())
print("Rear Item:",q.rear_item())

print("Is Queue is empty ?",q.isempty())

print("\n The Queue are:")
q.traversal()

print("The Length of Queue is:",q.size())

q.dequeue()

print("After Dequeue:")
q.traversal()


        


