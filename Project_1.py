class Question:
    def __init__(self, q, a):
        self.quiz_question = q
        self.quiz_answer = a

football_questions = [
    Question('Who won the most Ballon d\'Or in football history?\n(a) Messi\n(b) C. Ronaldo\n(c) Mbappe\n(d) Neymar\n', 'a'),
    Question('Who won FIFA World Cup in 2022?\n(a) Brazil\n(b) Portugal\n(c) France\n(d) Argentina\n', 'd'),
    Question('Who won Euro Cup in 2020?\n(a) Portugal\n(b) Italy\n(c) France\n(d) Netherlands\n', 'b'),
    Question('Who hosted FIFA World Cup in 2014?\n(a) Italy\n(b) Australia\n(c) Brazil\n(d) England\n', 'c')
]

cricket_questions = [
    Question('Who is the captain of India in 2011?\n(a) V. Kohli\n(b) Sachin\n(c) Dhoni\n(d) R. Sharma\n', 'c'),
    Question('Who hit 6 sixes in an over?\n(a) Ricky Ponting\n(b) Chris Gayle\n(c) Sachin\n(d) Yuvraj Singh\n', 'd'),
    Question('Who won the Cricket World Cup in 2023?\n(a) Australia\n(b) India\n(c) England\n(d) Sri Lanka\n', 'a'),
    Question('Who scored the first 200 in a World Cup?\n(a) Sachin\n(b) Chris Gayle\n(c) Sehwag\n(d) B. McCullum\n', 'b')
]

movie_questions = [
    Question('Who won the Best Actor National Award in 2022?\n(a) Surya\n(b) Allu Arjun\n(c) Vikram\n(d) Dhanush\n', 'a'),
    Question('Who directed the movie "Manichithrathazhu"?\n(a) Sibi Malayil\n(b) Bharathan\n(c) Padmarajan\n(d) Fazil\n', 'd'),
    Question('Best director of 2023?\n(a) Rajamouli\n(b) Nikhil Mahajan\n(c) R. Hirani\n(d) S. Shankar\n', 'b'),
    Question('Best music director of 2023?\n(a) A.R Rahman\n(b) Illairaja\n(c) Devi Sri Prasad\n(d) Vidya Sagar\n', 'c')
]

politics_questions = [
    Question('Who is the first Prime Minister of India?\n(a) Abdul Kalam\n(b) Nehru\n(c) Vajpayee\n(d) Manmohan Singh\n', 'b'),
    Question('Who is the Education Minister of Kerala?\n(a) Veena George\n(b) G.R. Anil\n(c) V. Shivankutty\n(d) R. Bindu\n', 'c'),
    Question('Who is the current President of India?\n(a) Pratibha Patil\n(b) Rajendra Prasad\n(c) Ram Nath Kovind\n(d) Droupati Murmu\n', 'c'),
    Question('Who is the CM of Kerala?\n(a) Pinarayi Vijayan\n(b) K. Balakrishnan\n(c) Oommen Chandy\n(d) Balagopal\n', 'a')
]

def run_politics_questions():
    score = 0
    for question in politics_questions:
        answer = input(question.quiz_question)
        if answer.lower() != question.quiz_answer:
            print('Your answer is incorrect! The correct answer is', question.quiz_answer)
        else:
            print('Your answer is correct! You have got 5 points')
            score += 5
    print(f'You got {score // 5} correct answers')
    return f'You got total points {score} out of {len(politics_questions) * 5}'

def run_cricket_questions():
    score = 0
    for question in cricket_questions:
        answer = input(question.quiz_question)
        if answer.lower() != question.quiz_answer:
            print('Your answer is incorrect! The correct answer is', question.quiz_answer)
        else:
            print('Your answer is correct! You have got 5 points')
            score += 5
    print(f'You got {score // 5} correct answers')
    return f'You got total points {score} out of {len(cricket_questions) * 5}'

def run_football_questions():
    score = 0
    for question in football_questions:
        answer = input(question.quiz_question)
        if answer.lower() != question.quiz_answer:
            print('Your answer is incorrect! The correct answer is', question.quiz_answer)
        else:
            print('Your answer is correct! You have got 5 points')
            score += 5
    print(f'You got {score // 5} correct answers')
    return f'You got total points {score} out of {len(football_questions) * 5}'

def run_movie_questions():
    score = 0
    for question in movie_questions:
        answer = input(question.quiz_question)
        if answer.lower() != question.quiz_answer:
            print('Your answer is incorrect! The correct answer is', question.quiz_answer)
        else:
            print('Your answer is correct! You have got 5 points')
            score += 5
    print(f'You got {score // 5} correct answers')
    return f'You got total points {score} out of {len(movie_questions) * 5}'

print('Welcome to the WORLD of QUIZ GAME!')
playing = input('Do you want to play?:  ').lower()
if playing != 'yes':
    print('Okay, maybe next time!')
else:
    print('Okay, let us play :)')

question_type = input('Which type of questions do you want?\nMovies\nSports\nPolitics\n').lower()

if question_type == 'sports':
    sports_type = input('Which type of sports do you want?\nFootball\nCricket\n').lower()
    if sports_type == 'football':
        print('There will be 4 options in your hand! You have to choose one option as given in the question')
        print(run_football_questions())
    elif sports_type == 'cricket':
        print('There will be 4 options in your hand! You have to choose one option as given in the question')
        print(run_cricket_questions())
elif question_type == 'movies':
    print('There will be 4 options in your hand! You have to choose one option as given in the question')
    print(run_movie_questions())
elif question_type == 'politics':
    print('There will be 4 options in your hand! You have to choose one option as given in the question')
    print(run_politics_questions())
