from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import pyqtSignal  # Імпортуємо pyqtSignal

class MenuWindow(QWidget):
    # Створюємо сигнал, який буде передавати словник із новим питанням
    new_question_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Додати нове питання')
        self.setGeometry(100, 100, 400, 300)

        # Створюємо віджети для введення даних
        self.question_label = QLabel('Введіть запитання:')
        self.question_input = QLineEdit()

        self.right_answer_label = QLabel('Введіть вірну відповідь:')
        self.right_answer_input = QLineEdit()

        self.wrong1_label = QLabel('Введіть першу хибну відповідь:')
        self.wrong1_input = QLineEdit()

        self.wrong2_label = QLabel('Введіть другу хибну відповідь:')
        self.wrong2_input = QLineEdit()

        self.wrong3_label = QLabel('Введіть третю хибну відповідь:')
        self.wrong3_input = QLineEdit()

        self.add_question_button = QPushButton('Додати запитання')
        self.clear_button = QPushButton('Очистити')

        # Прив'язуємо кнопку для додавання питання до функції
        self.add_question_button.clicked.connect(self.add_question)

        # Створюємо розмітку
        layout = QVBoxLayout()
        layout.addWidget(self.question_label)
        layout.addWidget(self.question_input)

        layout.addWidget(self.right_answer_label)
        layout.addWidget(self.right_answer_input)

        layout.addWidget(self.wrong1_label)
        layout.addWidget(self.wrong1_input)

        layout.addWidget(self.wrong2_label)
        layout.addWidget(self.wrong2_input)

        layout.addWidget(self.wrong3_label)
        layout.addWidget(self.wrong3_input)

        layout.addWidget(self.add_question_button)
        layout.addWidget(self.clear_button)

        self.setLayout(layout)

    def add_question(self):
        ''' Збирає дані про питання і передає їх через сигнал '''
        question_data = {
            'question': self.question_input.text(),
            'right': self.right_answer_input.text(),
            'wrong': [
                self.wrong1_input.text(),
                self.wrong2_input.text(),
                self.wrong3_input.text()
            ]
        }

        # Відправляємо сигнал з новим питанням
        self.new_question_signal.emit(question_data)

        # Очищуємо поля після додавання
        self.clear_fields()

    def clear_fields(self):
        ''' Очищає всі поля після додавання питання '''
        self.question_input.clear()
        self.right_answer_input.clear()
        self.wrong1_input.clear()
        self.wrong2_input.clear()
        self.wrong3_input.clear()


