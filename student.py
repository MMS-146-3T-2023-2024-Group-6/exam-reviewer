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
    