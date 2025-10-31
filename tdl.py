def strike(text):
    return ''.join([c + '\u0336' for c in text])

to_do_list = input("Would you like to open your to-do list? (y/n): ").lower()

if to_do_list == "y":
    file_name = input("What is your file name? ")
    try:
        with open(file_name, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        print(f"\nYour file '{file_name}' has successfully opened.")
    except FileNotFoundError:
        print("File not found. Starting a new to-do list instead.")
        tasks = []
elif to_do_list == "n":
    file_name = input("Enter a name for your new to-do list file (e.g. todo.txt): ")
    tasks = []
else:
    print("Invalid choice.")
    quit()

print("\nHere are the items on your to-do list:")
if tasks:
    for i, item in enumerate(tasks, 1):
        print(f"{i}. {item}")
else:
    print("Your to-do list is empty!")

update = input("\nDo you want to update your to-do list? (y/n): ").lower()

if update == "y":
    action = input("Would you like to add more (add) or complete (tick)? ").lower().strip()

    if action == "add":
        while True:
            add = input("What would you like to add? (type 'done' when finished): ").strip()
            if add == "done":
                break
            tasks.append(add)

    elif action == "tick":
        for i, item in enumerate(tasks):
            completed = input(f"Is this task completed? '{item}' (y/n): ").lower()
            if completed == "y":
                tasks[i] = strike(item)

    with open(file_name, "w") as file:
        for task in tasks:
            file.write(task + "\n")

print("\n✅ Done! Your to-do list has been updated.")
