import random
import math
from Generate_key import generate_prime, generate_e



def text_to_binary_ascii(text):
    binary_representation = ''.join(format(ord(char) & 0xFF, '08b') for char in text)
    return binary_representation

def binary_to_text_ascii(binary_string):
    while len(binary_string) % 8 != 0:
        binary_string = '0' + binary_string
    byte_list = [chr(int(binary_string[i:i + 8], 2)) for i in range(0, len(binary_string), 8)]
    decoded_text = ''.join(byte_list)
    return decoded_text

def pow_mod(a, b, n):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % n
        a = (a * a) % n
        b = b // 2
    return result

def del_zero(binary_string):
    k = 0
    for i in binary_string:
        if i == '0':
            k += 1
        elif i == '1':
            break
    if k != 0:
        binary_string = binary_string[((k//8) * 8):]
    while len(binary_string) % 8 != 0 and binary_string[0] == '0':
        binary_string = binary_string[1:]
    return binary_string


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def split_and_pad_binary_string(binary_string, k):
    length = len(binary_string)
    num_blocks = (length + k - 1) // k
    blocks = []
    for i in range(num_blocks):
        start = max(length - (i + 1) * k, 0)
        end = length - i * k
        block = binary_string[start:end]
        if i == num_blocks - 1 and len(block) < k:
            block = '0' * (k - len(block)) + block
        blocks.append(block)
    return blocks



def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime


def extendedEuclideanAlgorithm(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def encrypt(e, n, binary_string):
    cipher_binary = ''
    log_down = math.floor(math.log2(n))
    log_up = math.ceil(math.log2(n))
    blocks = split_and_pad_binary_string(binary_string, log_down)
    for i in range(len(blocks) - 1, -1, -1):
        number = int(blocks[i], 2)
        number_encrypt = encrypt_number(number, e, n)
        cipher_bin = str(bin(number_encrypt))[2:]
        while len(cipher_bin) < log_up:
            cipher_bin = '0' + cipher_bin
        cipher_binary += cipher_bin

    return cipher_binary


def decrypt(d, n, binary_string):
    open_binary = ''
    log_down = math.floor(math.log2(n))
    log_up = math.ceil(math.log2(n))
    blocks = split_and_pad_binary_string(binary_string, log_up)
    for i in range(len(blocks) - 1, -1, -1):
        number = int(blocks[i], 2)
        number_encrypt = decrypt_number(number, d, n)
        cipher_bin = str(bin(number_encrypt))[2:]
        while len(cipher_bin) < log_down:
            cipher_bin = '0' + cipher_bin
        open_binary += cipher_bin
    return open_binary

def encrypt_number(x, e, n):
    return pow_mod(x, e, n)

def decrypt_number(x, d, n):
    return pow_mod(x, d, n)


def modularInverse(a, m):
    gcd, x, y = extendedEuclideanAlgorithm(a, m)
    if gcd != 1:
        raise ValueError(f"The modular inverse does not exist for {a} modulo {m}")
    else:
        return x % m

def generate_key():
    p = generate_prime(512)
    q = generate_prime(512)
    e = generate_e(512, p, q)
    return p, q, e

def configurate_key():
    p = 12345141716564547852219131387337094825475326566953395165669439557878159335945064957745820241213030816394409657789785229831658671245005698259036306984989803
    q = 7444412843530608582007560449935595681259604694622952244602906288023657858257171617396700856639228003507330273629780917377961377286401491980413021122118377
    e = 65537
    return p, q, e



if __name__ == '__main__':
    action_key = int(input('Enter action 1 - Key generation 2 - Select the specified key: '))
    if action_key == 1:
        p, q, e = generate_key()
    elif action_key == 2:
        p, q, e = configurate_key()
    n = p * q
    phi = (p - 1) * (q - 1)
    d = modularInverse(e, phi)
    public_key = (e, n)
    private_key = (d, n)


    print(f'public_key: {public_key}')
    print(f'private_key: {private_key}')

    action = int(input('Enter action 1 - encryption 2 - decryption: '))

    if action == 1:
        path = str(input('Enter the filename in the current directory: '))
        with open(path, 'r') as file:
            content = file.read()

        binary = text_to_binary_ascii(content)
        a = encrypt(e, n, binary)
        with open(path[:-4] + '_encrypted.txt', 'w') as file:
            file.write(binary_to_text_ascii(a))
    elif action == 2:
        path = str(input('Enter the filename in the current directory: '))
        with open(path, 'r', newline='') as file:
            content = file.read()
        binary = text_to_binary_ascii(content)
        b = decrypt(d, n, binary)
        b = del_zero(b)

        with open(path[:-4] + '_deciphered.txt', 'w') as file:
            file.write(binary_to_text_ascii(b))
















