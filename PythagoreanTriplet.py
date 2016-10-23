def is_pythagorean_triplet(a, b, c):
    return a*a + b*b == c*c


def product_special_pythagorean_triplet():
    for a in range(3, 333):
        for b in range(4, 499):
            for c in range(5, 994):
                if a + b + c == 1000 and is_pythagorean_triplet(a, b, c):
                    return a*b*c


print(product_special_pythagorean_triplet())
