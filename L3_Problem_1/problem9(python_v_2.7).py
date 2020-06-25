high = 100
low = 0
guess = (high + low) / 2

print "Please think of a number between 0 and 100!"

while True:
    print "Is your secret number", guess, "?"
    input_guy = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if input_guy == "h":
        high = guess
        guess = int(guess + low) / 2
        
    elif input_guy == "l":
        low = guess
        guess = int(guess + high) / 2
        
    elif input_guy == "c":
        break
        
    else:
        print "Sorry, I did not understand your input."
        
print "Game over. Your secret number was:", guess