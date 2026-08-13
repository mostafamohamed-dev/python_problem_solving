# iterables and iterators
def print_from_stream(n, OddStream=1):
    if OddStream == 1:
        for i in range(0, n * 2):
            if i % 2 != 0:
                print(i)
    else:
        for i in range(0, n * 2):
            if i % 2 == 0:
                print(i)


n = int(input())
string = []
for i in range(0, n):
    string.append(input())
for i in string:
    name, value = i.split(" ")
    value = int(value)
    if name == "odd":
        print_from_stream(value)
    else:
        print_from_stream(value, 0)
