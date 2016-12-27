n = 5
k = 4
a = [1,2,3,4,5]

b = a[k:]
b.extend(a[:k])
print(b)