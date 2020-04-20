#1 miles = 1.609344km
def kmMiles(x):
    return print(x,'km', '=', x/1.609344)

def milesKm(x):
    return print(x, 'miles', '=', x*1.609344)

print('-- Kilometer to Miles Converter --')
n = int(input('Enter 1 for Km to Miles / Enter 2 for Miles to Km: '))

if n == 1:
    k = int(input('Enter the km values: '))
    kmMiles(k)

elif n == 2:
    m = int(input('Enter the miles values: '))
    milesKm(m)