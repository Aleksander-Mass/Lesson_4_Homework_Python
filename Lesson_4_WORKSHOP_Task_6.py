'''
Погружение в Python (семинары)
Урок 4. Функции СЕМИНАР

Задание №6
Функция получает на вход список чисел и два индекса. 
Вернуть сумму чисел между между переданными индексами. 
Если индекс выходит за пределы списка, сумма считается 
до конца и/или начала списка.
'''
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index1 = 2
index2 = 6
a = len(list)
def sum_between_indexes(list, index1, index2):

  sum = 0
  if (index2 > a):
    for i in range((index1 + 1), a):
      sum += list[i]
  elif (index1 > index2) or (index1 < 0):
    for i in range(0, index2):
      sum += list[i]
  else:
    for i in range((index1 + 1), index2): # По условию: Вернуть сумму чисел между (!!! между) переданными индексами
      sum += list[i]

  return sum

print(sum_between_indexes(list, 2, 6))