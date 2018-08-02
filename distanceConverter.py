print("Enter distance.")
distance = int(input())
print("Enter 'mi' or 'km' unit.")
unit1 = input()
print("Enter desired 'mi' or 'km' unit.")
unit2 = input()


if unit1 == "mi":
    distance / 1.60934
    
elif unit1 == "km":
    distance1/ 0.621371

print(distance, unit1, "is converted to", distance, unit2)


#mi = 1
#km = 1.60934
#ft = 5280
#m = 1609.34