class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', children=None, leaf=False):
        self.name = name
        self.children = []
        self.leaf = leaf
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

def has_letter(node, letter):
    for child in node.children:
        if child.name == letter:
            return child
    return None
        
def add_name(root, contact):
    node = root
    for letter in contact:
        next_node = has_letter(node, letter)
        if not next_node:
            next_node = Tree(letter)
            node.add_child(next_node)
        node = next_node
    node.leaf = True
    pass        

def find_contact(root, contact):
    node = root
    for letter in contact:
        node = has_letter(node, letter)
        if not node:
            return 0
        
    bfs = [node]
    con = 0
    while bfs:
        node = bfs.pop(0)
        if not node.children:
            con = con + 1
        else:
            if node.leaf: con = con + 1
            bfs.extend(node.children)
            pass
        pass
    return con

        
        
root = Tree("")
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    
    if op == "add":
        add_name(root, contact)
        
    if op == "find":
        print(find_contact(root, contact))
