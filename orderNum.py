def largest(n1, n2, n3):
    if (n1 > n2) and (n1 > n3):
        largest_num = n1
    elif (n2 > n1) and (n2 > n3):
        largest_num = n2
    else:
        largest_num = n3
    print("The largest of the 3 numbers is: ", largest_num)


def smallest(n1, n2, n3):
    if (n1 < n2) and (n1 < n3):
        smallest_num = n1
    elif (n2 < n1) and (n2 < n3):
        smallest_num = n2
    else:
        smallest_num = n3
    print("The smallest of the 3 numbers is: ", smallest_num)


num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")
largest(num1, num2, num3)
smallest(num1, num2, num3)