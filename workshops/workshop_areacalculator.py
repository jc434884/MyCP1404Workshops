
print('Area Calculator')

width = float(input('Enter Width '))
height = float(input('Enter Height '))
def areacalc(width,height):
    area = width * height
    return area

print(width, height,'=', areacalc(width,height))
