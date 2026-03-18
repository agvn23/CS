#  Personal Library Manager
books = []

def print_divider():
    print("\n" + "=" * 45)

def go_back():
    choice = input("Press enter to return to the main menu.")
    if choice == "":
        return
 
def print_menu():
    print_divider()
    print("        Personal Library Manager")
    print_divider()
    print("  1. Add a Book")
    print("  2. View All Books")
    print("  3. Search Books by Title")
    print("  4. Show Statistics")
    print("  5. Exit")
    print_divider()
    choice = input("Enter your choice: ")
    return choice.strip()
 
# Add a Book – Store title, author, year, and genres.
def add_book(books):
    print_divider()
    print("\n--------Add a New Book---------")
    
    title = input("Please enter book name: ").strip().title()                 # Taking input for book title and formatting it
    while title == "":                                                        # loop untill title input
        title = input("You have to enter a title for the book: ").strip().title()
    
    author = input(f"Enter author of {title}: ").strip().title()              # Taking input for author of book and formatting it
    while author =="":                                                        # loop untill author input
        author = input(f"Enter author of {title}: ").strip().title()

            # Validating year input to prevent crashes
    year = input(f"Please enter the year {title} was written: ").strip()      # Taking input for year of book
    while not year.isdigit():                                                 # loop untill year input is a valid number
        year = input(f"Please enter a valid year for when {title} was written: ").strip()
    
    # while True:
    #     try:
    #         year = int(input(f"Please enter the year {title} was written: "))
    #         break
    #     except ValueError:
    #         print("Enter a valid number for the year.")
    
    # year = int(input(f"Enter the year that {author} wrote {title}"))    # Taking input for year of book #
    # while year =="":                                                    # loop untill year input
    #     print("Enter year")
    #     year = input(f"Enter the year that {author} wrote {title}")   

    genre = input(f"Please enter the genre of {title}: ").strip().title()      # Taking input of genre and formatting it
    while genre =="":                                                          # loop untill genre input
        genre = input(f"Enter the genre of {title}: ").strip().title()

    book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre
    }

    books.append(book.copy())              # Adding book to the list of books, .copy() to create a copy 
    print_divider()
    print(f"Book {title} added successfully.")
    return

# View All Books – Display every book in the library.
def view_books(books):
    print_divider()
    print("\n--------All Books---------")
    if not books:                          # Checking if there are any books in the list of books,
        choice = input("No books added yet. Do you wish to add a book now? yes/no: ").strip()
        if choice.lower() == "yes":
            add_book(books)
            print("\nBook Information: ")
            for book in books:
                print(f"\nTitle: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}")
            print_divider()
            go_back()
        else:
            go_back()  
    else:
        print("\nBook Information: ")
        for book in books:
            print(f"\nTitle: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}")
        print_divider()
        go_back()

# Search Books by Title – Case-insensitive match.
def search_books(books):
    print_divider()
    print("\n--------Search for a Book---------")
    search_title = input("Enter book to search: ").strip().title()      # Taking input for book
    print(f"\nSearching results for {search_title}: ")
    
    for book in books:
        if book["title"] == search_title:
            print(f"\nBook: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}")
            print_divider()
            go_back()
    else:
        print("Book not found.")      ###########problem
        go_back()                                                       # If the book is found
    print_divider()           


# Show Statistics – Number of books, unique authors, genres count.
def show_statistics(books):
    print_divider()
    print("\n--------Statistics---------")

    if not books:                        # If there are no 
        print("No books found.")
        print_divider()
        return
    
    # Total books
    total_books = len(books)             # Getting the number of books by using the len()
    print(f"Total Books: {total_books}")   
    print_divider() 

    # 2. Author Statistics
    author_counts = {}
    for book in books:
        for author in book["authors"]:
            # Increment count for each author found
            author_counts[author] = author_counts.get(author, 0) + 1

    print("\nBooks by author:")
    if author_counts:
        # Sorting by author name (the key)
        for author in sorted(author_counts):
            print(f"- {author}: {author_counts[author]}")
    else:
        print("No authors recorded.")
    print_divider()

    # 3. Genre Statistics
    genre_counts = {}
    for book in books:
        for genre in book["genres"]:
            # Increment count for each genre found
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    print("\nBooks in genre:")
    if genre_counts:
        # Sorting by genre name
        for genre in sorted(genre_counts):
            print(f"- {genre}: {genre_counts[genre]}")
    else:
        print("No genres recorded.")
    print_divider()
    

def main():
    while True:
        #print_divider()
        #print_menu()
        choice = print_menu() # Catch the returned choice here
        #print_divider()
        if choice == '1':
            add_book(books)
        elif choice == '2':
            view_books(books)
        elif choice == '3':
            search_books(books)
        elif choice == '4':
            show_statistics(books)
        elif choice == '5':
            choice = input("Are you sure you want to exit? yes/no: ")
            if choice.lower() == "yes":
                break
            else:
                print("\n" + "-" * 20)
                continue
        else:
            print("Invalid choice. Please try again.")
            print("\n" + "-" * 20)

if __name__ == "__main__":
    main()