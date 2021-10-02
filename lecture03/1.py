def is_prime(x) -> bool:
    sq = int(x**0.5)
    for i in range(2, sq+1):
        if x % i == 0:
            return False
    return True


while True:
    try:
        N = int(input("Введите целое число N: "))
        primes = [x for x in range(2, N) if is_prime(x)]
        print("Простые числа от 2 до N:", *primes)
        exit(0)
    except (TypeError, ValueError) as e:
        print("Упс, что-то пошло не так, попробуйте снова ввести целое число!")
