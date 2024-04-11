#!/usr/bin/env python
# coding: utf-8

# In[3]:


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
    def sumNumber(self,root):
        def dfs(node ,num):
            if node:
                if not node.left and not node.right:
                    return num*10+node.data
                
                add=0
                add+=dfs(node.left,num*10+node.data)
                add+=dfs(node.right,num*10+node.data)
                
                return add
            else:
                return 0
        print("The Sum of root-to-leaf is:" ,dfs(root,0)) 
bt=BinaryTree() 
while True: 
    print("1.Create Tree 2.Exit") 
    ch=int(input("Enter choice: ")) 
    if ch==1: 
        rt = int(input("Enter root:")) 
        bt.create_root(rt) 
    elif ch==2: 
        break
bt.sumNumber(bt.root)


# In[ ]:





# In[ ]:





# In[ ]:




