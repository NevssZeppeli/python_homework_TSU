# для ЕГЭ я использовал этот алгоритм, для решета Эратосфена напишу потом
#def is_prime(x) -> bool:
#    sq = int(x**0.5)
#    for i in range(2, sq+1):
#        if x % i == 0:
#            return False
#    return True


def is_prime(N):
    # это я делаю для того, чтобы само число N тоже проверялось!
    N += 1
    A = [True] * N
    A[0] = A[1] = False
    for k in range(2, int(N**0.5)):
        if A[k]:
            for m in range(2*k, N, k):
                A[m] = False
    return [k for k in range(N) if A[k]]


while True:
    try:
        N = int(input("Введите целое число N: "))
        print("Простые числа от 2 до N:", *is_prime(N))
        exit(0)
    except (TypeError, ValueError) as e:
        print("Упс, что-то пошло не так, попробуйте снова ввести целое число!", e)
