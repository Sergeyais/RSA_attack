import random

def extendedEuclideanAlgorithm(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    def check_witness(a, d, n, s):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 1)
        if not check_witness(a, d, n, s):
            return False

    return True

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1
        if is_prime(num):
            return num


def generate_e(bits, p, q):
    phi = (p - 1) * (q - 1)
    x = bits
    while True:
        prime_number = generate_prime(512)
        if extendedEuclideanAlgorithm(prime_number, phi)[0] == 1:
            return prime_number
        x += 1

if __name__ == "__main__":
    p = generate_prime(512)
    print(p)
    q = generate_prime(512)
    print(q)
    e = generate_e(512, p, q)
    print(e)




