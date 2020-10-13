#variant 12
num = int(input("enter a number:"))
mult = 1
sum = 0
while num > 0:
    digit = num % 10
    mult *= digit
    sum += digit
    num = num // 10
print("Множення:", mult)
print("Додавання в квадраті:", sum*sum)
if sum*sum != mult:
    print("false")
else:
    print("true")