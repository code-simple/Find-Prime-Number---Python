def isPrime(n):
    if n==1:
        return False
    elif n==2:
        return True
    else:
        for x in range(2,n):
            if n%x==0:
                return False
        return True

for i in range(1, 100):
	if isPrime(i + 1):
			print(i + 1, end=" ")
