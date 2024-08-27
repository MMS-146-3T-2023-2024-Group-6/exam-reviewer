from student import Student
from examreviewer import ExamReviewer, PerformanceAnalysis
from questionbank import question_bank
import time

# Main program loop
def main():

    # Prompt the user for their name and create a new student instance
    student_name = input("Enter your name: ")
    student = Student(student_name)

    # Prompt the user to choose a subject
    while True:
        subject = input("Choose a subject: \n Math \n Filipino \n \n")
        subject = subject.lower()  # case-insensitivity
        result = question_bank(subject)

        if result == "Subject not found":
            print("No reviewer available. Please enter a valid subject.")
        else:
            break  # Exit the loop if a valid subject is found

    # Prompt the user to choose the number of questions
    while True:
        try:
            num_questions = int(input("Choose the number of questions (5, 10, 15): "))
            if num_questions not in (5, 10, 15):
                raise ValueError
            break  # Exit the loop if a valid number of questions is entered
        except ValueError:
            print("Invalid number of questions. Please enter 5, 10, or 15.")

    # Initialize ExamReviewer with the question bank depending on subject
    reviewer = ExamReviewer(question_bank(subject))

    # Generate random questions for the review session
    questions = reviewer.generate_random_questions(num_questions)

    # Start the timer
    start_time = time.time()

    # Ask each question to the student and save their answer
    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}:")
        question.display_question()
        answer = input("Your answer: ")
        student.save_answer(question, answer)

    # End the timer and calculate the elapsed time
    end_time = time.time()
    elapsed_time = int(end_time - start_time)

    # Calculate hours, minutes, and seconds
    hours = elapsed_time // 3600
    minutes = (elapsed_time % 3600) // 60
    seconds = elapsed_time % 60

    # Format the time taken
    time_taken = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    perf_analysis_test = PerformanceAnalysis(student, questions)
    perf_analysis_test.print_performance_report(time_taken)

    # Generate and display the performance report, including time taken
    while True:
        x = input("Do you want to review the exam? Y/N \n").upper()
        if x == "Y":
            perf_analysis_test.create_exam_review()
            ask_to_save = input("Would you like to save the report into a text file? Y/N \n").upper()
            if ask_to_save == "Y":
                perf_analysis_test.save_exam_review_to_file()
            print("Session Ended")
            raise SystemExit
        elif x == "N":
            print("Session Ended")
            raise SystemExit


# Run the program
main()
