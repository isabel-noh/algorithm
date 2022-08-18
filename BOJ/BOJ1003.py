def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
T = int(input())
for tc in range(T):
    count_0 = 0
    count_1 = 0
    print(fibonacci(int(input())))

    print(f'{count_0} {count_1}')
