# The first exercise
first_name = input('Your first name: ')
middle_name = input('Your middle name: ')
last_name = input('Your last name: ')
print('So you are,' + first_name + middle_name + last_name)

# String slicing
postal_code = '033-11091-00018'
print('\n' + 'postal code = ' + postal_code)
print('Country code: ', postal_code[:3])
print('Product code: ', postal_code[4:9])
print('Batch number: ', postal_code[10:])