class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None
def push(self,val):
    
    new_node=Node(val)
    #case 1
    if self.head is None:
        self.head=new_node
        self.head.next=None
        return
    
    temp=self.head
    while temp.next is not None:
        temp=temp.next
        
    temp.next=new_node
    new_node.next=None
    
LinkedList.push=push

def __str__(self):
    
    re_str="["
    
    temp=self.head
    while temp is not None:
        re_str+=" "+str(temp.val) + " ,"
        temp=temp.next
        
    re_str=re_str.rstrip(",")
    re_str+="]"
    
    return re_str
LinkedList.__str__=__str__

def pop(self):
    
    #case 1
    
    if self.head is None:
        raise IndexError("list cannot be pop, : because list is empty")
    #case 2
    if self.head.next is None:
        val=self.head.val
        self.head=None
        return val
    
    temp=self.head
    while temp.next is not None:
        pre=temp
        temp=temp.next
        
    val=temp.val
    pre.next=None
    return val
    
LinkedList.pop=pop       

def insert(self,index,val):
    new_node=Node(val)
    if index==0:
        new_node.next=self.head
        self.head=new_node
        return
    
    count=0
    temp=self.head
    while temp is not None and count<index:
        pre=temp
        temp=temp.next
        count+=1
    pre.next=new_node
    new_node.next=temp
        
        
LinkedList.insert=insert

def remove_at(self,index):
    
    if index>self.len():
        raise IndexError("list index out of Range ")
    
    if index==0:
        self.head=self.head.next
        return
    
    if self.head is None:
        raise IndexError("Cannot be remove because list is empty")
        
    
        
    count=0
    temp=self.head
    # remove funtion must be temp not the temp.next remember!!!!
    while temp is not None and count<index:
        pre=temp
        temp=temp.next
        count+=1
        
    pre.next=temp.next
    
    
    
LinkedList.remove_at=remove_at

def len(self):
    
    if self.head is None:
        return 0
    temp=self.head
    count=0
    while temp is not None:
        temp=temp.next
        count+=1
    return count

LinkedList.len=len

def remove(self,val):
    
    
    if self.head is None:
        raise IndexError(" Cannot be removed becaus list is empty ")
        
    if self.head.val ==val:
        self.head=self.head.next
        return
    
    if self.head.next is None:
        if self.head.val==val:
            self.head=None
            return 
        
    temp=self.head
    while temp.next is not None:
        pre=temp
        temp=temp.next
        if temp.val==val:
            break
        else:
            return
        
    pre.next=temp.next
    return

LinkedList.remove=remove
        
def reverse_list(self):
    pre = None
    current = self.head 
    while current is not None:
        next = current.next
        current.next = pre 
        pre = current 
        current = next
    self.head = pre 
LinkedList.reverse_list=reverse_list         
    

if __name__ == '__main__': 
    l = LinkedList() 
    l.push(1) 
    l.push(2)
    l.push(3)

    print(l)

    l.reverse_list() 
    print(l)

