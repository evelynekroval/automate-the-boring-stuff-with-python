print('Enter C or F to indicate Celsius or Fahrenheit:')
scale = input().upper()
print('Enter the number of degrees:')
degrees = float(input())
if scale == 'C':
    if degrees >= 16 and degrees <= 38:
        print('Safe')
    else:
        print('Dangerous')
elif scale == 'F':
    if degrees > 60.8 and degrees <= 100.4:
        print('Safe')
    else:
        print('Dangerous')