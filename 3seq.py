"""
number1 = input("Введите элементы 1-го списка через запятую: ")
number2 = input("Введите элементы 2-го списка через запятую: ")

numbers1 = number1.replace(',', ' ').replace(';', ' ').replace('/', ' ').split()
numbers2 = number2.replace(',', ' ').replace(';', ' ').replace('/', ' ').split()

checklist1 = {''}
for element in numbers1:
    checklist1.add(element)

checklist2 = {''}
for element in numbers2:
    checklist2.add(element)

for number in numbers1:
    if number in numbers2:
        numbers1.remove(number)

print(checklist1-checklist2)
"""
number_one = input("Введите элементы 1-го списка через запятую: ")
number_two = input("Введите элементы 2-го списка через запятую: ")
numbers_one = number_one.replace(',', ' ').replace(';', ' ').replace('/', ' ').split()
numbers_two = number_two.replace(',', ' ').replace(';', ' ').replace('/', ' ').split()
print(numbers_one)
print(numbers_two)
for number in numbers_one[:]:
    if number in numbers_two:
        numbers_one.remove(number)
print(numbers_one)


