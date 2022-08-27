def largest_number(numbers):
    biggest_num = numbers[0]
    for num in numbers:
        if num > biggest_num:
            biggest_num = num
    return biggest_num


def smallest_number(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num


print(largest_number([-201, 4, 62, 61]))
print(smallest_number([-201, 4, 62, 61]))
