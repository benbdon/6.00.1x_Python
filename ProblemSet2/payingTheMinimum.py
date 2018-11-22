balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12
remBal = balance
totalPaid = 0

for month in range(1,13):
    print 'Month: ' + str(month)
    minPayment = monthlyPaymentRate * remBal
    totalPaid += minPayment
    print 'Minimum monthly payment: ' + str(round(minPayment,2))
    monthlyUnpaidBal = remBal - minPayment
    remBal = monthlyUnpaidBal + monthlyInterestRate * monthlyUnpaidBal
    print 'Remaining balanace: ' + str(round(remBal,2))

print 'Total paid: ' + str(round(totalPaid,2))
print 'Remaining balance: ' + str(round(remBal,2))