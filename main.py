from student import Student
from examreviewer import ExamReviewer
from questions_math import questions_math

# Main program loop
def main():
    # Initialize ExamReviewer with the question bank
    reviewer = ExamReviewer(questions_math)
    
    # Prompt the user for their name and create a new student instance
    student_name = input("Enter your name: ")
    student = Student(student_name)
    
    # Generate random questions for the review session
    questions = reviewer.generate_random_questions()

    # Ask each question to the student and save their answer
    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}:")
        question.display_question()
        answer = input("Your answer: ")
        student.save_answer(question, answer)

    # Generate and display the performance report
    report = reviewer.generate_report(student)
    print("\n" + report)


# Run the program
main()