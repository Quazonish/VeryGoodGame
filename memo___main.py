from memo___card_layout import *
from PyQt5.QtWidgets import QWidget
from random import shuffle # перемішуватимемо відповіді у картці питання
from memo_data import Question
from time import sleep
from memo___app import *
from random import choice

card_width, card_height = 600, 500 # початкові розміри вікна "картка"

app = QApplication([])

win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300, 300)
win_card.setWindowTitle("Memory card")

q1 = Question('Яблуко', 'apple', 'application', 'builder', 'car')

quests.append(q1)
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def newQuests():
    global quest
    quest = choice(quests)
    shuffle(radio_list)
    lb_Question.setText(quest.question)
    lb_Correct.setText(quest.answer)
    radio_list[0].setText(quest.answer)
    radio_list[1].setText(quest.wrong_answer1)
    radio_list[2].setText(quest.wrong_answer2)
    radio_list[3].setText(quest.wrong_answer3)

def check_result():
    RadioGroup.setExclusive(False)
    for answer in radio_list:
        if answer.isChecked():
            if answer.text() == lb_Correct.text():
                quest.got_right()
                lb_Correct.setText("Вірно!")
                answer.setChecked(False)
                break
            else:
                quest.got_wrong()
                lb_Correct.setText("Не вірно!")
    RadioGroup.setExclusive(True)

def click_OK():
   # поки що перевіряємо питання, якщо ми в режимі питання, інакше нічого
   if btn_OK.text() == 'Наступне питання':
       check_result()
       RadioGroupBox.hide()
       AnsGroupBox.show()
       btn_OK.setText('Відповісти')
   else:
       newQuests()
       RadioGroupBox.show()
       AnsGroupBox.hide()
       btn_OK.setText('Наступне питання')
       

def rest():
    win_card.hide()
    sleep(box_Minutes.value()*60)
    win_card.show()

def openMenu():
    countResults(quest)
    win_card.hide()
    menu_win.show()

newQuests()
show_question()
btn_OK.clicked.connect(click_OK)
btn_Sleep.clicked.connect(rest)
btn_Menu.clicked.connect(openMenu)

win_card.setLayout(layout_card)
win_card.show()
giveWinCard(win_card)

app.exec_()