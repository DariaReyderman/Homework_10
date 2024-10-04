# a
# 'Try-except' gives an option to "catch" the error without the program crashing

# b
# This way we can prevent the program from crashing

# c
x = 88
y = 0
while True:
    try:
        print(f"{x} / {y} = {x / y}")
    except:
        print("You cannot divide by zero")
        break
print("Change the value of 'y'")

# d
while True:
    try:
        temperature: float = float(input("Enter the temperature in your city: "))
        if not -30 <= temperature <= 50:
            raise ValueError(f"Pay attention on the condition")
        break
    except ValueError:
        print(f"The temperature is invalid.")
print(f"The temperature {temperature} is ok.")

# e
list1: list[int] = [20, 10, 7, 13]
while True:
    try:
        number = int(input("Enter a number: "))
        if number == -999:
            break
        if list1[number]:
            list1.insert(number, number)
            print(list1.index(number), list1)
    except ValueError:
        print("This is not a valid number")
    except IndexError:
        print("This index is out of range")
print(list1)
