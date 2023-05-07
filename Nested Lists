def count(lst):
    a = min(lst)
    for i in range(N):
        if (lst[i] == a):
            i += 1
        else:
            return i


if __name__ == '__main__':
    student = []
    N = int(input())
    for i in range(N):
        name = input()
        score = float(input())
        student.append([name, score])

    marks = sorted(list([score for name, score in student]))
    req_index= count(marks)           
    sec_lowest = sorted(list([score for name, score in student]))[req_index]
    selected = sorted(list([name for name, score in student if score == sec_lowest]))
    print('\n'.join(selected))

