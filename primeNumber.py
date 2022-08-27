# Prime Number: Number greater than 1 that has no positive divisors other 1 and itself
def prime_number(n):
    if n > 1:
        for i in range(2, n):
            if (num % i) == 0:
                print(num, " is not a prime number!")
                break
        else:
            print(num, " is a prime number!")
    else:
        print(num, " is not a prime number!")


num = int(input("Enter any positive number to check whether it is prime or not: "))
prime_number(num)
