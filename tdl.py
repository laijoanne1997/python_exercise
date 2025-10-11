#creating a to-do list that can be updated and completed in python
to_do_list=input("Would you like me to open your to-do list? (y/n) ").lowercase

if to_do_list == "y":
    file_name = input("What is your file name? ")
    file = open(file_name)
elif "n":
    quit()

for words in file:
    print (words)

    #adding more files to the list