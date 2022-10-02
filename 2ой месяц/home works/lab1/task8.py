relationship = {
    'max_to_min': '',
    'min_to_max': '',
    'difference': ''
}
num1 = int(input("Enter the first num: "))
num2 = int(input("Enter the second num: "))

if num1 > num2:
    max = num1
    min = num2
elif num1 < num2:
    max = num2
    min = num1
else:
    pass

relationship['max_to_min'] = max / min
relationship['min_to_max'] = min / max
relationship['difference'] = abs(num1) - abs(num2)

print("Max to min: %s" % relationship['max_to_min'])
print('Min to max: %s' % relationship['min_to_max'])
print('Difference: %s' % relationship['difference'])