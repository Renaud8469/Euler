def sum_of_primes_below(a):
    prime_list = list()
    i = 2
    prime_sum = 0
    while i <= a:
        isprime = True
        for j in prime_list:
            if i % j == 0:
                isprime = False
                break
        if isprime:
            prime_list.append(i)
            prime_sum += i
        i += 1

    return prime_sum

# Complexity too high, must be worked on again
print(sum_of_primes_below(2000000))
