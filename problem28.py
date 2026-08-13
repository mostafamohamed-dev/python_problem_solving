
# the minion game

def minion_game(string):
    string = string.upper()

    kevin = 0
    stuart = 0

    for i in range(len(string)):
        if string[i] in "AEIOU":
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
