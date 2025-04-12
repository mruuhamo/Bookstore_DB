# Bookstore Application

## Overview
This Python program acts as a bookstore application that manages a database of books. The program takes a file as a command line argument, which contains rows of book information separated by double underscores (`__`). It allows the user to add new books, update the database, and print the current database content.

## Features
- **Add New Book**: Allows the user to input book details and add them to the database.
- **Update Existing Book**: Checks for duplicate ISBNs and allows the user to update existing book information.
- **Print Database Content**: Prints all book information in a human-readable format.
- **Error Handling**: Handles various exceptions and ensures robust user input validation.

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/mruuhamo/Bookstore_DB.git
    ```


## Usage
1. **Running the program**:
    ```bash
    python Library_db.py <filename>
    ```
    Replace `<filename>` with the name of your input file.
    Program comes with two sample databases, Library_1.txt and Library_2.txt
    To use example databases, input f.ex
    ```bash
    python Library_db.py Library_1.txt
    ```

3. **Program Options**:
    - **Add a new book**: Enter book details and choose whether to update the database.
    - **Print current database content**: Display all books in the database file that was inputted.
    - **Exit**: Exit the application.

## Input File Format
The input file should contain rows of book information separated by double underscores (`__`). Each row should include:
- Book Name
- Writer Name
- ISBN
- Publishing Year
