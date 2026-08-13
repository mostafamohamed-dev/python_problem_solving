# string validators
if __name__ == "__main__":
    s = input()
    flag1 = True
    flag2 = True
    flag3 = True
    flag4 = True
    flag5 = True

    for i in range(0, len(s)):
        if s[i].isalpha() or s[i].isdigit():
            flag1 = True

            break
        else:
            flag1 = False
    print(flag1)

    for i in range(0, len(s)):
        if s[i].isalpha():
            flag2 = True

            break
        else:
            flag2 = False
    print(flag2)

    for i in range(0, len(s)):
        if s[i].isdigit():
            flag3 = True

            break
        else:
            flag3 = False
    print(flag3)

    for i in range(0, len(s)):
        if s[i].islower():
            flag4 = True

            break
        else:
            flag4 = False
    print(flag4)

    for i in range(0, len(s)):
        if s[i].isupper():
            flag5 = True

            break
        else:
            flag5 = False
    print(flag5)
