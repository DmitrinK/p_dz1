"""
Пользователь вводит целое положительное число. Найдите самую большую цифру
в числе. Для решения используйте цикл while и арифметические операции.
"""
user_num = int(input(f"Введите целое положительное число: "))
max_num = 0
while user_num > 0:
    if max_num < user_num % 10:
        max_num = user_num % 10
        user_num = user_num // 10
    else:
        user_num = user_num // 10
print(f'Самая большая цифра в числе: {max_num}')
