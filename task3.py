numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

def filter_num(numbers):
    if(numbers % 2 and numbers > 50) != 0:
        return True
    else:
        return False

odd_numbers_over_50 = list(filter(filter_num, numbers))

print(odd_numbers_over_50)