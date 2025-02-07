#Weight conversion program

weight = float(input("Write the weight: "))
convert = input("To which measurement you want to convert (Kg or Lb): ")
def kilo(weight):
    return weight * 0.45

def libs(weight):
    return weight * 2.2

while True:
    if convert.capitalize() == "Kg":
        print(f"{(kilo(weight)):.2f}Kg")
        break
    elif convert.capitalize() == "Lb":
        print(f"{(libs(weight)):.2f}Lbs")
        break
    else:
        print("Please enter a valid input.")
        break