'''
Погружение в Python (семинары)
Урок 4. Функции
Задание 2.
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
где ключ - значение переданного аргумента, а значение - имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.
'''
def func(**kwargs):
    def hashable(obj):
        try:
            hash(obj)
            return True
        except TypeError as _:
            return False

    return {val if hashable(val) else str(val): key for key, val in kwargs.items()}

print(f'new dict: {func(value=98, secret_val=99, levi_gin_list=[1,2,3,4,5,6,7,8,9,10,11], strange_name="Levi Gin", red_code=98)}')