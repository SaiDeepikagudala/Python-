class Library:
    def __init__(self, book_inventory):
        self.books = book_inventory  # Dictionary to keep track of book names and quantities
        self.borrow_return_log = []  # List to track borrowed and returned book details

    def display_available_books(self):
        print("\nAvailable Books:")
        for book, count in self.books.items():
            print(f"{book}: {count} copies")

    def borrow_book(self, name, bookname):
        if bookname not in self.books or self.books[bookname] == 0:
            print(f"\n{bookname} is not available at present.")
        else:
            self.borrow_return_log.append({"Name": name, "Book": bookname, "Status": "Borrowed"})
            self.books[bookname] -= 1  # Reduce the count by 1
            print("\nBook issued. Please return before the due date.")

    def return_book(self, name, bookname):
        if bookname in self.books:
            self.books[bookname] += 1  # Increase the count by 1
        else:
            self.books[bookname] = 1  # Add the book if it was not in the collection
        self.borrow_return_log.append({"Name": name, "Book": bookname, "Status": "Returned"})
        print("\nBook returned: Thank you!")

    def donate_book(self, bookname):
        if bookname in self.books:
            self.books[bookname] += 1
        else:
            self.books[bookname] = 1
        self.borrow_return_log.append({"Name": "Donor", "Book": bookname, "Status": "Donated"})
        print(f"\nThank you for donating {bookname}!")

    def display_borrow_return_log(self):
        print("\nBorrow/Return Log:")
        if not self.borrow_return_log:
            print("No books have been borrowed or returned yet.")
        else:
            for record in self.borrow_return_log:
                print(f"{record['Name']} {record['Status']} '{record['Book']}'")


# Initialize the library with some books
library = Library({
    "Science and Invention": 3,
    "Fiction": 5,
    "Economics": 2,
    "Deadpool": 1,
    "You Can Win": 4,
    "The Alchemist": 2
})

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Display Available Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Donate Book")
        print("5. Display Borrow/Return Log")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            library.display_available_books()

        elif choice == '2':
            name = input("Enter your name: ")
            bookname = input("Enter the book name to borrow: ")
            library.borrow_book(name, bookname)

        elif choice == '3':
            name = input("Enter your name: ")
            bookname = input("Enter the book name to return: ")
            library.return_book(name, bookname)

        elif choice == '4':
            bookname = input("Enter the book name to donate: ")
            library.donate_book(bookname)

        elif choice == '5':
            library.display_borrow_return_log()

        elif choice == '6':
            print("Exiting the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
