from fractions import Fraction, gcd


def solution(m):
    tmat = transform(m)
    sfmat, non_abs = standard_form(tmat)
    R = getR(sfmat, non_abs)
    Q = getQ(sfmat, non_abs)
    q_len = len(Q)
    i_mat = [[0 for x in range(q_len)] for y in range(q_len)]
    for i in range(q_len):
        i_mat[i][i] = 1
    f = subtract(i_mat, Q)
    f = inverse(f)
    tmat = mat_mult(f, R)
    row = tmat[0]
    l = 1
    for item in row:
        l = lcm(l, item.denominator)
    tmat = list(map(lambda x: (x.numerator*l/x.denominator), row))
    tmat.append(l)
    return tmat


def subtract(mat1, mat2):
    result = []
    size = len(mat1)
    for i in range(size):
        r1 = mat1[i]
        r2 = mat2[i]
        r = []
        for j in range(size):
            item = r1[j] - r2[j]
            r.append(item)
        result.append(r)
    return result


def getR(mat, non_abs):
    length = len(mat)
    m = min(non_abs)
    middle = length/2
    result = []
    for i in range(m, length):
        row = mat[i]
        new_row = []
        for j in range(0, middle+1):
            new_row.append(row[j])
        result.append(new_row)
    return result


def getQ(mat, non_abs):
    length = len(mat)
    m = min(non_abs)
    middle = length/2
    result = []
    for i in range(m, length):
        row = mat[i]
        new_row = []
        for j in range(middle+1, length):
            new_row.append(row[j])
        result.append(new_row)
    return result


def standard_form(tmat):
    abs = []
    non_abs = []
    length = len(tmat)
    for i in range(length):
        row = tmat[i]
        if(is_abs(row)):
            abs.append(i)
        else:
            non_abs.append(i)
    order = abs + non_abs
    result = order_mat(tmat, order)
    result2 = []
    for x in non_abs:
        result2.append(order.index(x))
    return result, result2


def order_mat(tmat, order):
    length = len(order)
    result = [[0 for i in range(length)] for x in range(length)]
    for i in range(length):
        row = tmat[i]
        for j in range(length):
            item = row[j]
            result[order.index(i)][order.index(j)] = item
    return result


def is_abs(row):
    if sum(row, 0) == 0:
        return True
    return False


def lcm(x, y):
    return x*y/gcd(x, y)


def transform(mat):
    length = len(mat)
    new_mat = []
    for i in range(length):
        row = mat[i]
        new_row = []
        row_sum = sum(row, 0)
        for x in row:
            item = Fraction(0, 1)
            if x != 0:
                item = Fraction(x, row_sum)
            new_row.append(item)
        new_mat.append(new_row)
    return new_mat


def copy_mat(mat):
    cmat = []
    length = len(mat)
    for i in range(length):
        new_row = []
        for j in range(length):
            cell = mat[i][j]
            new_row.append(cell)
        cmat.append(new_row)
    return cmat


def gauss_elmination(m, values):
    mat = copy_mat(m)
    for i in range(len(mat)):
        index = -1
        for j in range(i, len(mat)):
            if mat[j][i].numerator != 0:
                index = j
                break
        if index == -1:
            raise ValueError('Gauss elimination failed!')
        mat[i], mat[index] = mat[index], mat[j]
        values[i], values[index] = values[index], values[i]
        for j in range(i+1, len(mat)):
            if mat[j][i].numerator == 0:
                continue
            ratio = -mat[j][i]/mat[i][i]
            for k in range(i, len(mat)):
                mat[j][k] += ratio * mat[i][k]
            values[j] += ratio * values[i]
    res = [0 for i in range(len(mat))]
    for i in range(len(mat)):
        index = len(mat) - 1 - i
        end = len(mat) - 1
        while end > index:
            values[index] -= mat[index][end] * res[end]
            end -= 1
        res[index] = values[index]/mat[index][index]
    return res


def transpose(mat):
    tmat = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == 0:
                tmat.append([])
            tmat[j].append(mat[i][j])
    return tmat


def inverse(mat):
    tmat = transpose(mat)
    mat_inv = []
    for i in range(len(tmat)):
        values = [Fraction(int(i == j), 1) for j in range(len(mat))]
        mat_inv.append(gauss_elmination(tmat, values))
    return mat_inv


def mat_mult(mat1, mat2):
    result = []
    length1 = len(mat1)
    length2 = len(mat2)
    for i in range(length1):
        new_row = []
        result.append(new_row)
        for j in range(len(mat2[0])):
            result[i].append(Fraction(0, 1))
            for k in range(length2):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

# Test
m = [
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
answer = [7, 6, 8, 21]
print(solution(m) == answer)

m = [
            [0, 1, 0, 0, 0, 1],
            [4, 0, 0, 3, 2, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
answer = [0, 3, 2, 9, 14]
print(solution(m) == answer)
