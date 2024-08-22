# Question Class Goes here

class Question:
    """
    Initiate base Question class

    question_text: Text of the question
    correct_answer: The designated correct answer
    """
    def __init__(self, question_text, correct_answer):
        self.question_text = question_text        # Private attribute
        self.__correct_answer = correct_answer      # Private attribute
    
    """
    Method to check if user's answer is correct    
    """
    def check_answer(self, user_answer):
        return user_answer == self.__correct_answer

class TrueFalseQuestion(Question):
    """
    Initiate a True/False Question
    options: an array with True and False
    """
    def __init__(self, question_text, options, correct_answer):
        super().__init__(question_text, correct_answer)
        """
        If the question provides different options aside from True/False, use those.
        Otherwise use True/False

        """
        if options != ["True", "False"]:
            self.__options = options        
        else:
            self.__options = ["True, False"]

    """
    Method to display the question and the true/false options    
    """
    def display_question(self):
        print(f"{self.question_text}")
        for option in self.__options:
            print(option)

class MultipleChoiceQuestion(Question):
    """
    Initiate a Multiple Choice Question
    options: an array with all the possible answers (minimum of 4)
    """
    def __init__(self, question_text, options, correct_answer):
        super().__init__(question_text, correct_answer)
        self.__options = options                    # Private attribute
    
    """
    Method to display the question and all the options    
    """
    def display_question(self):
        print(f"{self.question_text}")
        for option in self.__options:
            print(option)