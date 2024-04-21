def pow_mod(a, b, n):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % n
        a = (a * a) % n
        b = b // 2
    return result

def reencryption_attack(y, e, n):
    y_i = y
    while True:
        y_i = pow_mod(y_i, e, n)
        if y_i == y:
            return y_prev
        y_prev = y_i


N = 143
e = 77
y = 121
# N = 84517
# e = 397
# y = 8646
# e, n = map(int, input("Enter public key (e, N): ").split())
# y = int(input("Enter encrypted message: "))
x = reencryption_attack(y, e, N)
print("Open text:", x)
