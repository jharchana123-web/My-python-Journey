school = {}
while True:
    print("\n" + "="*30)
    print(" SCHOOL MANAGEMENT SYSTEM ")
    print("="*30)
    print("1. Admission of new student")
    print("2. Search Student Result")
    print("3. View All Students & Stats")
    print("4. Exit")

    choice = input("\nWhat do you want to do (1-4): ")

    if choice == '1':
        print("\n--- Enter Student Details ---")

        name = input("Name: ")
        roll = input("Roll No.: ")
        try:
            marks = int(input("Enter marks (0-100): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        else:
            grade = "F"

        print(f"\n[Success] Student: {name} | Roll: {roll} | Grade: {grade}")
        
        school[roll] = {"Name": name, "Marks": marks, "Grade": grade}
        
        if grade == "F":
            print(f" Notice: Student {name} has failed and needs a re-test.")

    elif choice == '2':
        search_roll = input("\nEnter Roll No. to search: ")
        if search_roll in school:
            data = school[search_roll]
            print(f"\n--- Result for {search_roll} ---")
            print(f"Name:  {data['Name']}")
            print(f"Marks: {data['Marks']}")
            print(f"Grade: {data['Grade']}")
        else:
            print("Student record not found!")

    elif choice == '3':
        if not school:
            print("\nNo students registered yet.")
        else:
            print("\n--- Student Directory ---")
            total_marks = 0
            for r, info in school.items():
                print(f"Roll: {r} | Name: {info['Name']} | Grade: {info['Grade']}")
                total_marks += info['Marks']
            
            avg = total_marks / len(school)
            print("-" * 30)
            print(f"Total Students: {len(school)}")
            print(f"Class Average:  {avg:.2f}")

    elif choice == '4':
        print("Exiting... Have a great day!")
        break
    else:
        print("Invalid choice, please try again.")
        break