def is_prime(number):
    if number > 1:
        if number == 2 or number == 3 or number == 5 or number == 7:
            return True
        elif number % 6 == 1 or number % 6 == 5:
            return True
        else:
            return False
    else:
        return False
