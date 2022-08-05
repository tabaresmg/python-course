def isPrime(num):
    var=False
    if num==2 or num==3:
        var=True
    elif num >1 and num %2 != 0 and num%3!=0:
        var=True
    else:
        var=False
    return var

for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()