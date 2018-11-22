low = 0
high = 100
compGuess = 50

print "Please think of a number between 0 and 100!"

while True:
    print "Is your secret number " + str(compGuess) + "?"
    char = raw_input("Enter 'h' to indicate the guess is too high. "\
    "Enter 'l' to indiciate the guess is too low. "\
    "Enter 'c' to indicate I guesssed correctly. ")
    if char == 'c':
        print 'Game over. Your secret number was: ' + str(compGuess)
        break    
    elif char == 'l':
        low = compGuess
        compGuess = (low + high)/2
    elif char == 'h':
        high = compGuess
        compGuess = (low + high)/2
    else:
        print 'Sorry, I did not understand your input'