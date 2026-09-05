if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    unique_scores = []
    for student in students:
        score = student[1]
        if score not in unique_scores:
            unique_scores.append(score)
    unique_scores.sort()
    second_lowest_score = unique_scores[1]
    
    # collect names with the second lowest score
    second_lowest_names = []
    for student in students:
        if student[1] == second_lowest_score:
            second_lowest_names.append(student[0])
    second_lowest_names.sort()
    
    for name in second_lowest_names:
        print(name)