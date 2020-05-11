General_weight=input('Type in your weight: ')
unit=input('"Kgs" or "Lbs"? ')

if unit.upper() == 'KGS':
    print (f'Your weight in Lbs is {(float(General_weight)*2.2)}')


elif unit.upper()== "LBS":
    print(f'Your weight in Kgs is {float(General_weight)/2.2}')



