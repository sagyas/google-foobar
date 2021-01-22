from fractions import Fraction as frac


def solution(pegs):
    num_pegs = len(pegs)
    first_r = None

    if num_pegs % 2 != 0:
        first_r = solve_odd(pegs)

    else:
        first_r = solve_even(pegs)

    cur_r = first_r
    for i in range(num_pegs - 2):
        dist = pegs[i + 1] - pegs[i]
        next_r = dist - cur_r
        if cur_r < 1 or next_r < 1:
            return -1, -1
        else:
            cur_r = next_r

    return first_r.numerator, first_r.denominator


def solve_odd(pegs):
    pegs_len = len(pegs)
    mid = ((-1) * pegs[0] - pegs[pegs_len - 1])
    for i in range(1, pegs_len - 1):
        mid += 2 * (-1)**(i + 1) * pegs[i]
    first_radius = frac(2 * mid).limit_denominator()
    return first_radius


def solve_even(pegs):
    pegs_len = len(pegs)
    mid = ((-1) * pegs[0] + pegs[pegs_len - 1])
    for i in range(1, pegs_len - 1):
        mid += 2 * (-1)**(i + 1) * pegs[i]
    first_radius = frac(2 * (float(mid) / 3)).limit_denominator()
    return first_radius

# Test
pegs = [4, 30, 50]
answer = (12, 1)
print(solution(pegs) == answer)

pegs = [4, 17, 50]
answer = (-1, -1)
print(solution(pegs) == answer)