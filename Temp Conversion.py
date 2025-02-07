#Temperature conversion program

temp = float(input("Write the temperature: "))
convert = input("To which measurement you want to convert (C or F): ")

def celsius(temp):
    return (temp - 32) * 5/2

def fahrenheit(temp):
    return (temp * 9/5) + 32

while True:
    if convert.capitalize() == "C":
        print(f"{(celsius(temp)):.2f}C")
        break
    elif convert.capitalize() == "F":
        print(f"{(fahrenheit(temp)):.2f}F")
        break
    else:
        print("Please enter a valid input.")
        break