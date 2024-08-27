import random
from question import TrueFalseQuestion, MultipleChoiceQuestion

# ExamReviewer Class: Manages the overall exam review session    
class ExamReviewer:    
    def __init__(self, question_bank):
        self.question_bank = question_bank  # Store the question bank
        
    # Method to generate a list of random questions from the question bank  
    def generate_random_questions(self, num_questions=5):
        # Ensure that we don't request more questions than are available
        num_questions = min(num_questions, len(self.question_bank))
        
        # Select a random subset of questions
        selected_questions = random.sample(self.question_bank, num_questions)
        
        # Create a list to store the selected Question objects
        questions = []
        
        # For each selected question ID, create a Question object
        for question_data in selected_questions:
            question_text = question_data['question_text']
            options = question_data['options']
            correct_answer = question_data['correct_answer']
            
            # Create a Question object and add it to the list
            if len(options) == 2:
                # If there are 2 options, create a TrueFalseQuestion object
                question = TrueFalseQuestion(question_text, options, correct_answer)
            else:
                # Otherwise, create a MultipleChoiceQuestion object
                question = MultipleChoiceQuestion(question_text, options, correct_answer)
            questions.append(question)
        
        # Return the list of Question objects
        return questions
    
    # Method to generate a performance report for the student
    def generate_report(self, student):
        return student.get_performance_report()
    
class PerformanceAnalysis:
    def __init__(self, student: object, generated_questions):
        self.student = student
        self.generated_questions = generated_questions

    # Method to generate and return a performance report for the student
    def print_performance_report(self, time_taken):
        print(self.student.get_performance_report())
        print(f"Time taken: {time_taken}")

    # Method to create exam review
    def create_exam_review(self):
        print("----------------EXAM REVIEWER----------------")
        for i, question in enumerate(self.generated_questions, start=1):
            print(f"\nQuestion {i}:\n")
            question.display_question()
            print("")
            print("Correct Answer:", question.get_correct_answer())
            answers = [x[1] for x in self.student.answers]
            print("Your Answer:", answers[i - 1])  # Adjust index to match question number
            print("")
    
    def save_exam_review_to_file(self, file_name="exam_reviewer.txt"):
        try:
            with open(file_name,'w') as file:
                file.write("----------------EXAM REVIEWER----------------\n")
                for i, question in enumerate(self.generated_questions, start=1):
                    file.write(f"\nQuestion {i}:\n")
                    # Capture the output of display_question and write it to the file
                    file.write(f"{question.question_text}\n")
                    for option in question.options:
                        file.write(f"{option}\n")
                    file.write("\n")
                    file.write("Correct Answer: " + question.get_correct_answer() + "\n")
                    answers = [x[1] for x in self.student.answers]
                    file.write("Your Answer: " + answers[i - 1] + "\n")
                    file.write("\n")
            print(f"All questions and answers have been saved to {file_name}")
        except Exception as e:
            print(f"An error occurred while saving questions to file: {e}")