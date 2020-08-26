def is_even(num):

    if num % 2 == 0:
        return True

    else:
        return False

#print(is_even(int(input('Number? '))))

def is_odd(num):

    return not is_even(num)
print(is_odd(int(input('Number? '))))
#print(num)

### below contains is_odd part.....needs 'not' keyword

