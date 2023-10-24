for _ in range(int(input)):
    n = int(input())
    if n < 7 or n == 9:
        print('NO')
    elif n % 3 != 0:
        print(f'YES\n{n-3} {2} {1}')
    else:
        print(f'YES\n{n-5} {4} {1}')
