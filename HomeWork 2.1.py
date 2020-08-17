def rec(a, b, k):
    while(a > 0 and b > 0):
        if a < b:
            k += 1
            l = b - a
            print("Квадрат с стороной ",a," Прямоугольник иммеет размер " ,a,"x",l)
            return rec(a,l,k)
        else:
            k += 1
            l = a - b
            print("Квадрат с стороной ",b," Прямоугольник иммеет размер:", l, "x",b)
            return rec(l, b, k)
    return print("Конец, всего ", k ,"квадратов")



k=0
a = int(input("Введите длину прямоугольника:\n"))
b = int(input("Введите ширену прямоугольника:\n"))
rec(a,b,k)