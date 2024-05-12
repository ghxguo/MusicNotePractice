# Music Note Practice

This Python program is designed to help users practice their music note recognition skills. It generates a group of random notes and asks the user to identify them. The user can specify the number of practice runs, the size of the note group, and the type of note names to use.

## Features

- Generates a group of random notes without duplicates
- Checks the user's answers and provides feedback
- Calculates and displays the percentage of correct answers at the end of all runs

## Usage

1. Run the program. Example: 
```
python music_note_practice.py
```
2. Enter the number of practice runs.
3. Enter the size of the note group (between 1 and 7).
4. Enter the type of note names to use ('name' for 'do', 're', 'mi', etc., or 'CDE' for 'C', 'D', 'E', etc.).
5. For each run, the program will display a group of random notes. Enter your answers in one line, separated by spaces or commas.
6. The program will check your answers and provide feedback. If all answers are correct, it will print a message saying so. If any answer is incorrect, it will print the incorrect ones and the correct answers.
7. At the end of all runs, the program will calculate and print the percentage of correct answers.

## Note Mapping

The program uses the following mapping between numbers and note names:

1: ['do', 'C']
2: ['re', 'D']
3: ['mi', 'E']
4: ['fa', 'F']
5: ['sol', 'so', 'G']
6: ['la', 'A']
7: ['si', 'ti', 'B']
