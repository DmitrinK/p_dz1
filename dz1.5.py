"""
Запросите у пользователя значения выручки и издержек фирмы. Определите,
с каким финансовым результатом работает фирма (прибыль — выручка больше
издержек, или убыток — издержки больше выручки). Выведите соответствующее
сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
и определите прибыль фирмы в расчете на одного сотрудника.
"""
user_profit = int(input(print("Введите значения выручки:")))
user_costs = int(input(print("Введите и издержек:")))
if user_profit > user_costs:
    print('Фирма работает с прибылью')
    user_profitability = round((user_profit - user_costs)/user_profit, 2)
    print(f'рентабельность выручки составила: {user_profitability}')
    num_of_employees = int(input(print("Введите численность сотрудников:")))
    profit_employees = round(user_profit / num_of_employees, 2)
    print(f'прибыль фирмы в расчете на одного сотрудника: {profit_employees}')
else:
    print('Фирма работает с Убытком')