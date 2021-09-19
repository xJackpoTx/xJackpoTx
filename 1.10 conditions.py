x = int(input("Невідоме число"))
if x % 2 == 0:
    print("Парне")
else:
    print("Не парне")

x = int(input("Невідоме число"))
if x % 3 == 0:
    print("Ділиме на 3")
elif x % 3 == 1:
    print("решта тільки 1")
else:
    print("решта 2")

a = int(input())
b = int(input())
if a != b:
    if a > b:
        print('Перше число більше!')
    else:
        print('Друге число більше!')
else:
    print('Два числа рівні!')


a = int(input())
b = int(input())
if b != 0:
    print(a / b)
else:
    print('Ділення неможливе')
    b = int(input('Потрібно ввести не нульве значення'))
    if b == 0:
        print('Ви не впоралися!')
    else:
        print(a / b)
