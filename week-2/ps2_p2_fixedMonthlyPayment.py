"""
Take in a balance, annual interest rate, and calculate the minimum amount of time it will take to pay off a bank balance
"""

balance = 3063
annualInterestRate = .23
months = 0

assumed_payment = round(balance/12)
further_round = assumed_payment%10
if further_round != 0:
    assumed_payment += (10 - further_round)
    #print('assumed_payment: ' +str(assumed_payment))


def pay(balance, payment, months):
    unpaid = balance - payment
    balance = unpaid + (annualInterestRate/12)*unpaid
    months+=1
    #if months ==12:
    #    return 'small'
    if months == 12:
        #print('balance after 12 months: '+str(balance))
        #print('payment: '+str(payment))
        return balance
    else:
        return pay(balance, payment, months)

while True:

    bal = pay(balance, assumed_payment, months)
    #print(bal)
    if bal >=0:
        assumed_payment+=10
    else:
        break
print('Lowest Payment: '+str(assumed_payment))