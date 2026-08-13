# find the runner-up score
import math
import array

if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())

    arr = list(arr)
   
    max_arr = max(arr)

    while max_arr in arr:
        arr.remove(max_arr)

    print(max(arr))
