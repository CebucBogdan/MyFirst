input_ok = True

while input_ok == True:
    user_input = int(input('user input = '))
    if user_input == x:
        print('You won!')
    else:
        print('You lost!')
        print('The number was', x)
    question = input('Do you want to continue? yes/no: ')
    if question == 'yes':
        input_ok = True
    else:
        input_ok = False
        print('You wont, oke, have a nice day' )
        print('Good Bye')