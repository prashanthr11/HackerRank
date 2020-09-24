class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as info, left , right
'''

from collections import defaultdict as di

def lca(root, v1, v2):
    maxi = root
    tmp=root
    s = di(int)
    while tmp:
        if tmp.info == v1:
            break
        elif tmp.info < v1:
            tmp = tmp.right
        elif tmp.info > v1:
            tmp = tmp.left
        s[tmp] = 1

    tmp=root
    while tmp:
        if s[tmp]:
            maxi = tmp
        if tmp.info == v2:
            break  
        elif tmp.info > v2:            
            tmp = tmp.left
        elif tmp.info < v2:
            tmp = tmp.right
    return maxi

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
