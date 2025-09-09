# Uploaded file
# Showed a full solution, did not use it
can you write the save and load functions for the menu
it then asked if i wanted to use json or csv: i responded CSV
it then asked if i wanted it to overwrite or append new data, i responded with append
Can you now create 2 functions that prompts users to create a new book and a new review
add code to load the sample data into the csv
I asked why the the same entry was consistently updated
Inserted this error message into copilot when I was receiving the message for the error in loading data
Traceback (most recent call last):
  File "c:\Users\georg\AIDD-HW1\Assignment1.py", line 212, in <module>
    main_menu()
    ~~~~~~~~~^^
  File "c:\Users\georg\AIDD-HW1\Assignment1.py", line 165, in main_menu
    books, reviews = load_data()
                     ~~~~~~~~~^^
  File "c:\Users\georg\AIDD-HW1\Assignment1.py", line 79, in load_data
    row['genres'] = row['genres'].split('|')
                    ~~~^^^^^^^^^^ 
It suggested to delete the files manually, so I asked it to write a loop that deletes and reloads it each time it runs
