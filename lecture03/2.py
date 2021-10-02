def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


while True:
    try:
        A = int(input("Введите число A: "))
        B = int(input("Введите число B: "))
        if gcd(A, B):
            print("Наибольший общий делитель чисел {A} и {B}:".format(A, B), gcd(A, B))
        else:
            print("Наибольший общий делитель не найден :(")
        exit(0)
    except (TypeError, ValueError) as e:
        print("Упс, что-то пошло не так, попробуйте снова ввести целые числа!")
