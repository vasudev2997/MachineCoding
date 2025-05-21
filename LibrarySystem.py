from typing import Dict, Optional

# Initializing a book structure
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

# Initializing the library
class Library():
    def __init__(self):
        self.books: Dict[int, Book] = {}

    def add_book(self, id: int, title: str, author: str) -> bool:
        if id not in self.books:
            self.books[id] = Book(title, author)
            return 1
        return 0

    def remove_book(self, id:int) -> bool:
        return self.books.pop(id, None) is not None # removes self.books[id] if exists otherwise removes None

    def search_by_title(self, title:str) -> Optional[tuple[int, Book]]:
        for id in self.books:
            if self.books[id].title.lower() == title.lower():
                return f"{id} - {self.books[id].title} by {self.books[id].author}"
        return 0

    def search_by_author(self, author) -> Optional[tuple[int, Book]]:
        for id in self.books:
            if self.books[id].author.lower() == author.lower():
                return f"{id} - {self.books[id].title} by {self.books[id].author}"
        return 0

    def display_all_books(self) -> None:
        for id in self.books:
            print(f"{id} - {self.books[id].title} by {self.books[id].author}")

def main():
    library = Library()
    print("=== WELCOME TO THE LIBRARY SYSTEM ===")

    while True:
        print("\nMENU")
        print("1. Add Book\n" \
        "2. Remove Book\n" \
        "3. Search by Title\n" \
        "4. Search by Author\n" \
        "5. Display All Books\n" \
        "6. Exit")

        choice = input("Enter your choice - ").strip().lower()

        if choice in ("1", "add", "add book"):
            try:
                id = int(input("Id - "))
                title = input("Title - ")
                author = input("Author - ")
                if not library.add_book(id, title, author):
                    print("Id already exists, retry\n")
                else:
                    print("Book added successfully.\n")
            except ValueError:
                print("Invalid ID, Please enter a number.\n")

        elif choice in ("2", "remove book", "remove"):
            try:
                id = int(input("Id - "))
                if not library.remove_book(id):
                    print("Book id not found, retry\n")
                else:
                    print("Book removes successfully\n")
            except ValueError:
                print("Invalid ID, please enter a number.\n")
        
        elif choice in ("3", "search by title", "title"):
            title = input("Title - ")
            result = library.search_by_title(title)
            if not result:
                print("No book found with that title, retry\n")
            else:
                print(result)

        elif choice in ("4", "search by author", "author"):
            author = input("Author - ")
            result = library.search_by_author(author)
            if not result:
                print("No book found with that author, retry\n")
            else:
                print(result)

        elif choice in ("display", "display all books", "display all", "5"):
            library.display_all_books()
        
        elif choice in ("6", "exit", "bye"):
            break

        else:
            print("Invalid Choice, retry\n")

if __name__ == "__main__":
    main()
