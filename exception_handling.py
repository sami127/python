import sys
random_list = ['a',0,1]

for r in random_list:
    try:
        r = 1/int(r)
    except Exception as e:
        print('Ops exception occured')
        print('exception string is : ',e)
        print('exception name is : ',sys.exc_info()[0])
    except ValueError as e:
        print('exception string is : ',e)
    finally:
        print('I am in finally block')


