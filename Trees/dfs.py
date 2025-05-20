class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# Function to Visit all of the Nodes using Depth first Search Iteratively
def depthFirstSearchIterative(root):
    if(not root):
        return None
    data = [root]
    while(len(data)>0):
        current_node = data.pop()
        print(current_node.val)
        if(current_node.right!=None):
            data.append(current_node.right)
        if(current_node.left!=None):
            data.append(current_node.left)

# Function to Visit all of the Nodes using Depth first Search Recursively
def depthFirstRecursive(root):
    try:
        if(not root):
            return None
        print(root.val)
        depthFirstRecursive(root.left)
        depthFirstRecursive(root.right)
    except Exception as e:
        print(e)
        return

print(depthFirstSearchIterative(a))
print(depthFirstRecursive(a))

