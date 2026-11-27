class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BST():
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while temp:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left

                if new_node.data > temp.data:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data,end=" ")
            self.inorder(rt.right)

    def search(self, key):
        if self.root.data == key:
            return True
        else:
            temp = self.root
            while temp:
                if key<temp.data:
                    temp = temp.left
                elif key>temp.data:
                    temp = temp.right
                else:
                    return True
            return False
                
    def minmax(self):
        if self.root is None:
            return
        else:
            temp = self.root
            while temp.left is not None:
                temp = temp.left
            print("min", temp.data)

            temp = self.root
            while temp.right is not None:
                temp = temp.right
            print("max", temp.data)

    def delete(self, rt, val):
        if rt is None:
            return
        else:
            if val < rt.data:
                rt.left = self.delete(rt.left,val)
            elif val > rt.data:
                rt.right = self.delete(rt.right,val)
            else:
                if rt.left is None:
                    return rt.right
                if rt.right is None:
                    return rt.left

                succ = self.get_successor(rt)
                rt.data = succ.data
                rt.right = self.delete(rt.right, succ.data)
        return rt

    def get_successor(self, rt):
        if rt is None:
            return
        temp = rt.right
        while temp and temp.left is not None:
            temp = temp.left
        return temp

b = BST()
b.insert(Node(50))
b.insert(Node(30))
b.insert(Node(70))
b.insert(Node(20))
b.insert(Node(40))
b.insert(Node(60))
b.insert(Node(80))
b.insert(Node(10))

b.inorder(b.root)
print(b.search(40))
b.minmax()
b.delete(b.root,70)
b.inorder(b.root)