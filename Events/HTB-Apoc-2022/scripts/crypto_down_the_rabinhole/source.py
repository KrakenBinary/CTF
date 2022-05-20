from Crypto.Util.number import getPrime, isPrime, bytes_to_long
from Crypto.Util.Padding import pad
import os


FLAG = b"HTB{--REDACTED--}"


def getPrimes(coefficient):
    print('-=PRIME:1=-')
    while True:
        a = getPrime(512)
        p = 3 * coefficient * a + 2
        if isPrime(p):
            break
    print('-=PRIME:2=-')
    while True:
        b = getPrime(512)
        q = 3 * coefficient * b + 2
        if isPrime(q):
            break
    return p, q


def encrypt(message, coefficient):
    print('-=ENCRYPT:1=-')
    p, q = getPrimes(coefficient)
    n = p * q

    print('-=ENCRYPT:2=-')
    padded_message = bytes_to_long(pad(message, 64))
    message = bytes_to_long(message)

    print('-=ENCRYPT:3=-')
    c1 = (message * (message + coefficient)) % n
    c2 = (padded_message * (padded_message + coefficient)) % n
    return (n, c1, c2)


def main():
    print('-=MAIN:1=-')
    coefficient = getPrime(128)
    out = ""

    print('-=MAIN:2=-')
    message = FLAG[0:len(FLAG)//2]
    n1, c1, c2 = encrypt(message, coefficient)
    out += f"{n1}\n{c1}\n{c2}\n"
    print(out)

    print('-=MAIN:3=-')
    message = FLAG[len(FLAG)//2:]
    n2, c3, c4 = encrypt(message, coefficient)
    out += f"{n2}\n{c3}\n{c4}"
    print(out)

    print('-=MAIN:4=-')
    with open("out.txt", "w") as f:
        f.write(out)


if __name__ == '__main__':
    print('-=START=-')
    main()
