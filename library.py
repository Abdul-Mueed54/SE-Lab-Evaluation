# library.py
# A simple command-line library tracker.
books = {} # title -> {"author": str, "available": bool}
def show_menu():
    print("\n=== Library Tracker ===")
    print("0. Exit")
    print("2. List Books")
    print("4. Return Books")
    

def add_books() -> None: 
    title = input("Enter the title of book: ")
    author = input("Enter the name of author of book: ")
    if title not in books:
        books[title] = author
        print(f"Added {title}")
    else:
        print(f"{title} is already in the library")

def return_books() -> None:
    title = input("Enter the title of the book to return: ")
    if title in books:
        books[title]["available"] = True
        print(f"Returned title: '{title}'")
    else:
        print(f"No book titled '{title}'")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "2":
            list_books()

        elif choice == "1":
            add_books()

        elif choice == "4":
            return_books()

        else:
            print("Invalid option")


def list_books():
    print(books)
    
if __name__ == "__main__":
    main()