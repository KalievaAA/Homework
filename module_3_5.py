def get_multiplied_digits(number):
    str_number = str(number)
    first = str_number[0]
    first = int(first)


    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    if first == 0:
        return 1
    else:
        return first

result1 = get_multiplied_digits(40203)
print(result1)

result2 = get_multiplied_digits(402030)
print(result2)
