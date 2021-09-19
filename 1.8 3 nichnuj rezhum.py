X = int(input("Введіть к-сть хвилин"))
H = int(input("Введіть годину"))
M = int(input("Введіть хвилину"))

print(((H * 60) + X + M) // 60)
print((X + M) % 60)
