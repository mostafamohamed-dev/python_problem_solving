# set symmetric difference


n = int(input())

v1 = set(map(int , input().split()))
m= int(input())
v2 = set(map(int , input().split()))

print(len(v1.symmetric_difference(v2)))
