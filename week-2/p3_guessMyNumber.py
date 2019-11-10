low = 0
high = 100
print('Please think of a number between 0 and 100!')
#while True:
#    x = input('Please think of a number between 0 and 100!')
#    if int(x)<100 and int(x)>0:
#        break
#    else:
#        print("Sorry, I did not understand your input.")


while True:
    y = (high+low)//2
    print('Is your secret number: '+str(y) +'?')
    inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if str(inp) == "h":
        high = y
       # x = y
    elif str(inp) == "l":
        low = y
        #x = y
    elif inp == 'c':
        print("Game over. Your secret number was: "+str(y))
        break
    else:
        print("Sorry, I did not understand your input.")
