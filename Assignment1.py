#Copy Pasted sample data from file and added it into dictionaries
# did not need copilot for this, as it was given data and a simple dictonary and list format
# I created two: one for the sample data on books, and for the reviews
sample = {
    "books": [
        {
            "bookId": "1",
            "title": "The Quantum Garden",
            "aiMetric": 88,
            "releaseYear": 2023,
            "author": "Alice Johnson",
            "genres": ["Science Fiction", "Thriller"],
            "publisherName": "Bright Future Press",
            "publisherLocation": "USA",
            "pages": 420,
            "sales": [50000, 60000, 72000]
        },
        {
            "bookId": "2",
            "title": "The Forgotten Code",
            "aiMetric": 42,
            "releaseYear": 2024,
            "author": "Devon Chen",
            "genres": ["Mystery", "Techno-thriller"],
            "publisherName": "Redwood House",
            "publisherLocation": "UK",
            "pages": 310,
            "sales": [20000, 25000, 30000]
        },
        {
            "bookId": "3",
            "title": "Dreaming in Algorithms",
            "aiMetric": 65,
            "releaseYear": 2023,
            "author": "Sofia Martinez",
            "genres": ["Non-fiction", "Technology"],
            "publisherName": "AI4Books",
            "publisherLocation": "Canada",
            "pages": 280,
            "sales": [15000, 18000, 19000]
        }
    ],
    "reviews": [
        {
            "reviewId": "1",
            "reviewAuthor": "Jane Developer",
            "reviewDate": "2024-05-12",
            "reviewText": "Fascinating mix of science and thriller, but the AI-generated dialogue felt awkward.",
            "bookId": "1"
        },
        {
            "reviewId": "2",
            "reviewAuthor": "Mark Tester",
            "reviewDate": "2024-06-07",
            "reviewText": "The Forgotten Code was suspenseful but leaned too much on technical jargon.",
            "bookId": "2"
        },
        {
            "reviewId": "3",
            "reviewAuthor": "Emily Engineer",
            "reviewDate": "2024-07-01",
            "reviewText": "Dreaming in Algorithms gave me new insights into how AI impacts creativity.",
            "bookId": "3"
        }
    ]
}
#I used copilot to write the load and save functions for books, using its scaffolding to do the same for reviews
#it creates a function to save data in which it has a loop looking for each category in the book dictionary
# it orignally caused many issues it did not account for lists in genress, so I used copilot to install a split 
# I chose to use a CSV as it is a common known file format in which It is easy to export
# After multiple prompt fixes, Copilot was able to handle the function generation for file handling correctly, as each time would provide a different answer and cause errors
#This helped me a lot in prompt engineering, as it helped me understand how to talk to the LLM to get the best output
#

import csv
import os

