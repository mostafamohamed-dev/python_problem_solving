# merge the tools
def merge_the_tools(string, k):
   

   
    values = []
    s1 = ""
    split = len(string) // k

    for i in range(0, len(string)):
        s1 += string[i]
        if (i + 1) % k == 0:
            values.append(s1)
            s1 = ""

    for i in values:
        d = ""
        for chr in i:
            if chr not in d:
                d += chr
        print(d)
        d = ""


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
