from questions_filipino import questions_filipino
from questions_math import questions_math

def question_bank(subject):

    subject = subject.lower()  #case-insensitivity
    match subject:
        case "filipino":
            return questions_filipino
        case "math":
            return questions_math
        case _:
            return "Subject not found"
