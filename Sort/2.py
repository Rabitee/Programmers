def solution(numbers):
    answer = ''
    length = len(str(max(numbers)))
    def f(x):
        for i in range(length - len(x)):
            x += x[i]
        return x
    l = list(map(str, numbers))
    l = sorted(l, key=f, reverse=True)
    if max(numbers) == 0:
        return '0'
    return ''.join(l)


numbers = [0, 0]
print(solution(numbers))