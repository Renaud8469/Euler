from math import sqrt


def nth_prime(n):
    prime_list = list()
    i = 2
    while len(prime_list) < n:
        is_prime = True
        for j in prime_list:
            if j > sqrt(i):
                break
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
        i += 1

    return prime_list[n-1]

print(nth_prime(10001))
