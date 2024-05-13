import random
import re
import time

# Define the mapping between numbers and note names
note_mapping = {
    1: ['do', 'C'],
    2: ['re', 'D'],
    3: ['mi', 'E'],
    4: ['fa', 'F'],
    5: ['sol', 'so', 'G'],
    6: ['la', 'A'],
    7: ['si', 'ti', 'B']
}

def generate_notes(group_size):
    # Generate a group of random notes without duplicates
    return random.sample(range(1, 8), group_size)

def get_note_type():
    note_type = input('Enter the note type (name/CDE): ')
    while note_type not in ['name', 'CDE']:
        note_type = input("Invalid note type. Please enter 'name' or 'CDE': ")
    return note_type

def get_note_name(note_number, note_type):
    # Get the note name based on the note number and type
    return note_mapping[note_number] if note_type == 'name' else [note_mapping[note_number][-1]]

def check_answers(notes, answers, note_type):
    # Check the user's answers
    correct_count = 0
    incorrect_notes = []
    for i, note in enumerate(notes):
        try:
            correct_answers = get_note_name(note, note_type)
            if answers[i] in correct_answers:
                correct_count += 1
            else:
                incorrect_notes.append((i+1, note, correct_answers[0]))
        except IndexError:
            print(f"No answer provided for note {i+1}.")
    if correct_count == len(notes):
        print('All answers are correct. Good job!')
    else:
        for note_number, note, correct_answer in incorrect_notes:
            print(f'Number {note_number} (note {note}) is incorrect. The correct answer is {correct_answer}.')
    return correct_count

def music_note_practice(group_size, note_type):
    # Generate notes
    notes = generate_notes(group_size)
    print(f'Notes: {notes}')

    # Get user's answers
    answers = input(f'Enter the {note_type}s for all notes, separated by spaces or commas: ')
    answers = [answer for answer in re.split(',| ', answers) if answer]

    # Check answers and return the number of correct answers
    return check_answers(notes, answers, note_type)

def get_group_size():
    while True:
        group_size = int(input('Enter the group size (1-7): '))
        if 1 <= group_size <= 7:
            return group_size
        else:
            print('Invalid input. Please enter a number between 1 and 7.')

def run_practice(num_runs, group_size, note_type):
    total_correct = 0
    total_questions = num_runs * group_size
    run_times = []
    for i in range(num_runs):
        start_time = time.time()
        print(f'Running practice {i+1} of {num_runs}.')
        total_correct += music_note_practice(group_size, note_type)
        end_time = time.time()
        run_time = end_time - start_time
        run_times.append(run_time)
        print(f'Time for run {i+1}: {run_time * 1000} ms\n')

    # Calculate and print the percentage of correct answers
    correct_percentage = (total_correct / total_questions) * 100
    print(f'You got {correct_percentage}% correct!')

    # Print the average time for all runs
    average_time = sum(run_times) / len(run_times)
    print(f'Average time for all runs: {average_time * 1000} ms')

# Get user inputs
num_runs = int(input('Enter the number of runs: '))
group_size = get_group_size()
note_type = get_note_type()

# Run the practice program
run_practice(num_runs, group_size, note_type)