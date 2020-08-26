# C = (F - 32) * 5/9

# Run F input to C output

def C_temp():

    F_degree = int(input('How many degrees in Fahrenheit? '))
    C_degree = float(F_degree - 32) * (5/9)

    return C_degree

print(str(C_temp()) + 'C')