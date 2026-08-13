# mutate string
def mutate_string(string, position, character):
    list_s = list(string)
    list_s[position]=character
    string = "".join(list_s)
    
    
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
