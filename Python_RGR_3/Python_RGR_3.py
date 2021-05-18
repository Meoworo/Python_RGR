import turtle
from random import randint

#-----------------------окно--------------------------------------------
screen = turtle.Screen()
screen.setup(1200, 900)
screen.delay(0)
#------------------настройка кисти---------------------------------------
brush = turtle.Turtle()
brush.pensize(3)
brush.speed(10)
brush.penup()
brush.setpos(0, -400)
brush.pendown()
brush.color('brown')
brush.hideturtle()                      #скрыть кисть
#-----------------------ветви--------------------------------------------

# - лево
# + право
# [ сохранение параметров
# ] возврат к параметрам
# X функция (rule)
# Y конец
# @ разветвление

buffer = []
gens = 14                               #максимальный уровень
axiom = 'XY'
chrX = 'X'
#rule = 'F[@[-X]+X]'
rule = 'F[@-X+X]'
#rule = 'F[@[-X]+X]'
length = 90                             #длина
thick = 26                              #толщина
#------------------------------------------------------------------------
angle = lambda: randint(0, 45)
#angle = lambda: 45

def applyRules(axiom):
    return ''.join([rule if chr == chrX else chr for chr in axiom])

def getFunc(gens, axiom):
    for gen in range(gens):
        axiom = applyRules(axiom)
        #print(axiom,'\n')
    return axiom
#------------------------------------------------------------------------

axiom = getFunc(gens, axiom)            #получение функции полного дерева
brush.left(90)
brush.pensize(thick)

brush.forward(2 * length)               #отрисовка дерева
for chr in axiom:
    if chr == 'F' or chr == 'X':
        brush.forward(length)
        #уменьшение ветвей
    elif chr == '@':
        length -= 6
        thick -= 2
        thick = max(1, thick)
        brush.pensize(thick)
        #правая ветвь
    elif chr == '+':
        brush.right(angle())
        #левая ветвь
    elif chr == '-':
        brush.left(angle())
        #занесение параметров
    elif chr == '[':
        angleSave = brush.heading()
        posSave = brush.pos()
        buffer.append((angleSave, posSave, thick, length))
        #копирование и очистка буфера
    elif chr == ']':
        angleSave, posSave, thick, length = buffer.pop()
        brush.pensize(thick)
        brush.setheading(angleSave)
        brush.penup()
        brush.goto(posSave)
        brush.pendown()
    elif chr == 'Y':
        print('Ready')
        turtle.exitonclick()
