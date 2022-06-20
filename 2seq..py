
number = input("Введите элементы списка через запятую: ")

numbers = number.replace(',', ' ').replace(';', ' ').replace('/', ' ').split()

checklist = []
for element in numbers:
    if numbers.count(element) == 1:
        checklist.append(element)

print(checklist)









