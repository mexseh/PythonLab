a = [1, 2, 3, 4]
b = [11, 12, 13, 14]

a.append(10)
print(a)

a.extend(b)
print(a)

a = b.copy()
print(a)

a.sort(reverse=True)
print(a)

a.insert(2, 10)
print(a)

a.remove(10)
print(a)

a[1:2] = [6, 7]
print(a)

b.clear()
print(b)

