balance = 12000
annualInterestRate = .12

bal = balance
monthlyInterestRate = annualInterestRate / 12
lowBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate)**12)/12.0
paymentGuess = (lowBound + upperBound)/2

while paymentGuess < balance:
    bal = balance
    paymentGuess = (lowBound + upperBound)/2
    for month in range(1,13):
        bal = bal - paymentGuess
        interest = bal * monthlyInterestRate
        bal += interest
    if abs(bal) <= 0.01:
        print "Lowest Payment: " + str(round(paymentGuess,2))
        break
    if bal > 0:
        lowBound = paymentGuess
    else:
        upperBound = paymentGuess