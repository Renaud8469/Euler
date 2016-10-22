def is_palindrome(a):
    tostr = str(a)
    length = len(tostr)
    for i in range(0, length//2):
        if tostr[i] != tostr[length-1-i]:
            return False
    return True


def largest_palindrome_product():
    maximum = 10000
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i*j
            if is_palindrome(product) and product > maximum :
                maximum = product
    return maximum

print(largest_palindrome_product())
