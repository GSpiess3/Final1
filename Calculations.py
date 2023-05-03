def add(num1, num2):

    return float(num1) + float(num2)

def sub(num1, num2):

    return float(num1) - float(num2)

def mult(num1, num2):

    return float(num1) * float(num2)

def div(num1, num2):

    if float(num2) == 0:
        raise ZeroDivisionError
        
    return float(num1) / float(num2)