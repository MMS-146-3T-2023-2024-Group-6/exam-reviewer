from questions_filipino import questions_filipino
from questions_math import questions_math

# Question Bank method goes here

def question_bank(subject):
    # This returns the subject dictionary depending on what is chosen.
    match subject:
        case "Filipino":
            return questions_filipino
        case "Math":
            return questions_math
        case _:
            return "Subject not found"