balance = 320000
annualInterestRate = .2
monthlyInterestRate = annualInterestRate/12
lb = balance/12
up = (balance *(1+monthlyInterestRate)**12)/12
payment = (lb+up)/2
#print('lb: ' + str(lb))
#print('up: ' + str(up))
#print('1st payment: ' + str(payment))
months = 0

def pay(balance, payment, months):
    unpaid = balance - payment
    balance = unpaid + (annualInterestRate/12)*unpaid
    months+=1
    if balance <=0 and months <12:
        return balance
    elif months == 12:
        return balance
    else:
        return pay(balance, payment, months)

while True:
    bal = pay(balance, payment, months)

    if bal <=1 and bal>=-1:
        break
    elif bal <=0:
        #print('balance too low: '+str(bal))
        up = payment
        payment = (lb+up)/2
        #print('new payment: ' + str(payment))

    elif bal >=0:
        #print('balance too high: '+str(bal))
        lb = payment
        payment = (lb+up)/2
        #print('new payment: ' + str(payment))
print('Lowest Payment: '+str(round(payment,2)))
