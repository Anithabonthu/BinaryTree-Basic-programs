#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Node: 
    def __init__(self,v): 
        self.left=None 
        self.data=v 
        self.right=None 

class BinaryTree: 
    def __init__(self): 
        self.root=None 
    def create_root(self,value): 
        newnode = Node(value) 
        self.root=newnode 
        self.create_child(newnode) 

    def create_child(self,parent): 
        enq=input("is left child available for %d press y/n: "%parent.data).lower()
        if enq=='y': 
            lc=int(input("enter left child for %d: " %parent.data)) 
            parent.left=Node(lc) 
            self.create_child(parent.left) 
        enq=input("is right child available for %d:  press y/n: "%parent.data).lower()
        if enq=='y': 
            rc=int(input("enter right child for %d: " %parent.data)) 
            parent.right=Node(rc) 
            self.create_child(parent.right) 
def is_SameTree(p,q):
    if not p and not q:
            return True
    elif not p or not q:
            return False
    return p.data==q.data and is_SameTree(p.left,q.left) and is_SameTree(p.right,q.right)
    
p=BinaryTree() 
while True: 
    print("1.Create 1st Tree 2.Exit") 
    ch=int(input("Enter choice: ")) 
    if ch==1: 
        rt = int(input("Enter root:")) 
        p.create_root(rt) 
    elif ch==2: 
        break
q=BinaryTree() 
while True: 
    print("1.Create 2nd Tree 2.Exit") 
    ch=int(input("Enter choice: ")) 
    if ch==1: 
        rt = int(input("Enter root:")) 
        q.create_root(rt) 
    elif ch==2: 
        break
print(is_SameTree(p.root,q.root))


# In[ ]:




