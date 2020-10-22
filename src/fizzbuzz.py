

def fizzbuzz(number):
    number_is_divisible_by_three = number % 3 == 0
    number_is_divisible_by_five = number % 5 == 0
    if number_is_divisible_by_three and number_is_divisible_by_five:
        return "fizzbuzz"
    elif number_is_divisible_by_three:
        return "fizz"
    elif number_is_divisible_by_five:
        return "buzz"
    return str(number)

