#!/usr/bin/env python
# coding: utf-8

# In[14]:


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
    
    def sumOfLeftLeaves(self,root):
        def dfs(node,is_left):
            if not node:
                return 0
            if node.left is None and node.right is None:
                if is_left:
                    return node.data
                else:
                    return 0
            left=dfs(node.left,True)
            right=dfs(node.right,False)
            return left+right
        
        return dfs(root,False)
    
bt=BinaryTree() 
while True: 
    print("1.Create Tree 2.exit") 
    ch=int(input("Enter choice: ")) 
    if ch==1: 
        rt = int(input("Enter root:")) 
        bt.create_root(rt) 
    elif ch==2: 
        break
print("Sum of the left leaves:",bt.sumOfLeftLeaves(bt.root))


# In[ ]:





# In[ ]:




