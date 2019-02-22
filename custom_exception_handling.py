class Error(Exception):
    ''' Base class for other exceptions '''
    # single line comment 
    pass

class ValueTooSmall(Error):
    ''' Value too small '''
    # single line comment 
    print('Printing from clss')
    pass

# Exception -> Error -> ValueTooSmall

class ValueTooLarge(Error):
    ''' Value too large '''
    # single line comment 
    pass

number = 10

while True:
    try:
        i_num = int(input('Enter a number : '))

        if i_num < number:
            raise ValueTooSmall
        elif i_num > number:
            raise ValueTooLarge
        else:
            break

    except ValueError:
        print('Its not number. Please enter number')
    
    except ValueTooSmall:
        print("You have entered small number.")
    except ValueTooLarge:
        print("You have entered large number.")