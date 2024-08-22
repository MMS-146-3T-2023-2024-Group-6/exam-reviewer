from student import Student
from examreviewer import ExamReviewer
from questionbank import question_bank

# Main program loop
def main():

    
    # Prompt the user for their name and create a new student instance
    student_name = input("Enter your name: ")
    student = Student(student_name)

    # Prompt the user to choose a subject
    subject = input("Choose a subject: \n Math \n Filipino \n \n")

    # Initialize ExamReviewer with the question bank depending on subject
    reviewer = ExamReviewer(question_bank(subject))
    
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