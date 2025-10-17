#creating a to-do list that can be updated and completed in python
#need to consider fi they are making a new to-do list or updating an old one.
def strike(text):
    return ''.join([c + '\u0336' for c in text])

to_do_list=input("Would you like me to open your to-do list? (y/n) ").lower()

if to_do_list == "y":
    file_name = input("What is your file name? ")
    file = open(file_name, "r")
    print(f"Your file, {file_name}, has successfully opened.")
elif "n":
    quit()

print("\nHere are the list of item's on your to-do list:")

for item in file:
    print(item)

update=input("Do you want to update your to-do list? (y/n)").lower()

if update =="y":
    add_more=input("Did you want to add more (add) or complete (tick): ").lower().rstrip()
    while add_more == "add":
        add = input("What else would you like to add. If you're finished, write 'done'.").lower()
        if add == "done":
            break
        else:
            with open(file_name, "a") as afile:
                afile.write(add)
                continue
    elif add_more == "tick":
        for item in file:
            print(item)
            completed="Is this task completed? (y/n)".lowercase()
            if completed == "y":
                afile.write(strike(item))
            if complete == "n":
                continue

print("done")

