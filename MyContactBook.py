print('Contact Book')

input_ok = True
while input_ok == True:

    # name
    first_name = input('Introduce first name: ')
    second_name = input('Introduce second name: ')
    storage_name = first_name + ' ' + second_name
    # phone number
    phone = input('Introduce phone number: ')
    phone2 = '07' + phone
    if len(phone) - 1 > 8:
        print('Len have to be < 8')
        next_move = input('try again...')

    # email
    email = input('Introduce email: ')
    email2 = email + '@gmail.com'

    # adress
    adress = input('Introduce adress: ')
    output = storage_name + ' ' + phone2 + ' ' + email2 + ' ' + adress

    #writing in file
    contact_storage = open('...file path...', 'a+')
    contact_storage.write(output)
    contact_storage.write('\n')

    another_try = input('Do you want to write another contact? yes/no: ')
    if another_try == 'yes':
        input_ok = True
    else:
        print('Have a nice day!')
        exit()