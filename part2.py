from enchant.checker import SpellChecker
from random import randint

#create functions to match rubric

#function to check for spelling errors as 15% of total score
def chkr_set_text(filename):
    chkr = SpellChecker("en_GB")
    #open file, read and check for errors in text
    with open(filename, "r",encoding='utf-8') as F:
        text = F.read()
    chkr.set_text(text)
    error_word = []
    spelling_score = 0
    for err in chkr:
        error_word.append(err.word)
        if len(error_word) >= 30:
            spelling_score = randint(4,5)
        elif len(error_word) <= 25:
            spelling_score = randint(6,9)
        elif len(error_word) <= 10:
            spelling_score = randint(9,10)
    spelling_score = spelling_score *1.5
    return spelling_score
    
#clarity and simplicity 15% of total score
def simplicity_clarity(filename):
    #list of regular words
    regular_words = ["and","is","very","also","because","like","if","then"]
    for word in regular_words:
        if len(regular_words) >= 70:
            regular_words_score = randint(4,5)
        elif len(regular_words) == 50:
            regular_words_score = randint(6,8)
        elif len(regular_words) < 30:
            regular_words_score = randint(9,10)  
    regular_words_score = regular_words_score * 1.5
    return regular_words_score

#cognitive ability 20% of total score
def TTR_score(filename):
    TTR = text_TTR(filename)
    TTR = int(TTR * 100)
    TTR_score = 0
    if TTR >= 25:
        TTR_score = 1
    elif TTR == 25:
        TTR_score = 0.5
    elif TTR <= 10:
        TTR_score = TTR/30
    TTR_score = TTR_score *20
    return TTR_score

#length 50% of total score
def length_score(filename):
    length = len(book_segments(filename))
    if length >= 60:
        length_score = randint(9,10)
    elif length <= 60:
        length_score = randint(4,6)
    elif length <20:
        length_score = randint(2,4)
    length_score = length_score * 5
    return length_score
#final grade as a percentage
def final_grade(filename):
    a = chkr_set_text(filename)
    b = simplicity_clarity(filename)
    c = TTR_score(filename)
    d = length_score(filename)
    
    final_grade = a+b+c+d
    return final_grade
#final grade assigment        
def gradescores(filename):
    finalgrade = final_grade(filename)
    if finalgrade >= 85:
        print("You received an A")
    elif finalgrade >= 75:
        print("You received a B")
    elif finalgrade >= 65:
        print("You received a C")
    elif finalgrade >= 55:
        print("You received a D")
    else:
        print("Sorry, you received an F")
    
gradescores("Gallant.txt")