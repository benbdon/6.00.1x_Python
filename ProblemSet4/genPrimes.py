def genPrimes():
    prime = 2
    yield prime
    while True:
        prime += 1
        isPrime = True
        for x in range(2,prime):
            if prime % x == 0:
                isPrime = False
                break
        if isPrime == True:
                yield prime
        