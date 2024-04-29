
def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res <= 1:
            print(f'{res} - ноль')
        for i in range(2, int(res**0.5) + 1):
            if res % i == 0:
                print(f'{res} - составное число')
                break
            print(f'{res} - простое число')
            break


    return wrapper


@is_prime
def sum_three(a, b, c):
    summ = a + b + c
    return summ

res = sum_three(2, 3, 78)
