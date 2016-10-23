def sum_square(a):
    sum_sq = 0
    for i in range(1, a+1):
        sum_sq += i*i
    return sum_sq


def square_sum(a):
    sq_sum = sum(range(1, a+1))
    return sq_sum*sq_sum


def sq_sum_diff(a):
    return square_sum(a) - sum_square(a)

print(sq_sum_diff(100))
