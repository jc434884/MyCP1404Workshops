

print('Body Mass Index Calculator')

weight = float(input('Please enter your weight in Kgs: '))
height = float(input('Please enter your height in m: '))
def cal_bmi(weight,height):
   bmi =  weight / height ** 2
   return bmi
print('Your BMI is: ',cal_bmi(weight,height))