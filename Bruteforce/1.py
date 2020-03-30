def solution(answers):
    answer = []
    ans = [0] * 3
    a1 = [i%5 + 1 for i in range(len(answers))]
    a2 = [2 if i%2==0 else 4 if i%8==5 else 5 if i%8==7 else i%8 for i in range(len(answers))]
    tmp3 = [3, 1, 2, 4, 5]
    a3 = [tmp3[i%5] for i in range(len(answers)) for _ in range(2)]
    a3 = a3[:int(len(a3)/2)]
    for i in range(len(answers)):
        if answers[i] == a1[i]:
            ans[0] += 1
        if answers[i] == a2[i]:
            ans[1] += 1
        if answers[i] == a3[i]:
            ans[2] += 1
    if ans[0] >= ans[1] and ans[0] >= ans[2]:
        answer.append(1)
    if ans[1] >= ans[0] and ans[1] >= ans[2]:
        answer.append(2)
    if ans[2] >= ans[0] and ans[2] >= ans[1]:
        answer.append(3)
    return answer