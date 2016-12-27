class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', children=None, level=0):
        self.name = name
        self.children = []
        self.level = level
        self.win = 0
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

def build_tree(s, n):
	q = {n:1}
	t = Tree(q)
	t.level = 1
	bfs_queue = [t]
	while bfs_queue:
		node = bfs_queue.pop(0)
		# print(node.name)
		tried = []
		for i in node.name:
			for j in s:
				if i % j == 0:
					new_pile = int(i//j)
					a = dict(node.name)
					a[i] = a[i] - 1
					if a[i] == 0:
						del a[i]
					if not new_pile in a:
						a[new_pile] = 0
					a[new_pile] = a[new_pile] + j
					node.add_child(Tree(a,None,node.level + 1))
			pass
		pass
		bfs_queue.extend(node.children)
	return t

def compare_trees(t):
	if not t.children:
		if t.level % 2 == 0:
			print(t.level, t.name, 1)
			return 1
		else:
			print(t.level, t.name, 0)
			return 0

	for c in t.children:
		if compare_trees(c) == t.level % 2:
			print(t.level, t.name, t.level % 2)
			return t.level % 2
	print(t.level, t.name, (t.level + 1) % 2)	
	return (t.level + 1) % 2

first_input = input().split(" ")
second_input = input().split(" ")
# first_input = [10, 2]
# second_input = [2,5]

initial_pile = int(first_input[0])
size_of_set = int(first_input[1])

s = []
for i in range(0,size_of_set):
	s.append(int(second_input[i]))


t = build_tree(s, initial_pile)

if compare_trees(t) == 1:
	print("First")
else:
	print("Second")