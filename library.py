# library.py
# A simple command-line library tracker.
books = {} # title -> {"author": str, "available": bool}
def show_menu():
    print("\n=== Library Tracker ===")
    
def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "2":
            list_books()


def list_books():
    print(books)
    
if __name__ == "__main__":
    main()