def solution(x, y):
    lower_bound = y
    upper_bound = x + y
    id = 0 
    for i in range(lower_bound, upper_bound):
        id += i
    u_bound = y - 1
    for i in range(1, u_bound):
        id += i
    return str(id)

# Test
x = 3
y = 2
answer = "9"
print(solution(x, y) == answer)

x = 5
y = 10
answer = "96"
print(solution(x, y) == answer)

print(solution(4, 5))