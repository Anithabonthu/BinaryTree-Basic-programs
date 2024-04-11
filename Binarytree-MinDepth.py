#!/usr/bin/env python
# coding: utf-8

# In[4]:


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
    def minDepth(self,root):
        if root is None:
            return 0
        if not root.left and not root.right:
            return 1
        l=self.minDepth(root.left) if root.left else float('inf')
        r=self.minDepth(root.right) if root.right else float('inf')
        return min(l,r)+1
bt=BinaryTree() 
while True: 
    print("1.Create Tree 2.Exit") 
    ch=int(input("Enter choice: ")) 
    if ch==1: 
        rt = int(input("Enter root:")) 
        bt.create_root(rt) 
    elif ch==2: 
        break
print("Minimum depth of tree is:",bt.minDepth(bt.root))


# In[ ]:





# In[ ]:




