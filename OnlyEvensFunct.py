
def is_even(num):

    if num % 2 == 0:
        return True

    else:
        return False


def only_evens(list_of_numbers):
    even_numbers = []
#loop over each item 
    for number in list_of_numbers:
#check if number is even
        if is_even(number):
#if even append to even_numbers
            even_numbers.append(number)
#return even_numbers
    return even_numbers


print(only_evens([11, 20, 42, 97, 23, 10]))


