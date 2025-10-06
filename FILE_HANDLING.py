import os

while True:
    print("\nSTUDENT RECORD SYSTEM")
    print("1. Register Student")
    print("2. Open Student Record")
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n--- Register Student ---")
        student_no = input("Student No.: ")
        last_name = input("Last Name: ")
        first_name = input("First Name: ")
        middle_initial = input("Middle Initial: ")
        program = input("Program: ")
        age = input("Age: ")
        gender = input("Gender: ")
        birthday = input("Birthday: ")
        contact_no = input("Contact No.: ")

        data = [
            f"Student No.: {student_no}",
            f"Full Name: {last_name}, {first_name} {middle_initial}.",
            f"Program: {program}",
            f"Age: {age}",
            f"Gender: {gender}",
            f"Birthday: {birthday}",
            f"Contact No.: {contact_no}"
        ]

        doc_path = os.path.expanduser("~/Documents")
        os.makedirs(doc_path, exist_ok = True)  
        file_path = os.path.join(doc_path, f"{student_no}.txt")

        with open(file_path, "w") as f:
            for line in data:
                f.write(line + "\n")

        print(f"Student record for {first_name} {last_name} saved successfully!")

    elif choice == "2":
        print("\nOpen Student Record")
        student_no = input("Enter student number: ")

        doc_path = os.path.expanduser("~/Documents")
        file_path = os.path.join(doc_path, f"{student_no}.txt")

        try:
            with open(file_path, "r") as f:
                print("\n STUDENT RECORD:")
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print(" Student record not found.")

    elif choice == "3":
        print("\n Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
