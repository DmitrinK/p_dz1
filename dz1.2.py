"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и
секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
user_time = int(input(f"Введите колличество секунд: "))
watch = user_time // 3600
minutes = user_time // 60 % 60
seconds = user_time % 60
if watch > 10:
    print(f'{watch}:{minutes}:{seconds}')
else:
    print(f'0{watch}:{minutes}:{seconds}')
