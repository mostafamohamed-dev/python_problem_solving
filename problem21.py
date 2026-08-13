# swap case
def swap_case(s):
    list_v = list(s)
    s_copy = ""
    for i in range(0, len(s)):
        if list_v[i] == list_v[i].upper():
            list_v[i] = list_v[i].lower()
            s_copy += list_v[i]
        else:
            list_v[i] = list_v[i].upper()
            s_copy += list_v[i]

    return s_copy

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
