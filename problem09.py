# separate string by max_char

import textwrap


def wrap(string, max_width):
    sub = ""
    i = 0
    for iter in string:
        sub += iter
        i += 1

        if i % max_width == 0:
            sub += "\n"

    return sub




if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
