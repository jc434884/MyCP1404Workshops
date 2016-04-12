print('Area Calculator')

width = float(input('Enter Width '))
height = float(input('Enter Height '))

area = width * height

print(width, height, area)

print("*****************************************************")

print('Body Mass Index Calculator')

weight = float(input('Please enter your weight in Kgs: '))
height = float(input('Please enter your height in m: '))

bmi =  weight / height ** 2

print('Your BMI is: ', bmi)

print("*****************************************************")

print('Temperature Conversion Program')

celsiusVlaue = float(input('Enter temperature in Celsius: '))
fahrenheitValue = celsiusVlaue * 9 / 5 + 32

print('Celsius Value: ', celsiusVlaue)
print('Fahrenheit Value: ', fahrenheitValue)