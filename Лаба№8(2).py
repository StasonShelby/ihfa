def f(x):
    return (1 + x ** 2 + x ** 4 + x ** 6) / (1 + x ** 3 + x ** 5 + x ** 7)

def calculate_P(y):
    P = (1.7 * f(0.25) + 2 * f(1 + y)) / (6 - f(y ** 2 - 1))
    return P

y = int(input("Введите действительное число: "))
result = calculate_P(y)
print(f"P = {result}")
