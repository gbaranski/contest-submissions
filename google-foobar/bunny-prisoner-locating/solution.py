def solution(x, y):
    a = 0
    b = 0
    for i in range(x):
        # print("Adding %s to a" % str(i+1))
        a += (i + 1)
    for i in range(x, x + y - 1):
        # print('Adding %s to b' % str(i))
        b += i
    return str(a + b)


print(solution(5, 10))
