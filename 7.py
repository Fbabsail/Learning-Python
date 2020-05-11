sex = input('Are you a male of a female? (for male type 1/for female type 0) ')
weight = input("How much do you weigh in kilograms? ")
length = input('How tall are you in centimeters? ')
age = input('How old are you? ')
print('.')
print('.')
print('.')

BMI = float(weight)/((float(length)**2)/10000)
print(f"Your BMI is:  {float(BMI)}")

if int(age) < 15:
    print(f'Your body fat percentage is: {float(1.51 * float(BMI))-float(0.70 *float(age))-float(3.6 *float(sex) + 1.4)}'
          f''
          f' based on calculations and may not be accurate and is just a test feature.')
else:

    print(f'Your body fat percentage is: {float(1.20 * float(BMI))+float(0.23 *float(age))-float(10.8 *float(sex) + 1.4)}'
          f''
          f' based on calculations and may not be accurate and is just a test feature.')