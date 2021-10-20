#Has a function to calculate the square footage of a house
#Reminder of Formula: Length X Width == Area

def find_area():
    length = input("What is the length? ")
    width = input("What is the width? ")
    area = int(length) * int(width)
    return area

print(find_area())