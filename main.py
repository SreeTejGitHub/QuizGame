def newGame():

    correct_guess = 0
    question_num = 1
    for key in questions:
        print(key)
        for i in options[question_num-1]:
            print(i)

        userGuess = input('your Answer?: ').upper()
        correct_guess += check_answer(questions.get(key), userGuess)
        print('-------------------')

        question_num += 1
    print('your score is: ' + str(correct_guess))
def check_answer(answer, guess):
    if answer == guess:
        print(guess + ' is right')
        return 1
    else:
        print(guess + ' is wrong')
        return 0
def display_score():
    pass

def play_again():
    response = input(' wanna play again? (yes/no): ')
    response = response.upper()

    if response == 'YES':
        return True
    else:
        return False

questions = {
    'whats the biggest populations?: ': 'A',
    'what is country name?: ': 'B',
    'are you stupid?: ': 'C',
    'idiot?: ': 'A'
}

options = [
    ['A. India', 'B. USA', 'C. Mexico', 'D. Canada'],
    ['A. USA ', 'B. India', 'C. Canada', 'D. Mexico'],
    ['A. no', 'B. Maybe', 'C. Yes', 'D. Just a little bit'],
    ['A. no', 'B. Maybe', 'C. Yes', 'D. Just a little bit']
]


newGame()

while play_again():
    newGame()

print('bye')
