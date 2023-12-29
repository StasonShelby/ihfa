def Palindrom(S):
    if len(S) <= 1:
        return True
    else:
        if S[0] == S[-1]:
            return Palindrom(S[1:-1])
        else:
            return False

# Пример использования
strings = ["radar", "level", "hello", "noon", "python"]
for s in strings:
    result = Palindrom(s)
    print(f"Строка '{s}' является палиндромом: {result}")
