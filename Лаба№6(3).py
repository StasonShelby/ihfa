import random
def task(list):
    el1 = 0
    for i in range(0, len(list) + 1):
        if list[i] > 0:
            el1 = list[i]
            break
    sum = 0
    k = i + 1
    while list[k] < 0:
        if list[k] == el1:
            continue
        else:
            sum += list[k]
            k += 1
    return sum
def transform_list(input_list):
    odd_elements = input_list[1::2]
    even_elements = input_list[::2]
    transformed_list = even_elements + odd_elements
    return transformed_list
try:
    n = int(input("Введите размер списка: "))
    a = int(input("Введите левый предел значений: "))
    b = int(input("Введите правый предел значений: "))
    list = [random.randint(a,b + 1) for i in range(n)]
except (IndexError,ValueError,TypeError):
    print("Введен неверный тип данных")
else:
    if n < 0:
        print("Размер списка не может быть отрицательным!")
    else:
        if n <= 2:
            print("Список должен состоять минимум из 3 элементов")
        else:
             print(list)
             print(task(list),transform_list(list))



