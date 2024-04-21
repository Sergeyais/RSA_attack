import math

def wiener_attack(e, n):
    def continued_fraction(e, n):
        cf = []
        while n != 0:
            q = e // n
            cf.append(q)
            e, n = n, e - q * n
        return cf

    def convergents(cf):
        p_minus_2, p_minus_1, q_minus_2, q_minus_1 = 1, 0, 0, 1
        
        for i in cf:
            p = i * p_minus_1 + p_minus_2
            q = i * q_minus_1 + q_minus_2
            
            yield q, p
            
            p_minus_2, p_minus_1 = p_minus_1, p
            q_minus_2, q_minus_1 = q_minus_1, q

    cf = continued_fraction(e, n)
    for k, d in convergents(cf):
        if k != 0:
            phi = (e * d - 1) // k
            discriminant = (n - phi + 1) ** 2 - 4 * n
            if discriminant < 0:
                continue
            sqrt_discriminant = math.sqrt(discriminant)
            if sqrt_discriminant.is_integer():
                x1, x2 = ((n - phi + 1) + sqrt_discriminant)//2, ((n - phi + 1) - sqrt_discriminant)//2
                if x1 * x2 == n:
                    return d
    return None

e = 14187
n = 21583
# e, n = map(int, input("Enter public key (e, N): ").split())
d = wiener_attack(e, n)
if d:
    print(f"Private key found (d, N): {d, n}")
else:
    print("Attack Wiener fails😭")
