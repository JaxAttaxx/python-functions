#Change over to odd
def is_odd(num):

    if num % 2 == 0:
        return False

    else:
        return True


def only_odds(list_of_numbers):
    odd_numbers = []
#loop over each item 
    for number in list_of_numbers:
#check if number is odd
        if is_odd(number):
#if odd append to even_numbers
            odd_numbers.append(number)
#return odd_numbers
    return odd_numbers



print(only_odds([11, 20, 42, 97, 23, 10]))