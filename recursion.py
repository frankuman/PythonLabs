
def multiply(m, n):

    if n == 0:
        print("--------")
        print("m = ", m)
        print("n = ", n)
        return 0
    if n > 0:
        print("m = ", m)
        print("n = ", n)
        return (m + multiply(m,n-1)) # 5 + (5) n = 3, + 5(n=2) + 5(n=1) + 5(n=0)
    if n < 0:
        return (- m + multiply(m,n-1))
## m * n 
results = 0
m = int(input("Skriv ditt första heltal: "))
n = int(input("Skriv ditt andra heltal: "))
print(multiply(m,n))
