"""
Function library file for the Database app

Done for self

"""

# Load books -function that loads the data in the inputted file to the database
# If the input file is empty, noting that it starts with empty database
# If input file can't be found, start with empty file
def load_books(filename):
    books = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split('__')
                if len(parts) == 4:
                    books.append({
                        'name': parts[0],
                        'writer': parts[1],
                        'isbn': parts[2],
                        'year': int(parts[3])
                    })
        if not books:
            print(f"The file {filename} is empty. Starting with an empty database.")
            input("Press any key to continue...")
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty database.")
        input("Press any key to continue...")
    except ValueError as ve:
        print(f"ValueError: {ve}. There might be an issue with the data format.")
        input("Press any key to continue...")
    except IOError as ioe:
        print(f"IOError: {ioe}. There might be an issue with file permissions.")
        input("Press any key to continue...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        input("Press any key to continue...")
    return books



# Function that saves the book data to the database file
def save_books(filename, books):
    with open(filename, 'w') as file:
        for book in sorted(books, key=lambda x: x['year']):
            file.write(f"{book['name']}__{book['writer']}__{book['isbn']}__{book['year']}\n")


# Function to add books to the database
# Called with #2 option in the main app
# First asks the new book inputs, and then prompts if inputs are correct and they should be saved to the database
def add_book(books):
    try:
        name = input("\nEnter the book's name: ")
        writer = input("Enter the writer's name: ")

        # Check that ISBN given is numbers
        while True:
            isbn = input("Enter the book's ISBN: ")
            if isbn.isdigit():
                break
            else:
                print("Invalid ISBN. Please enter only numbers.")
        
        # Check for duplicate ISBN, and if user wants to update book details or terminate transaction
        for book in books:
            if book['isbn'] == isbn:
                print("\nA book with this ISBN already exists in the database.")
                while True:
                    update_existing = input("Do you want to update the existing book's information? (yes/no): ").lower()
                    if update_existing == 'yes':
                        book['name'] = name
                        book['writer'] = writer
                        while True:
                            try:
                                year = int(input("Enter the publishing year: "))
                                if year > 0 and year <= 2025:
                                    book['year'] = year
                                    break
                                else:
                                    print("Invalid year. Please enter a positive integer not greater than 2025.")
                            except ValueError:
                                print("Invalid input. Please enter a valid year.")
                        print("\nBook information updated.")
                        return True
                    elif update_existing == 'no':
                        print("\nBook not added to the database. Can't allow for duplicate ISBN numbers")
                        return False
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
        
        # While loop to check that the year input is correct
        while True:
            try:
                year = int(input("Enter the publishing year: "))
                if year > 0 and year <= 2025:
                    break
                else:
                    print("Invalid year. Please enter a positive integer not greater than 2025.")
            except ValueError:
                print("Invalid input. Please enter a valid year.")
        
        # Save values to dictionary
        new_book = {
            'name': name,
            'writer': writer,
            'isbn': isbn,
            'year': year
        }
        
        print(f"\nNew book details:\nName: {name}\nWriter: {writer}\nISBN: {isbn}\nYear: {year}")
        
        # While loop to check that the input is correct
        while True:
            update = input("Do you want to update the database with this book? (yes/no): ").lower()
            if update == 'yes':
                books.append(new_book)
                print("\nBook added to the database.")
                return True
            elif update == 'no':
                print("\nBook not added to the database.")
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        input("Press any key to continue...")



# This function prints the books saved in the database file, to the UI
def print_books(books):
    print("\n" + "="*80)
    print("\nThese are the books currently saved in the database.")
    print("Books are sorted in ascending order by the publishing year:")
    print("="*80)
    for book in sorted(books, key=lambda x: x['year']):
        print(f"Name: {book['name']}, Writer: {book['writer']}, ISBN: {book['isbn']}, Year: {book['year']}")
        print("-"*80)
