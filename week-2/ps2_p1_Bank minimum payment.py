"""
inputs:
    balance: total balance at the beginning of the month
    months: placeholder for months
    
    figure out what the minimum omonthly payment is with interest applied to each month
    
    output remaining ballance after 12 months. 
"""
balance = 42
annualInterestRate = .2
monthlyPaymentRate = .04
months = 0

def pay(balance, months):
    payment = balance*monthlyPaymentRate
    #print(payment)
    unpaid = balance - payment
    #print(unpaid)
    balance = unpaid + (annualInterestRate/12)*unpaid
    #print(balance)
    months+=1
    if months == 12:
        return balance
    else:
        return pay(balance, months)
bal = pay(balance, months)
print('Remaining balance: '+str(round(bal,2)))
