# s = input("Введите строку: ")
# result = ''
# for i in s:
#     if i == 'a':
#         i = 'A'
#     if i == 's':
#         i = 'S'
#     if i == 'd':
#         i = 'D'
#     if i == 'f':
#         i = 'F'
#     if i == 'g':
#         i = 'G'
#     if i == 'h':
#         i = 'H'
#     if i == 'j':
#         i = 'J'
#     if i == 'k':
#         i = 'K'
#     if i == 'l':
#         i = 'L'
#     if i == 'q':
#         i = 'Q'
#     if i == 'w':
#         i = 'W'
#     if i == 'e':
#         i = 'E'
#     if i == 'r':
#         i = 'R'
#     if i == 't':
#         i = 'T'
#     if i == 'y':
#         i = 'Y'
#     if i == 'u':
#         i = 'U'
#     if i == 'i':
#         i = 'I'
#     if i == 'o':
#         i = 'O'
#     if i == 'p':
#         i = 'P'
#     if i == 'z':
#         i = 'Z'
#     if i == 'x':
#         i = 'X'
#     if i == 'c':
#         i = 'C'
#     if i == 'v':
#         i = 'V'
#     if i == 'b':
#         i = 'B'
#     if i == 'n':
#         i = 'N'
#     if i == 'm':
#         i = 'M'
#     if i == 'i':
#         i = 'I'
#     if i == 'с':
#         i = 'С'
#     if i == 'а':
#         i = 'А'
#     if i == 'н':
#         i = 'Н'
#     if i == 'я':
#         i = 'Я'
#     if i == 'д':
#         i = 'Д'
#     if i == 'и':
#         i = 'И'
#     if i == 'х':
#         i = 'Х'
#     if i == 'й':
#         i = 'Й'
#     if i == 'к':
#         i = 'К'
#     if i == 'г':
#         i = 'Г'
#     if i == 'о':
#         i = 'О'
#     if i == 'л':
#         i = 'Л'
#     if i == 'ж':
#         i = 'Ж'
#     if i == 'э':
#         i = 'Э'
#     if i == 'ш':
#         i = 'Ш'
#     if i == 'щ':
#         i = 'Щ'
#     if i == 'ц':
#         i = 'Ц'
#     if i == 'у':
#         i = 'У'
#     if i == 'т':
#         i = 'Т'
#     if i == 'в':
#         i = 'В'
#     if i == 'ф':
#         i = 'Ф'
#     result += i
# print(result)

try:
 S = input("Введите строку: ")
except:
  if S.isdigit():
   print("Строка должна состоять из букв")
else:
 result = ''
 for i in S:
  x = ord(i)
  if x in range(97, 97+26) or x in range(1072, 1072+33):
   i = chr(x-32)
   result += i
 print(result)









# i = input("Введите символ: ")
# x = ord(i)
# print(x)


