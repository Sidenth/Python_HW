# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = int(input("Введите Х "))
y = int(input("Введите Y "))
z = int(input("Введите Z "))
if (x==0 or x==1) and (y==0 or y==1) and (z==0 or z==1):
    res_1 = not(x or y or z)
    res_2 = not x and not y and not z
    if res_1==res_2:
        print("Утверждение верно ")
    else:
        print("Утверждение не верно ")
else:
    print("Неверные условия ввода ")