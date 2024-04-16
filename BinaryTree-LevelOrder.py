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
    def LevelOrder(self,root):
        if root is None:
            return []
        temp=[]
        levels=[root]
        result=[[root.data]]

        while levels:
            node=levels.pop(0)
            if node.left:temp.append(node.left)
            if node.right:temp.append(node.right)

            if not levels:
                if temp:
                    result.append([i.data for i in temp])

                levels=temp
                temp=[]
        return(result)
        
bt=BinaryTree() 
while True: 
    print("1.Create Tree 2.Exit") 
    ch=int(input("Enter choice: ")) 
    if ch==1: 
        rt = int(input("Enter root:")) 
        bt.create_root(rt) 
    elif ch==2: 
        break
res=bt.LevelOrder(bt.root)
print("Level Order of a tree is:")
for i in res:
    print(i,end=" ")


# In[ ]:





# In[ ]:




