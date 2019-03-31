
"""*********************Queue*****************************"""
class Queue:
    def __init__(self,max_size):
        self.max_size=max_size
        self.elements=[None]*self.max_size
        self.rear=-1
        self.front=0
    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.elements == other.elements
        
        return NotImplemented
    
    def enter_data(self,input_list):
        for element in input_list:
            self.enqueue(element)
            
    def get_elements(self):
        return self.elements
    
    def is_full(self):
        if(self.rear==self.max_size-1):
                return True
        return False
    
    def is_empty(self):
        if(self.front>self.rear):
            return True
        return False
    
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.rear+=1
            self.elements[self.rear]=data
    
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.elements[self.front]
            self.front+=1
            return data
    
    def display(self):
        for index in range(self.front, self.rear+1):
            print(self.elements[index])
"""*********************Stack*****************************"""
class Stack:
    def __eq__(self, other):
        if isinstance(other, Stack):
            return self.elements == other.elements
        
        return NotImplemented

    def __init__(self,max_size):
        self.max_size=max_size
        self.elements=[None]*self.max_size
        self.top=-1
    def enter_data(self,input_list):
        for element in input_list:
            self.push(element)
    def get_elements(self):
        return self.elements
    def is_full(self):
        if(self.top==self.max_size-1):
            return True
        return False
    
    def is_empty(self):
        if(self.top==-1):
            return True
        return False
    
    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.top+=1
            self.elements[self.top]=data
            
    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.elements[self.top]
            self.top-=1
            return data
    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.top
            while(index>=0):
                print(self.elements[index])
                index-=1

            
"""*********************Linkedlist************************"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __str__(self):
        return (self.data,self.next)

class LinkedList:    
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __eq__(self, other):
        if isinstance(other, LinkedList):
            return self.get_elements() == other.get_elements()
        return NotImplemented
        
    def enter_data(self,input_list):
        for element in input_list:
            self.add(element)
            
    def add(self,data):
        new_node=Node(data) 
        if(self.head is None):
            self.head=self.tail=new_node
        else:
            new_node=Node(data)
            self.tail.next=new_node
            self.tail=new_node
    
    def insert(self,data,data_before):
        if(data_before==None):
            next_node=self.head
            new_node=Node(data) 
            self.head=new_node   
            self.head.next=next_node
        else:
            new_node=Node(data)
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.next=node_before.next
                node_before.next=new_node
                if(new_node.next is None):
                    self.tail=new_node
            else:
                print(data_before,"is not present in the Linked list")
            
    def display(self):
        node=self.head
        while(node.next is not None):
            print(node.data)
            node=node.next
        print(node.data)
    
    def find_node(self,data):
        node=self.head
        
        while(node.next is not None):
            if(node.data==data):
                return node
            node=node.next
        if(node.data==data):
            return node
        else:
            return None
    def get_elements(self):
        elements = []
        node = self.head
        while(node.next is not None):
            elements.append(node.data)
            node=node.next
        elements.append(node.data)
        return elements

    def delete(self,data):
        node=self.find_node(data)
        if(node is not None):
            if(node==self.head):
                self.head=node.next
            else:
                temp=self.head
                while(temp.next is not None):
                    if(temp.next==node):
                        temp.next=node.next
                        if(node==self.tail):
                            self.tail=temp
                            break
                    temp=temp.next
        else:
            print(data,"is not present in Linked list")
            

