books = []
print("\n---Welcome To Library Management System ---")
while True:
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        serial = input("Enter book serial number: ")
        for book in books:
            if book[0] == serial:
                print("Serial number already exists.")
                break
        else:
            name = input("Enter book name: ")
            books.append([serial, name, "Available"])
            print("Book added.")
    elif choice == "2":
        print("\n--- Books ---")
        if len(books) == 0:
            print("No books available.")
        else:
            for book in books:
                print(book[0], "-", book[1], "-", book[2])
    elif choice == "3":
        serial = input("Enter book serial number: ")
        for book in books:
            if book[0] == serial:
                print("Book:", book[1])
                print("Status:", book[2])
                break
        else:
            print("Book not found.")
    elif choice == "4":
        serial = input("Enter book serial number: ")
        for book in books:
            if book[0] == serial:
                if book[2] == "Available":
                    book[2] = "Issued"
                    print("Book issued.")
                else:
                    print("Book is already issued.")
                break
        else:
            print("Book not found.")
    elif choice == "5":
        serial = input("Enter book serial number: ")
        for book in books:
            if book[0] == serial:
                if book[2] == "Issued":
                    days = int(input("Enter number of days kept: "))
                    if days < 1:
                        print("Invalid number of days.")
                    else:
                        if days > 7:
                            fine = (days - 7) * 10
                            print("Fine = ₹", fine)
                        else:
                            print("No fine.")
                        book[2] = "Available"
                        print("Book returned successfully.")
                else:
                    print("This book is not issued.")
                break
        else:
            print("Book not found.")
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")