def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def goldbach_conjecture(n):
    if n <= 2 or n % 2 != 0:
        print("Число должно быть четным и больше 2")
        return
    primes = [i for i in range(2, n) if is_prime(i)]
    for prime in primes:
        if is_prime(n - prime):
            print(f"{n} = {prime} + {n - prime}")

# Пример использования
n = int(input("Введите число: "))
goldbach_conjecture(n)
