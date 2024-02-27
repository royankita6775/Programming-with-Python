print("Welcome to the quiz!")
print("Take quiz 1 to test your Finnish vocabulary for week names OR quiz 2 to test your Finnish vocabulary for month names!")


playing = input("Do you want to play quiz 1 or quiz 2: ")

if playing == "1" :
    class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

    question_prompts = [
        "What does 'Maanantai' mean?\n(a) 'Monday'\n(b)'Saturday'\n(c)'Thursday'",'\n'
        "What does 'Tiistai' mean?\n(a) 'Sunday'\n(b)'Tuesday'\n(c)'Monday'",'\n'
        "What does 'Sunnuntai' mean?\n (a) 'Saturday'\n (b) 'Tuesday'\n(c)'Sunday'", '\n'
        "What does 'Torstai' mean?\n (a) 'Tuesday'\n (b) 'Thursday'\n(c)'Friday'", '\n'
        "What does 'Lauantai' mean?\n (a) 'Saturday'\n (b) 'Wednesday'\n(c)'Thursday'", '\n'
        "What does 'Perjantai' mean?\n (a) 'Friday'\n (b) 'Wednesday'\n(c)'Thursday'", '\n'
        "What does 'Keskiviikko' mean?\n (a) 'Tuesday'\n (b) 'Friday'\n(c)'Wednesday'", '\n'
    ]

    name = input("Please enter a username: ").title()
    questions = [
        Question(question_prompts[0], "a"),
        Question(question_prompts[1], "b"),
        Question(question_prompts[2], "c"),
        Question(question_prompts[3], "b"),
        Question(question_prompts[4], "a"),
        Question(question_prompts[5], "a"),
        Question(question_prompts[6], "c")
        ]
    def run_quiz(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            if answer == question.answer:
                score += 1
        print("\n{0}, you scored {1} out of {2}.".format(name, score, len(questions)))
    run_quiz(questions)

elif playing == "2":
    class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

    question_prompts = [
        "What does 'Helmikuu' mean?\n(a) 'March'\n(b)'February'\n(c)'January'",'\n'
        "What does 'Maaliskuu' mean?\n(a) 'January'\n(b)'April'\n(c)'March'",'\n'
        "What does 'Lukakuu' mean?\n (a) 'October'\n (b) 'July'\n(c)'April'", '\n'
        "What does 'Kesäkuu' mean?\n (a) 'August'\n (b) 'June'\n(c)'May'", '\n'
        "What does 'Toukokuu' mean?\n (a) 'April'\n (b) 'May'\n(c)'June'", '\n'
        "What does 'Syyskuu' mean?\n (a) 'September'\n (b) 'January'\n(c)'April'", '\n'
        "What does 'Elokuu' mean?\n (a) 'July'\n (b) 'August'\n(c)'June'", '\n',
        "What does 'Huhtikuu' mean?\n (a) 'July'\n (b) 'April'\n(c)'June'", '\n',
        "What does 'Tammikuu' mean?\n (a) 'January'\n (b) 'April'\n(c)'July'", '\n',
        "What does 'Heinäkuu' mean?\n (a) 'July'\n (b) 'February'\n(c)'May'", '\n',
        "What does 'Joulukuu' mean?\n (a) 'January'\n (b) 'December'\n(c)'July'", '\n',
        "What does 'Marraskuu' mean?\n (a) 'January'\n (b) 'November'\n(c)'July'", '\n',
    ]

    name = input("Please enter a username: ").title()
    questions = [
        Question(question_prompts[0], "b"),
        Question(question_prompts[1], "c"),
        Question(question_prompts[2], "a"),
        Question(question_prompts[3], "b"),
        Question(question_prompts[4], "b"),
        Question(question_prompts[5], "a"),
        Question(question_prompts[6], "b"),
        Question(question_prompts[7], "b"),
        Question(question_prompts[8], "a"),
        Question(question_prompts[9], "a"),
        Question(question_prompts[10], "b"),
        Question(question_prompts[11], "b")        
        ]
    def run_quiz(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            if answer == question.answer:
                score += 1
        print("\n{0}, you scored {1} out of {2}.".format(name, score, len(questions)))
    run_quiz(questions)  

else:
    print("Invaild input :( \nPlease try again")
    quit()          

