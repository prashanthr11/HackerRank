""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def isbst(root, mini = -98798798797, maxi = 9797979797979):
    if not root:
        return True
    
    if root.data <= mini or root.data >= maxi:
        return False
    
    lft = isbst(root.left, mini, root.data)
    rt = isbst(root.right, root.data, maxi)
    
    return lft and rt

def check_binary_search_tree_(root):
    return isbst(root)
