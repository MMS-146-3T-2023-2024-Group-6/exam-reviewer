class PerformanceAnalysis:
    def __init__(self, student:object, reviewer):
        self.student = student
        self.reviewer = reviewer

 # Method to generate and return a performance report for the student
    def print_performance_report (self):
        print(self.student.get_performance_report())

 # Method to review or end sessions
    def exam_review (self):
        x = str(input("Do you want to review or end session? Y/N \n"))

        if x == "Y":
            print("----------------EXAM REVIEWER----------------")
            y = 0
            for i, question in enumerate(self.reviewer, start=1):
                print(f"\nQuestion {i}:\n")
                question.display_question()
                print("")
                print("Corrrect Answer:", question.get_correct_answer())
                answers = [x[1] for x in self.student.answers]
                print("Your Answer:", answers[y])
                print("")
                y += 1
            
        elif x == "N":
            print("Session Ended")
            raise SystemExit

        else:
            print("invalid input")

            self.exam_review()

    