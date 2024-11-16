from PyQt5.QtCore import QTimer
from memo_card_layout import *
from menu import MenuWindow
from PyQt5.QtWidgets import QWidget
from random import shuffle

total_answers = 0
corect_answers = 0

question_list = []
current_question = None

menu_window = None
rest_timer = QTimer()


question_list.append({
    'question': 'Яблуко'
    'right': 'apple'
    'wrong': ['application', 'building', 'caterpillar']
})
def add_new_question(question_data):
    question_list.append(question_data)

def show_data():
    global current_question
    if not question_list:
        lb_Question.setText('')
        return
    shuffle(question_list)
    current_question = question_list.pop(0)
    lb_Question.setText(current_question['question'])
    lb_Correct.setText(current_question['right'])
    radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
    shuffle(radio_list)

    radio_list[0].setText(current_question['right'])
    radio_list[1].setText(current_question['wrong'][0])
    radio_list[2].setText(current_question['wrong'][1])
    radio_list[3].setText(current_question['wrong'][2])

    global answer 
    answer = radio_list

def check_result():
    global total_answers, corect_answers
    total_answers += 1
    correct = answer.isChecked()
    if correct:
        corect_answers += 1
        lb_Result.setText('Правильно!')
    else:
        lb_Result.setText('Неправильно!')
    show_result()

def show_next_question():
    if question_list:
        show_question()
        show_data()
    else:
        show_statistics()
        