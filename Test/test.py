
print("Hello")


def boucle(a, n):
    for i in range(n):
        print(f"{a}")



def fibo(n):
    if n == 0 or n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)
