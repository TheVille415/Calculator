#This is the calculator assignment
#question asking a number
number = input("Pick a number")

#question asking how many eggs a small child can hold
othernumber = input("pick another number ")

new_number = input("Would you like to add, subtract, or multiply them? ")

if new_number == "add":
    print(f"You picked add, your new number is {int(number) + int(othernumber)}.")

elif new_number == "subtract":
    print(f"You picked subtract, your new number is {int(number) - int(othernumber)}.")

elif new_number == "multiply":
    print(f"You picked multiply, your new number is {int(number) * int(othernumber)}.")