def smallest_multiple(max_range):
    num = 1
    for i in range(1, max_range):
        if num % i == 0:
            continue
        else:
            for j in range(i-1, 0, -1):
                if i % j == 0:
                    num *= i // j
                    break
    return num

print(smallest_multiple(20))