def load_data(books_file='books.csv', reviews_file='reviews.csv'):
    books = []
    reviews = []
    if os.path.exists(books_file):
        with open(books_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                genres_val = row.get('genres', '')
                if genres_val:
                    row['genres'] = genres_val.split('|')
                else:
                    row['genres'] = []
                sales_val = row.get('sales', '')
                if sales_val:
                    row['sales'] = list(map(int, sales_val.split('|')))
                else:
                    row['sales'] = []
                row['aiMetric'] = int(row.get('aiMetric', 0) or 0)
                row['releaseYear'] = int(row.get('releaseYear', 0) or 0)
                row['pages'] = int(row.get('pages', 0) or 0)
                books.append(row)
    if os.path.exists(reviews_file):
        with open(reviews_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                reviews.append(row)
    return books, reviews

def save_data(book, review=None, books_file='books.csv', reviews_file='reviews.csv'):
    if book:
        books_fieldnames = ['bookId', 'title', 'aiMetric', 'releaseYear', 'author', 'genres', 'publisherName', 'publisherLocation', 'pages', 'sales']
        with open(books_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=books_fieldnames)
            # This loop uses copilot's scaffoling, in which it checks if the book is in a list, and if it is it appends it to the dictionary
            book_list = book if isinstance(book, list) else [book]
            for b in book_list:
                if not isinstance(b, dict):
                    continue
                if not all(k in b for k in ['genres', 'sales']):
                    continue
                row = b.copy()
                row['genres'] = '|'.join(b['genres']) if isinstance(b['genres'], list) else b['genres']
                row['sales'] = '|'.join(map(str, b['sales'])) if isinstance(b['sales'], list) else b['sales']
                writer.writerow(row)
    if review:# this section is used to write the reviews into the CSV, in which I used copilot's scaffoldling to help understand each instance in the loop that would be written into the CSV
        # it uses this loop to check if the review is in a list, it will then append into the dictionary
        reviews_fieldnames = ['reviewId', 'reviewAuthor', 'reviewDate', 'reviewText', 'bookId']
        with open(reviews_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=reviews_fieldnames)
            review_list = review if isinstance(review, list) else [review]
            for r in review_list:
                if not isinstance(r, dict):
                    continue
                writer.writerow(r)

#this is used to load books and reviews into the data
books, reviews = load_data()

# This function is designed to get the user to input a new book
# I used copilot to help with the formatting structure, as I kept getting issues with the formatting
# I took copilots advice as it made sure the formats were correct, I kept playing around with the prompt to make sure it was correct
# It saved a lot of time in making sure the inputs had the correct formatting, but I did not like the titles it gave, as it seemed too long for a menu
# I got rid of the copilot titles as they had the type of field in them, as that shows too much information for the user.
def prompt_new_book():
    print('Enter new book details:')
    book = {}
    book['bookId'] = input('Book ID: ')
    book['title'] = input('Title: ')
    book['aiMetric'] = int(input('AI Metric: '))
    book['releaseYear'] = int(input('Release Year: '))
    book['author'] = input('Author: ')
    genres = input('Genres: ')
    book['genres'] = [g.strip() for g in genres.split(',') if g.strip()]
    book['publisherName'] = input('Publisher Name: ')
    book['publisherLocation'] = input('Publisher Location: ')
    book['pages'] = int(input('Pages: '))
    sales = input('Sales: ')
    book['sales'] = [int(s.strip()) for s in sales.split(',') if s.strip()]
    return book

#I used the same structure, I copied the same structure as the previous function. It was easy to replicate.
# I did not take copilots advice, as It kept trying to add more complexity to the function
# Copilot wanted to add multiple different formatting technicalities, such as strip and split for certain inputs, but it was not needed
def prompt_new_review():
    print('Enter new review details:')
    review = {}
    review['reviewId'] = input('Review ID: ')
    review['reviewAuthor'] = input('Review Author: ')
    review['reviewDate'] = input('Review Date (YYYY-MM-DD): ')
    review['reviewText'] = input('Review Text: ')
    review['bookId'] = input('Book ID (for this review): ')
    return review

# This is the menu system. I used copilot for the conditions in the if statements, but did not really like how it was structured at first
## To fix this, I wrote the print statements myself, and made the if-elif-else structure more simple for the first 3, while using copilot assistance for the inputs
## When the Menu is operating, it will print these 8 options, and the user can choose one
def main_menu():
    while True:
        print("\nMenu:")
        print("1. Load Data")
        print("2. Save Data")
        print("3. Add Book")
        print("4. Add Review")
        print("5. Print titles of all books released in a user specified year")
        print("6. Print titles of all books with an AI metric lower than a user specified value")
        print("7. Print all books that have at least 1 review")
        print("0. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            global books, reviews
            books, reviews = load_data()
            print("Data loaded from CSV.")
        elif choice == "2":
            print("Data is always appended automatically when you add a book or review.")
        elif choice == "3":
            
            book = prompt_new_book()
            books.append(book)
            save_data(book, None)
            print("Book added and saved.")
        elif choice == "4":
            review = prompt_new_review()
            reviews.append(review)
            save_data(None, review)
            print("Review added and saved.")
        elif choice == "5":
            year = int(input("Enter release year: "))
            titles = [b['title'] for b in books if b['releaseYear'] == year]
            print("Books released in", year, ":", titles)
        elif choice == "6":
            value = int(input("Enter AI metric value: "))
            titles = [b['title'] for b in books if b['aiMetric'] < value]
            print("Books with AI metric lower than", value, ":", titles)
        elif choice == "7":
            reviewed_book_ids = set(r['bookId'] for r in reviews)
            titles = [b['title'] for b in books if b['bookId'] in reviewed_book_ids]
            print("Books with at least one review:", titles)
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

# This function wasn't written by copilot, as I used previous structures written above to build an idea for this function
# I attempted copilot for writing the data into the csv, but it consistently caused formatting issues, and caused too many crashes
# It pulls the sample data from the dictionary, and uses the save_data function to write the sample data provided into the csv
def write_sample_to_csv():
    books = sample['books']
    reviews = sample['reviews']
    save_data(books, reviews)
    print("Sample data written to books.csv and reviews.csv.")

if __name__ == "__main__":
    # Copilot originally had it where it would keep the files
    # I went against this advice and wanted it to remove each time as it can reload the data and not cause issues
    # I needed copilot assistance in the os based functions, as I didn't have the expeirience with it
    # This loop is used to check if the files are currently stored, and if they are it removes them to not cause issues and system crashes
    for filename in ['books.csv', 'reviews.csv']:
        if os.path.exists(filename):
            os.remove(filename)
    print("Deleted old CSV files. Reloading sample data...")
    books = sample['books']
    reviews = sample['reviews']
    save_data(books, reviews)
    main_menu()

