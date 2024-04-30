# Функция с произвольным числом параметров разного типа
def test(*args):
    for arg in args:
        print(arg)

# Рекурсивная функция для вычисления факториала числа n
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Пример использования функций
test(1, 'hello', True, 3.14)
print("Факториал числа 5:", factorial(5))
