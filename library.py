class Book:
    def __init__(self, name, author, department):
        self.name = name
        self.author = author
        self.department = department
        self.issued = False
        self.roll = ""
        self.days = 0


books = [
    # Mechanical Engineering
    Book("Engineering Mechanics", "R.S. Khurmi", "Mechanical"),
    Book("Theory of Machines", "R.S. Khurmi", "Mechanical"),
    Book("Strength of Materials", "R.K. Rajput", "Mechanical"),
    Book("Fluid Mechanics", "R.K. Rajput", "Mechanical"),
    # Civil Engineering
    Book("Surveying", "B.C. Punmia", "Civil"),
    Book("Building Materials", "S.K. Duggal", "Civil"),
    Book("Structural Analysis", "R.C. Hibbeler", "Civil"),
    Book("Strength of Materials", "R.K. Bansal", "Civil"),
    # Electrical Engineering
    Book("Electrical Technology", "B.L. Theraja", "Electrical"),
    Book("Electrical Machinery", "P.S. Bimbhra", "Electrical"),
    Book("Engineering Circuit Analysis", "Hayt", "Electrical"),
    Book("Power System Engineering", "Nagrath and Kothari", "Electrical"),
    # Computer Science Engineering
    Book("Python Crash Course", "Eric Matthes", "Computer Science"),
    Book("Clean Code", "Robert C. Martin", "Computer Science"),
    Book("Operating System Concepts", "Silberschatz", "Computer Science"),
    Book("Computer Networking", "Kurose and Ross", "Computer Science"),
    # Pre-added books, i searched all the books name and their author on google
    # Electronics Engineering
    Book("Microelectronic Circuits", "Sedra and Smith", "Electronics"),
    Book("Digital Design", "Morris Mano", "Electronics"),
    Book("Electronic Devices", "Thomas Floyd", "Electronics"),
    Book("Communication Systems", "Simon Haykin", "Electronics"),
    # Chemical Engineering
    Book("Chemical Engineering Thermodynamics", "Smith and Van Ness", "Chemical"),
    Book("Unit Operations", "McCabe, Smith and Harriott", "Chemical"),
    Book("Chemical Reaction Engineering", "Octave Levenspiel", "Chemical"),
    Book("Transport Phenomena", "Bird, Stewart and Lightfoot", "Chemical"),
    # Aerospace Engineering
    Book("Introduction to Flight", "John D. Anderson", "Aerospace"),
    Book("Fundamentals of Aerodynamics", "John D. Anderson", "Aerospace"),
    Book("Aircraft Structures", "T.H.G. Megson", "Aerospace"),
    Book("Flight Stability and Control", "Robert C. Nelson", "Aerospace"),
    # Automobile Engineering
    Book("Automotive Mechanics", "William H. Crouse", "Automobile"),
    Book("Automobile Engineering", "Kirpal Singh", "Automobile"),
    Book("Automotive Technology", "James D. Halderman", "Automobile"),
    Book("Internal Combustion Engines", "V. Ganesan", "Automobile"),
]


# this function adds a new book to the library
def add_book():
    name = input("Enter book name: ")
    author = input("Enter author name: ")
    department = input("Enter department: ")
    book = Book(name, author, department)
    books.append(book)
    print("\nBook added successfully!")
    print("Process done.")


# this function views all books in the library
def view_books():
    if len(books) == 0:
        print("No books in library.")
        return
    print("\n========== ALL BOOKS ==========")
    for book in books:
        print("\nBook:", book.name)
        print("Author:", book.author)
        print("Department:", book.department)
        if book.issued == True:
            print("Status: Issued")
            print("Roll Number:", book.roll)
            print("Days:", book.days)
        else:
            print("Status: Available")
        print("------------------------------")


# this function searches for a book
def search_book():
    name = input("Enter book name: ")
    for book in books:
        if book.name.lower() == name.lower():
            print("\nBook found!")
            print("Book:", book.name)
class Book:
    def __init__(self, name, author, department):
        self.name = name
        self.author = author
        self.department = department
        self.issued = False
        self.roll = ""
        self.days = 0


