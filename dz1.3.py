"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
user_num = int(input(print("Введите число n")))
answer = user_num + user_num * 11 + user_num * 111
print(answer)
