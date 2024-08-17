import random

# Sample Question Bank
question_bank = {
    1: {
        "question_text": "What is the capital of France?",
        "options": ["Paris", "London", "Rome", "Berlin"],
        "correct_answer": "Paris"
    },
    2: {
        "question_text": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "correct_answer": "Mars"
    },
    3: {
        "question_text": "True or False: The Sun is a star.",
        "options": ["True", "False"],
        "correct_answer": "True"
    },
    4: {
        "question_text": "Which element has the chemical symbol 'O'?",
        "options": ["Gold", "Oxygen", "Silver", "Helium"],
        "correct_answer": "Oxygen"
    },
    5: {
        "question_text": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "correct_answer": "Pacific Ocean"
    }
}

# Question Class: Represents a single question in the exam reviewer
class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    # Method to display the question and its options
    def display_question(self):
        print(f"Question: {self.question_text}")
        for option in self.options:
            print(option)

    # Method to check if the user's answer is correct
    def check_answer(self, user_answer):
        return user_answer == self.correct_answer
    
# Student Class: Represents a student taking the exam review
class Student:
    def __init__(self, name):
        self.name = name
        self.answers = []  # List to store the student's answers
        
    # Method to save the student's answer for a particular question    
    def save_answer(self, question, answer):
        self.answers.append((question, answer))

    # Method to generate and return a performance report for the student
    def get_performance_report(self):
        # Initialize a counter for correct answers
        correct_answers = 0
        
        # Loop through each question and answer the student provided
        for question, answer in self.answers:
            # Check if the student's answer is correct
            if question.check_answer(answer):
                # If correct, increase the correct_answers counter by 1
                correct_answers += 1
        
        # Get the total number of questions the student answered
        total_questions = len(self.answers)
        
        # Calculate the score as a percentage
        if total_questions > 0: # Avoid division by zero
            score = (correct_answers / total_questions) * 100
        else:
            score = 0 # If no questions were answered, set score to 0
        
        # Create and return a performance report string
        return f"Performance Report for {self.name}:\nCorrect Answers: {correct_answers}/{total_questions}\nScore: {score}%"
    
# ExamReviewer Class: Manages the overall exam review session    
class ExamReviewer:    
    def __init__(self, question_bank):
        self.question_bank = question_bank  # Store the question bank
        
    # Method to generate a list of random questions from the question bank  
    def generate_random_questions(self, num_questions=5):
        # Get a list of all question IDs
        all_question_ids = list(self.question_bank.keys())
        
        # Select a random subset of question IDs
        selected_question_ids = random.sample(all_question_ids, num_questions)
        
        # Create a list to store the selected Question objects
        questions = []
        
        # For each selected question ID, create a Question object
        for q_id in selected_question_ids:
            question_data = self.question_bank[q_id]
            question_text = question_data['question_text']
            options = question_data['options']
            correct_answer = question_data['correct_answer']
            
            # Create a Question object and add it to the list
            question = Question(question_text, options, correct_answer)
            questions.append(question)
        
        # Return the list of Question objects
        return questions

    # Placeholder method for customizing the review session (not implemented here)
    def customize_session(self):
        pass
    
    # Method to generate a performance report for the student
    def generate_report(self, student):
        return student.get_performance_report()
        
# Main program loop
def main():
    # Initialize ExamReviewer with the question bank
    reviewer = ExamReviewer(question_bank)
    
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