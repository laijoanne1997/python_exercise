#creating a to-do list that can be updated and completed in python
to_do_list=input("Would you like me to open your to-do list? (y/n) ").lowercase

if to_do_list == "y":
    file_name = input("What is your file name? ")
    file = open(file_name)
    print(f"Your file, {file_name}, has successfully opened.")
elif "n":
    quit()

    print("Here are the list of item's on your to-do list: ")
for item in file:
    print(item)



