class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data=newdata
        
    def setNext(self,newnext):
        self.next=newnext

class UnorderedList:
    def __init__(self):
        self.head=None
    def is_empty(self):
        return self.head==None

    """enqueue places at end"""
    def enqueue(self,item):
        if self.head==None:
            self.head=Node(item)
        else:
            current=self.head
            while current.getNext() != None:
                current=current.getNext()
            current.setNext(Node(item))

    """stack places at front"""
    def stack(self,dat):
        temp=Node(dat)
        temp.setNext(self.head)
        self.head=temp

    def delete(self,adv):
        if self.head==None:
            print("no nodes to delete")
        else:
            current=self.head
            while current.getNext() and current.getNext().getData()!=adv:
                current=current.getNext()
            if current.getNext()==None:
                print("node does not exist")
            elif not current.getNext().getNext():
                current.setNext(None)
            else:
                current.setNext(current.getNext().getNext())

    def display(self):
        current=self.head
        while current != None:
            print(current.getData())
            current=current.getNext()



myList=UnorderedList()

for i in range(0,6):
    i=input("Enter a number: ")
    myList.enqueue(i)

myList.display()
