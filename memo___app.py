from PyQt5.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from memo_data import Question
quests = []
menu_win = QWidget()
win_card = None

lb_quest = QLabel('Введіть запитання:')
lb_right_ans2 = QLabel('Введіть вірну відповідь:')
lb_wrong_ans1 = QLabel('Введіть першу хибну відповідь')
lb_wrong_ans2 = QLabel('Введіть другу хибну відповідь')
lb_wrong_ans3 = QLabel('Введіть третю хибну відповідь')


le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()


lb_header_stat = QLabel('Статистика')
lb_header_stat.setStyleSheet('font-size: 19px; font-weight: bold;')


lb_statistic = QLabel()


vl_labels = QVBoxLayout()
vl_labels.addWidget(lb_quest)
vl_labels.addWidget(lb_right_ans2)
vl_labels.addWidget(lb_wrong_ans1)
vl_labels.addWidget(lb_wrong_ans2)
vl_labels.addWidget(lb_wrong_ans3)


vl_lineEdits = QVBoxLayout()
vl_lineEdits.addWidget(le_question)
vl_lineEdits.addWidget(le_right_ans)
vl_lineEdits.addWidget(le_wrong_ans1)
vl_lineEdits.addWidget(le_wrong_ans2)
vl_lineEdits.addWidget(le_wrong_ans3)


hl_question = QHBoxLayout()
hl_question.addLayout(vl_labels)
hl_question.addLayout(vl_lineEdits)


btn_back = QPushButton('Назад')
btn_add_question = QPushButton('Додати запитання')
btn_clear = QPushButton('Очистити')
hl_buttons = QHBoxLayout()
hl_buttons.addWidget(btn_add_question)
hl_buttons.addWidget(btn_clear)


vl_res = QVBoxLayout()
vl_res.addLayout(hl_question)
vl_res.addLayout(hl_buttons)
vl_res.addWidget(lb_header_stat)
vl_res.addWidget(lb_statistic)
vl_res.addWidget(btn_back)

def giveWinCard(widget):
    global win_card
    win_card = widget

def addQuest():
    quests.append(Question(le_question.text(), le_right_ans.text(), le_wrong_ans1.text(), le_wrong_ans2.text(), le_wrong_ans3.text()))

def countResults(quest):
    progress = 0
    if quest.count_asked != 0:
        progress = quest.count_right/quest.count_asked*100
    
    lb_statistic.setText(
f'''Разів відповіли: {quest.count_asked}
Вірних відповідей: {quest.count_right}
Успішність: {progress}%''')
    
def closeMenu():
    menu_win.hide()
    win_card.show()

def clean():
    le_question.setText('')
    le_right_ans.setText('')
    le_wrong_ans1.setText('')
    le_wrong_ans2.setText('')
    le_wrong_ans3.setText('')

btn_add_question.clicked.connect(addQuest)
btn_back.clicked.connect(closeMenu)
btn_clear.clicked.connect(clean)

menu_win.setLayout(vl_res)
menu_win.resize(400, 300)