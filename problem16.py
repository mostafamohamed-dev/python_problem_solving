# finding the percentage
if __name__ == '__main__':
    n = int(input())
    sum = 0 
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    values = student_marks[query_name]
    for i in values :
        sum += i
    avg = sum/3
    
        
    print(f"{avg:.2f}")
