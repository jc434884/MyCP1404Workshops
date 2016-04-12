print('Temperature Conversion Program')
celsiusVlaue = float(input('Enter temperature in Celsius: '))
def convert(celsiusvalue):
        fahrenheatValue = celsiusVlaue * 9 / 5 + 32
        return fahrenheatValue
print('Celsius Value: ', celsiusVlaue)
print('Fahrenheit Value: ',convert(celsiusVlaue))
