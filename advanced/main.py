
while True:

    print("""
    Choose how you would like to format your string:
    1. Format a Name
    2. Format a Title
    3. Format a List
    4. Process Numbers
    5. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == "5":
        break

    elif choice == "1":
        while True:
            name = input("Enter a name to format (First Name Last Name): ")
            Clean_String = name.strip()
            Name_parts = Clean_String.split()

            if len(Name_parts) == 2:
                Final_name = " ".join(Name_parts).title()
                print(Final_name)
                break
            else:
                print("Invalid name. Please try again.")

    elif choice == "2":
        while True:
            title = input("Enter a title to format: ")

            if title.strip() != "":
                if "," in title or "::" in title:
                    Cleaned_text = title.replace(",", " ").replace("::", " ").strip().title()
                    Title_Words = Cleaned_text.split("   ")
                    Final_Words = []

                    for word in Title_Words:
                        clean_word = word.replace(" ", "")
                        Final_Words.append(clean_word)

                    Joined_Text = " ".join(Final_Words).title()
                    print(Joined_Text)
                else:
                    print(title.strip().title())

                break
            else:
                print("Invalid title. Please try again.")

    elif choice == "3":
        while True:
            items = input("Enter a list of items (Item1, Item2, Item3): ")
            Cleaned_items = items.strip().upper()

            if Cleaned_items != "":
                Final_items = Cleaned_items.replace(",", " | ")
                print(Final_items)
                break
            else:
                print("Invalid input. Please enter some items.")

    elif choice == "4":
        while True:
            numbers = input("Enter numbers separated by commas: ")
            Cleaned_numbers = numbers.strip()
            Number_list = Cleaned_numbers.split(",")

            Valid = True
            Count = 0
            Total = 0

            for number in Number_list:
                if not number.strip().isdigit():
                    Valid = False
                Count += 1

            if Valid:
                for number in Number_list:
                    Total += int(number.strip())

                Average = Total / Count

                print(f"Total: {Total}")
                print(f"Average: {Average}")
                break

            else:
                print("Invalid input. Please enter valid numbers.")

    else:
        print("Invalid choice. Please try again.")
