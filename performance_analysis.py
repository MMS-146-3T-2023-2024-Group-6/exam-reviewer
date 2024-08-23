class PerformanceAnalysis:
    def __init__(self, student: object, generated_questions):
        self.student = student
        self.generated_questions = generated_questions

    # Method to generate and return a performance report for the student
    def print_performance_report(self, time_taken):
        print(self.student.get_performance_report())
        print(f"Time taken: {time_taken}")

    # Method to review or end sessions
    def exam_review(self):
        while True:
            x = input("Do you want to review or end session? Y/N \n").upper()

            if x == "Y":
                print("----------------EXAM REVIEWER----------------")
                for i, question in enumerate(self.generated_questions, start=1):
                    print(f"\nQuestion {i}:\n")
                    question.display_question()
                    print("")
                    print("Correct Answer:", question.get_correct_answer())
                    answers = [x[1] for x in self.student.answers]
                    print("Your Answer:", answers[i - 1])  # Adjust index to match question number
                    print("")
                break

            elif x == "N":
                print("Session Ended")
                raise SystemExit

            else:
                print("Invalid Input")
