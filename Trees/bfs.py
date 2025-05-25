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

def breadthFirstSearch(root):
    try:
        data = [root]
        while(len(data) > 0):
            current_node = data.pop(0)
            print(current_node.val)
            if(current_node.left != None):
                data.append(current_node.left)
            if(current_node.right != None):
                data.append(current_node.right)
    except Exception as e:
        print(e)
        return
    
print(breadthFirstSearch(a))