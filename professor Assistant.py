import random
import os


def main():
    print("Welcome to professor assistant version 1.0.")

    # 1. Get Professor's Name
    prof_name = input("Please Enter Your Name: ")
    print(f"Hello Professor. {prof_name}, I am here to help you create exams from a question bank.")

    # 2. Main Program Loop
    while True:
        # Ask to proceed
        choice = input(f"Do you want me to help you create an exam (Yes to proceed | No to quit the program)? ")

        # Check if user wants to quit
        # We use .lower() to make it case-insensitive (handles 'No', 'no', 'NO')
        if choice.strip().lower() == 'no':
            print(f"Thank you professor {prof_name}. Have a good day!")
            break

        elif choice.strip().lower() == 'yes':
            # Ask for the path to the question bank
            bank_filename = input("Please Enter the Path to the Question Bank. ")

            # Check if file exists to prevent crashing
            if not os.path.exists(bank_filename):
                print("Error: The file path provided does not exist. Please try again.")
                continue

            print("Yes, indeed the path you provided includes questions and answers.")

            # --- READING THE FILE ---
            questions_and_answers = []

            try:
                with open(bank_filename, 'r') as file:
                    lines = file.readlines()

                    # Logic: We step through the lines 2 at a time.
                    # i is the index of the Question. i+1 is the index of the Answer.
                    for i in range(0, len(lines), 2):
                        if i + 1 < len(lines):  # Ensure there is an answer for the question
                            q = lines[i].strip()
                            a = lines[i + 1].strip()
                            questions_and_answers.append((q, a))  # Store as a tuple
            except Exception as e:
                print(f"An error occurred reading the file: {e}")
                continue

            # --- GATHERING EXAM DETAILS ---
            try:
                num_questions = int(input("How many question-answer pairs do you want to include in your exam? "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            # Validation: Ensure we don't ask for more questions than exist in the bank
            if num_questions > len(questions_and_answers):
                print(
                    f"Warning: You asked for {num_questions}, but the bank only has {len(questions_and_answers)}. Using all available questions.")
                num_questions = len(questions_and_answers)

            output_filename = input("Where do you want to save your exam? ")

            # --- SELECTING RANDOM QUESTIONS USING RANDINT ---
            selected_exam_questions = []

            # Create a copy of the list indices to track which ones we've used
            # (to avoid picking the same question twice)
            available_indices = list(range(len(questions_and_answers)))

            for _ in range(num_questions):
                # Generate a random index based on how many are left
                # randint(0, length - 1)
                random_pos = random.randint(0, len(available_indices) - 1)

                # Get the actual index from our available list
                selected_index = available_indices[random_pos]

                # Add that question pair to our exam
                selected_exam_questions.append(questions_and_answers[selected_index])

                # Remove the used index so we don't pick it again
                available_indices.pop(random_pos)

            # --- WRITING THE OUTPUT FILE ---
            with open(output_filename, 'w') as outfile:
                for q, a in selected_exam_questions:
                    outfile.write(f"{q}\n")
                    outfile.write(f"{a}\n")

            print(f"Congratulations Professor {prof_name}. Your exam is created and saved in {output_filename}.")

        else:
            print("Invalid input. Please type Yes or No.")


# Standard boilerplate to run the main function
if __name__ == "__main__":
    main()