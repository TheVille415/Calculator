#This is the calculator assignment
#question asking how many eggs they can hold
egg_number = input("How many eggs can you hold? ")

#question asking how many eggs a small child can hold
kidegg_number = input("How many eggs can a child hold? ")

#asking which operation they would like to do and printing out a new number
new_number = input("Would you like to Give them your eggs, Take their eggs, Break their eggs , or Split your eggs with them? ")
#You are taking the kids eggs so you add them to your own
if new_number == "take":
    print(f"You picked take, your now have {int(egg_number) + int(kidegg_number)} eggs.")
#You give the child your eggs so you add the eggs to their total
elif new_number == "give":
    print(f"You picked give, they now have {int(egg_number) + int(kidegg_number)} eggs.")
#This process will add the numbers then divide by 2 so you can get the mean for how many eggs each person will have
elif new_number == "split":
    newst_number = (int(egg_number) + int(kidegg_number))/2
    print(f"You picked split, you each have at least {round(newst_number)} eggs.")
elif new_number == "break":
    print(f"You picked break, you used your eggs to break their eggs. You have {int(egg_number) - int(kidegg_number)} eggs left.")
else:
    print("Please enter one of the options!")
#the code ends on the else statement but I would like it to loop back up to ask the questions again instead of closing off
