num1 = int(input('num1 ='))
num2 = int(input('num2 ='))
num3 = int(input('num3 ='))
num4 = int(input('num4 ='))
print("%3d%3d%3d%3d" % (num1, num2, num3, num4))
print('{:3}{:3}{:3}{:3}'.format(num1, num2, num3, num4))
print(f"{num1:3}{num2:3}{num3:3}{num4:3}")

floatNum1 = float(input('float num1 ='))
floatNum2 = float(input('float num2 ='))
print("%11f%11f" % (floatNum1, floatNum2))
print('{:11}{:11}'.format(floatNum1, floatNum2))
print(f"{floatNum1:11}{floatNum2:11}")

floatNum3 = float(input('float num3 ='))
floatNum4 = float(input('float num4 ='))
print("%5.2f%5.2f" % (floatNum3, floatNum4))
print('{:5.2f}{:5.2f}'.format(floatNum3, floatNum4))
print(f"{floatNum3:5.2f}{floatNum4:5.2f}")
