hour = int(input("input hours (up to 11)"))
minute = int(input("input minutes (up to 59)"))
seconds = int(input("input seconds (up to 59)"))
angle = 30 * hour + 0.5 * minute + 30.0/3600 * seconds
print("angle is", angle)
