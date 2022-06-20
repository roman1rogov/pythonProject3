
checklist = []

count = int(input("Введите количество элементов: "))

for i in range(count):

    element = int(input("Введите элемент: "))

    checklist.append(element)


checklist.sort()

print(checklist)
