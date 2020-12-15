from random import sample
import string

alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase
numbers = '0123456789'
symbols = '/.,\;][=-#$%^&*()!@'

alpha_low, alpha_up, digits, symb = True, True, True, True

the_content = ''

if alpha_low:
    the_content += alphabet_lower
if alpha_up:
    the_content += alphabet_upper
if digits:
    the_content += numbers
if symb:
    the_content += symbols

numbers_of_letters = 12
number_of_passowords = 15
print('You generate {} passwords!'.format(number_of_passowords))
for i in range(number_of_passowords):
    password = ''.join(sample(the_content, numbers_of_letters))
    print(password)
