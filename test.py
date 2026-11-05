books = {}

def add_books():
    title = input("Enter the title of book: ")
    author = input("Enter the name of author of book: ")
    if title not in books:
        books[title] = author
        print(books)
    else:
        print("books is already in the library")


add_books()