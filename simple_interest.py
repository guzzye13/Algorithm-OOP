# Simple interest = (Principal amount * Rate of interest * Number of years) / 100
def simple_interest_calculator(p, r, t):
    simpleInterest = (principal * rate * time) / 100
    return simpleInterest


principal = float(input('Enter principal amount: '))
rate = float(input('Enter interest amount: '))
time = float(input('Enter number of years: '))


print('Simple interest: {0}'.format(simple_interest_calculator(principal, rate, time)))
