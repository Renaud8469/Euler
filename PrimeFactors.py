from math import sqrt


def highestprimefactor(a):
    num = a
    maxprime = 1
    primelist = list()
    i = 2
    while i <= num:
        isprime = True
        for j in primelist:
            if j > sqrt(i):
                break
            if i % j == 0:
                isprime = False
                break
        if isprime:
            primelist.append(i)
            while num % i == 0:
                maxprime = i
                num /= i
        i += 1

    return maxprime

print(highestprimefactor(600851475143))
