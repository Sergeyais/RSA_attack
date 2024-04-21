def pow_mod(a, b, n):
    if b < 0:
        g, _, _ = extendedEuclideanAlgorithm(a, n)
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % n
        a = (a * a) % n
        b = b // 2
    return result

def extendedEuclideanAlgorithm(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

e1, N = map(int, input("Enter public key 1 (e, N): ").split())
e2, N = map(int, input("Enter public key 2 (e, N): ").split())
y1 = int(input("Enter encrypted message 1: "))
y2 = int(input("Enter encrypted message 2: "))
e1, N = 191, 137759
e2, N = 233, 137759
y1 = 60197
y2 = 63656

_, r, s = extendedEuclideanAlgorithm(e1, e2)
# r = r % N
# s = s % N
res = (pow(y1, r, N) * pow(y2, s, N)) % N
print(f"Open text: {res}")