books = [
    # Mechanical Engineering
    Book("Engineering Mechanics", "R.S. Khurmi", "Mechanical"),
    Book("Theory of Machines", "R.S. Khurmi", "Mechanical"),
    Book("Strength of Materials", "R.K. Rajput", "Mechanical"),
    Book("Fluid Mechanics", "R.K. Rajput", "Mechanical"),
    # Civil Engineering
    Book("Surveying", "B.C. Punmia", "Civil"),
    Book("Building Materials", "S.K. Duggal", "Civil"),
    Book("Structural Analysis", "R.C. Hibbeler", "Civil"),
    Book("Strength of Materials", "R.K. Bansal", "Civil"),
    # Electrical Engineering
    Book("Electrical Technology", "B.L. Theraja", "Electrical"),
    Book("Electrical Machinery", "P.S. Bimbhra", "Electrical"),
    Book("Engineering Circuit Analysis", "Hayt", "Electrical"),
    Book("Power System Engineering", "Nagrath and Kothari", "Electrical"),
    # Computer Science Engineering
    Book("Python Crash Course", "Eric Matthes", "Computer Science"),
    Book("Clean Code", "Robert C. Martin", "Computer Science"),
    Book("Operating System Concepts", "Silberschatz", "Computer Science"),
    Book("Computer Networking", "Kurose and Ross", "Computer Science"),
    # Electronics Engineering
    Book("Microelectronic Circuits", "Sedra and Smith", "Electronics"),
    Book("Digital Design", "Morris Mano", "Electronics"),
    Book("Electronic Devices", "Thomas Floyd", "Electronics"),
    Book("Communication Systems", "Simon Haykin", "Electronics"),
    # Chemical Engineering
    Book(
        "Chemical Engineering Thermodynamics",
        "Smith and Van Ness",
        "Chemical",
    ),
    Book("Unit Operations", "McCabe, Smith and Harriott", "Chemical"),
    Book("Chemical Reaction Engineering", "Octave Levenspiel", "Chemical"),
    Book("Transport Phenomena", "Bird, Stewart and Lightfoot", "Chemical"),
    # Aerospace Engineering
    Book("Introduction to Flight", "John D. Anderson", "Aerospace"),
    Book("Fundamentals of Aerodynamics", "John D. Anderson", "Aerospace"),
    Book("Aircraft Structures", "T.H.G. Megson", "Aerospace"),
    Book("Flight Stability and Control", "Robert C. Nelson", "Aerospace"),
    # Automobile Engineering
    Book("Automotive Mechanics", "William H. Crouse", "Automobile"),
    Book("Automotive Engineering", "Kirpal Singh", "Automobile"),
    Book("Automotive Technology", "James D. Halderman", "Automobile"),
    Book("Internal Combustion Engines", "V. Ganesan", "Automobile"),
]


# this function adds a new book to the library
def add_book():
    name = input("Enter book name: ")
    author = input("Enter author name: ")
    department = input("Enter department: ")
    book = Book(name, author, department)
    books.append(book)
    print("\nBook added successfully!")
    print("Process done.")


# this function views all books in the library
def view_books():
    if len(books) == 0:
        print("No books in library.")
        return
    print("\n========== ALL BOOKS ==========")
    for book in books:
        print("\nBook:", book.name)
        print("Author:", book.author)
        print("Department:", book.department)
        if book.issued == True:
            print("Status: Issued")
            print("Roll Number:", book.roll)
            print("Days:", book.days)
        else:
            print("Status: Available")
        print("------------------------------")


# this function searches for a book
def search_book():
    name = input("Enter book name: ")
    for book in books:
        if book.name.lower() == name.lower():
            print("\nBook found!")
            print("Book:", book.name)
            print("Author:", book.author)
            print("Department:", book.department)
            if book.issued == True:
                print("Status: Issued")
                print("Roll Number:", book.roll)
                print("Days:", book.days)
            else:
                print("Status: Available")
            print("Process done.")
            return
    print("Book not found.")


# this function searches books by department
def search_department():
    department = input("Enter department: ")
    found = False
    print("\n========== BOOKS ==========")
    for book in books:
        if book.department.lower() == department.lower():
            print("\nBook:", book.name)
            print("Author:", book.author)
            print("Department:", book.department)
            if book.issued == True:
                print("Status: Issued")
            else:
                print("Status: Available")
            found = True
    if found == True:
        print("\nProcess done.")
    else:
        print("No books found for this department.")


# this function issues a book
def issue_book():
    name = input("Enter book name: ")
    for book in books:
        if book.name.lower() == name.lower():
            if book.issued == True:
                print("Book is already issued!")
                return
            book.roll = input("Enter student roll number: ")
            book.days = input("How many days do you want the book? ")
            book.issued = True
            print("\nBook issued successfully!")
            print("Book:", book.name)
            print("Student Roll Number:", book.roll)
            print("Number of Days:", book.days)
            print("Process done.")
            return
    print("Book not found.")


# this function returns a book
def return_book():
    name = input("Enter book name: ")
    for book in books:
        if book.name.lower() == name.lower():
            if book.issued == True:
                book.issued = False
                book.roll = ""
                book.days = 0
                print("\nBook returned successfully!")
                print("Process done.")
            else:
                print("This book is not issued.")
            return
    print("Book not found.")


# Main program
while True:
    print("\n========================================")
    print(" LIBRARY MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Search By Department")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        search_department()
    elif choice == "5":
        issue_book()
    elif choice == "6":
        return_book()
    elif choice == "7":
        print("\nThank you for using the Library Management System!")
        print("Program ended.")
        break
    else:
        print("Invalid choice! Please enter 1-7.")