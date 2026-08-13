
# permutations
from itertools import permutations

string , k = input().split()
k=int(k)




for i in permutations(sorted(string), k):
    print(''.join(i))
    
