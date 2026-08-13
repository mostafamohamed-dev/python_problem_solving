# nested lists
if __name__ == "__main__":

    full_list = []
    sort_list = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        full_list.append([name, score])

    min_score = min(score for name, score in full_list)

    for name, score in full_list:
        if min_score == score:
            full_list.remove([name, score])

    secound_low = min(score for name, score in full_list)

    for name, score in full_list:
        if secound_low == score:
            sort_list.append(name)
    
    for index in sorted(sort_list) :
        print(index)
