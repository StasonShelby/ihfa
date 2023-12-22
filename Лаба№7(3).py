
input_string = input("Введите строку из чисел от 0 до 9: ")

count_dict = {}
for char in input_string:
    if char.isdigit():
        num = int(char)
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

print("Словарь с количеством повторений каждого числа:")
print(count_dict)

user_num = int(input("Введите число для проверки количества его повторений: "))
if user_num in count_dict:
    print(f"Число {user_num} встречается {count_dict[user_num]} раз(а) в строке.")
else:
    print(f"Число {user_num} не встречается в строке.")
