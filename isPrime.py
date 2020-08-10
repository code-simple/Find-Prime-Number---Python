def isPrime(n):
    if n==2 or n==3 or n==5:
        return True
    elif n==1 or n%2==0 or n%3==0 or n%5==0:
        return False
    else:
        for x in range(2,n):
            if n%x==0:
                return False
        return True

for i in range(1, 6850):
	if isPrime(i):
		print(i, end=" ")
