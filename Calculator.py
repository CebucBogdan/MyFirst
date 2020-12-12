print('My first Calculator')
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def nums_input():
    a = float(input('first num = '))
    b = float(input('second num = '))
    return a, b


def chooice():
    global  user_choice
    user_input = True
    while user_input == True:
        print('1.Add')
        print('2.Substract')
        print('3.Multiply')
        print('4.Divide')
        print('-'*50)
        user_choice = input('What type of operation do you prefer? ')
        if user_choice in ('1','2','3','4'):
            user_input = False
        else:
            print('Your selection is not in our meniu')
            user_input = True
    print('-'*25)
    return user_choice


finished = False
while finished == False:
    result = 0
    my_chooice = chooice()
    x, y = nums_input()
    if my_chooice == '1':
        result = add(x, y)
    if my_chooice == '2':
        result = substract(x, y)
    if my_chooice == '3':
        result = multiply(x, y)
    if my_chooice == '4':
        result = divide(x, y)
    print('-'*50)
    print('Result is {}'.format(result))
    print('-'*50)
    user_ask = input('Do you want to make another operation? yes/no: ')
    if user_ask == 'yes':
        finished = False
    else:
        print('Have a nice day!')
        finished = True
