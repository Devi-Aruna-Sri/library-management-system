import json
books = []
try:
    with open("books.json", "r") as file:
        books = json.load(file)
except FileNotFoundError:
    books = []
print("=================================")
print("    LIBRARY MANAGEMENT SYSTEM ")
print("=================================")
while True:
    print()
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")
    choice = input("Enter your choice:")
    if choice == "1":
        book_name = input("Enter book name: ")
        author = input("Enter author name: ")
        book_id = input("Enter book ID: ")
        if book_name == "":
            print("Book name cannot be empty!")

        elif author == "":
            print("Author name cannot be empty!")

        elif book_id == "":
            print("Book ID cannot be empty!")
        else:
            duplicate = False
            for book in books:
                if book["id"] == book_id:
                    duplicate = True
            if duplicate:
                print("Book ID already exists!")
            else:       
                book={
                "id": book_id,
                "name": book_name,
                "author": author,
                "status":"Available"
                }
            books.append(book)
            with open("books.json", "w") as file:
                json.dump(books, file, indent=4)
            print("Book added successfully!")
    elif choice == "2":
        if len(books) == 0:
            print("No books available.")
        else:
            print("/nLibrary Books:")
            for book in books:
                print("ID:", book["id"])
                print("Name:", book["name"])
                print("Author:", book["author"])
                print("Status:", book.get("status", "Available"))
                print("---------------------") 
    elif choice == "3":
        search_id = input("Enter book ID to search: ")
        found = False
        for book in books:
            if book["id"] == search_id:
                print("Book Found!")
                print("ID:", book["id"])
                print("Name:", book["name"])
                print("Author:", book["author"])
                print("Status:",book.get("status","Available"))
                found = True
                break
        if found == False:
            print("Book not found.")
    elif choice == "4":
        issue_id = input("Enter book ID to issue: ")
        found = False
        for book in books:
            if book["id"] == issue_id:
                found = True
                if book.get("status", "Available") == "Available":
                    book["status"] = "Issued"
                    with open("books.json", "w") as file:
                        json.dump(books, file, indent=4)
                    print("Book issued successfully!")
                else:
                    print("Book is already issued.")
                break    
        if found == False:
            print("Book not found.")
    elif choice == "5":
        return_id = input("Enter book ID to return: ")
        found = False
        for book in books:
            if book["id"] == return_id:
                found = True
                if book.get("status", "Available") == "Issued":
                    book["status"] = "Available"
                    with open("books.json", "w") as file:
                        json.dump(books, file, indent=4)
                    print("Book returned successfully!")
                else:
                    print("Book was not issued.")
                break    
        if found == False:
            print("Book not found.")                          
    elif choice == "6":
            print("Thank you for using the Library Management System!")
            break
    else:
        print("Invalid choice. Please enter 1 to 6.")        