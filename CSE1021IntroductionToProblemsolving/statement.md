# Project Statement
## Project Title
Library Management System

## Problem Statement
Managing books manually in a library can make it difficult to keep track of which books are available and which books have been issued.

The aim of this project is to create a simple Library Management System using Python that can help manage basic book records.

The system uses a serial number for each book so that users can easily search, issue, and return books without entering the complete book name.

## Objectives
The main objectives of this project are:

1. To add books to the library.
2. To assign a serial number to each book.
3. To display the books and their current status.
4. To search for books using their serial number.
5. To issue available books.
6. To prevent an already issued book from being issued again.
7. To allow only issued books to be returned.
8. To calculate a fine for late book returns.

## Fine System
A book can be kept for 7 days without a fine.

If the book is kept for more than 7 days, a fine of ₹10 is charged for every extra day.

### Formula
Fine = (Number of days - 7) × ₹10