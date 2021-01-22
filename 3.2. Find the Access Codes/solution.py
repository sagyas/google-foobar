def solution(l):
    total = 0
    size = len(l)
    count = [0 for i in range(size)]
    if not size:
        return total
    for i in range(size):
        num1 = l[i]
        for j in range(i+1, size):
            num2 = l[j]
            if num2 % num1 == 0:
                count[j] += 1
                total += count[i]
    return total


# Test
l = [1, 1, 1]
answer = 1 # (1,1,1)
print(solution(l) == answer)

l = [1, 2, 3, 4, 5, 6]
answer = 3 # (1,2,4), (1,3,6), (1,3,6)
print(solution(l) == answer)