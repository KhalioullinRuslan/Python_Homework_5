# Задача калькулятор.
# Решать только через рекурсию!
# Пользоваться встроенными функциями вычисления таких выражений нельзя, 
# если только для проверки вашего алгоритма.
# на вход подается строка из операторов 
# / * + - и целых чисел. Надо посчитать результат введенного выражения.
# Например:
# На входе: 1+9/3*7-4
# На выходе: 18


def ret(s):
    s = str(s)
    if s.isdigit():
        return float(s)
    for _ in ('-','+','*','/'):
        left, op, right = s.partition(c)
        if op == '*':
            return ret(left) * ret(right)
        elif op == '/':
            return ret(left) / ret(right)
        elif op == '+':
            return ret(left) + ret(right)
        elif op == '-':
            return ret(left) - ret(right)
print(eval(input('Введите математическое выражение: ')))
