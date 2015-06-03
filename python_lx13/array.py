b = []
a = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for elements in a:
    for j in elements:
        print elements, j
        b.append((elements,j))

print b
