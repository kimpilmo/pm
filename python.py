from time import time
#iteracti
def iterfibo(n):

    count = 1
    f0, f1 = 0, 1

    while n >= 2 and count < n:

        temp = f0 + f1
        f0 = f1
        f1 = temp
        count += 1

    return f1
#recursive function
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


"""while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time()
    fibonumber = iterfibo(nbr)
    ts = time() - ts
    print("Fibo(%d) = %d, time = %.6f " %(nbr, fibonumber, ts))"""


