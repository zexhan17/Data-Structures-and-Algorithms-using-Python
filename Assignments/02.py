class Node:
	def __init__(self,data=None):
		self.val=data
		self.next=None


class LinkedList:
	def __init__(self):
		self.head=None

def push(self,val):
	new_node=Node(val)

	if self.head is None:
		self.head=new_node
		return

	last=self.head

	while last.next is not None:
		last=last.next

	last.next=new_node

LinkedList.push=push

def __str__(self):

	re_str="["
	temp=self.head

	while temp is not None:
		re_str+=str(temp.val)+", "
		temp=temp.next
	re_str=re_str.rstrip(", ")
	re_str+="]"

	return re_str

LinkedList.__str__=__str__

def len(self):
	temp=self.head
	count=0
	while temp is not None:
		count+=1
		temp=temp.next
        
	return count
LinkedList.len=len

def pop(self):
    
	if self.head is None:
		raise IndexError("List is Empty!")
    
	last=self.head
    
	while last.next is not None:
		pre=last
		last=last.next
        
	re=last.val
	pre.next=None
	return re

LinkedList.pop=pop

def get(self, index):
    
	if index==0:
		re=self.head.val
		return re
	re_count=len(self)
	if index==re_count:
		raise IndexError("Index out of bound")
	temp=self.head
	count=0
	while temp is not None:
		if count==index:
			re=temp.val
			return re
		pre=temp
		temp=temp.next
		count+=1

        
	if index>count:
		raise IndexError("Index out of bound")

def remove(self,value):
    
	

	temp=self.head
    
	if temp is not None:
		if temp.val==value:
			self.head=temp.next
			return
	while temp is  not None:
		if temp.val==value:
			break
		pre=temp
		temp=temp.next
	if temp is None:
		return
	pre.next=temp.next
        
LinkedList.remove=remove
def insert(self,index,val):
	new_node=Node(val)
    #at zero index;
	if index==0:
		new_node.next=self.head
		self.head=new_node
		return
    
	count=0
	temp=self.head
	while temp.next is not None and count<index:
		pre=temp
		temp=temp.next
        
	pre.next=new_node
	new_node.next=temp
    
LinkedList.insert=insert	

LinkedList.get=get
if __name__ == "__main__": 
    l = LinkedList() 
    l.push(5) 
    l.push(6) 

    print(l)

    print(l.len())

    l.pop() 
    print(l.len())

    print(l.get(0))
    l.get(2) # Should say "IndexError: Index out of bound"

