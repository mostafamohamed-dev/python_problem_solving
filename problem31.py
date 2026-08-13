# cartesian product
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))

result = []
value = ()

for i in a:
    for j in b:
        value = (i, j)
        result.append(value)

for i in result:
    print(i, end=" ")
