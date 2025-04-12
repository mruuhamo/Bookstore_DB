"""
Database app with Library input

Done for self

App takes in file as an argument when launcing, and handles if input file is not given or correct

"""

# Import necessary libraries and functions
import sys
import os
from Func.Functions import load_books
from Func.Functions import save_books
from Func.Functions import add_book
from Func.Functions import print_books


def main():
    if len(sys.argv) != 2:
        print("Usage: python bookstore.py <filename>")
        return
    
    filename = sys.argv[1]
    
    books = load_books(filename)

    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print("\n" + "="*50)
        print("Welcome to the Bookstore™ Application".center(50))
        print("="*50)
        print("\n You have the following options:")
        print("1. Add a new book")
        print("2. Print current database content")
        print("3. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            # Calls the save-books function only if new book is to be added
            if add_book(books):
                save_books(filename, books)
        elif choice == '2':
            print_books(books)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

