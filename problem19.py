# python lists
f __name__ == '__main__':
    N = int(input())
    arr =[]
    list_v = []
    for i in range(0,N):
        list_v  = list(input().split())
        if list_v[0] == "append":
            arr.append(int(list_v[1]))
            list_v=[]
        elif list_v[0] == "insert":
            arr.insert(int(list_v[1] ),int(list_v[2]) )
            list_v=[]
        elif list_v[0] == "remove":
            arr.remove(int(list_v[1] ))
            list_v=[]
        elif list_v[0] == "sort":
            arr.sort()
        elif list_v[0] == "reverse":
            arr.reverse()
           
        elif list_v[0] == "pop":
            arr.pop()
            list_v=[]
        elif list_v[0] == "print":
            print(arr)
        
        

    
    
