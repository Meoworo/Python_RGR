import csv, time, subprocess, sys

visio = False
sports_category = {0:'Б/Р', 1:'МС', 2:'КМС',3:'I',4:'II', 5:'III', 6:'1юн', 7:'2юн', 8:'3юн'}
trainers = []
trainers_ = []
athletes = []
athletes_ = []
row = []

#---------------------------------------------------------------------------------------------------------------
def printAthletes(athletes):
    k = 0
    print('Номер\t  .  Фамилия\t  .  Имя\t  .  Год\t  .  Разряд\t  .  Тренер')
    print('.' * 110)
    while k != len(athletes):
        print('%3s'%(athletes[k][0]),athletes[k][1],athletes[k][2],
              athletes[k][3],'%3s'%sports_category.get(athletes[k][4]),trainers[athletes[k][5]][1], sep='\t  .  ')
        k += 1
    print('.' * 110)
    print('Всего легкоатлетов: ', len(athletes),'\n')

def bottomPanel(ats):
    print('1 - Изменить\n2 - Добавить\n3 - Удалить\n4 - Поиск по тренеру\n5 - Открыть файл')
    print('Ваш ', end='')
    while True:
        choice= int(input("выбор: "))
        if choice < 5 and choice > 0:
            break
        else:
            print("Повторите ", end='')

    if choice == 1:
        editAthletes(ats)
        printAthletes(athletes)
        bottomPanel(ats)
    elif choice == 2:
        addAthletes(ats)
        printAthletes(athletes)
        bottomPanel(ats)
    elif choice == 3:
        deleteAthletes(ats)
        printAthletes(athletes)
        bottomPanel(ats)
    elif choice == 4:
        searchByTrainer(ats)
        printAthletes(athletes)
        bottomPanel(ats)
    elif choice == 5:
        subprocess.call([
        r"C:\Program Files\Notepad++\notepad++.exe", r"PythonRGRSport_athletes.csv",
        "-n1500"])
        printAthletes(athletes)
        bottomPanel(ats)

def editAthletes(ats):
    num = int(input('Введите номер легкоатлета: '))
    k = 0
    flag = False
    while k < len(ats) and flag != True:
        if ats[k][0] == num:
            flag = True
            break
        else: 
            k += 1
    if flag != True:
        print('Номер не был найден')
        k = 0
        editAthletes(ats)
    print('.' * 110)
    print('%3s'%(ats[k][0]),ats[k][1],ats[k][2],
              ats[k][3],'%3s'%sports_category.get(ats[k][4]),trainers[ats[k][5]][1], sep='\t  .  ')
    print('.' * 110)
    print('Измененить номер: [%i] -> '%(ats[k][0]), end='')
    ats[k][0] = int(input())
    print('Измененить фамилию: [%s] -> '%(ats[k][1]), end='')
    ats[k][1] = str(input())
    print('Измененить имя: [%s] -> '%(ats[k][2]), end='')
    ats[k][2] = str(input())
    print('Измененить год рождения: [%i] -> '%(ats[k][3]), end='')
    ats[k][3] = int(input())
    print('0 - Б/Р - без разряда\n1 - МС  - мастер спорта\n2 - КМС - кандидат в мастера спорта\n3 - I   - первый разряд\n'
        '4 - II  - второй разряд\n5 - III - третий разряд\n6 - 1юн - первый юношеский разряд\n7 - 2юн - второй юношеский разряд\n'
        '8 - 3юн - третий юношеский разряд')
    print('Изменить ', end='')
    while True:
       print('код разряда: [%i] -> '%(ats[k][4]), end='')
       ats[k][4]= int(input())
       if ats[k][4] < 9 and ats[k][4] > -1:
           break
       else:
           print("Повторите ", end='')
    n = 0
    while n < len(trainers):
        print('%2i'%(trainers[n][0]), '-', trainers[n][1])
        n += 1
    print('Изменить ', end='')
    while True:
       print('код тренера: [%i] -> '%(ats[k][4]), end='')
       ats[k][5]= int(input())
       if ats[k][5] < len(trainers) + 1 and ats[k][5] > -1:
           break
       else:
           print("Повторите ", end='')

def addAthletes(ats):
    ats.append([])
    print('Номер: ', end='')
    ats[-1].append(int(input()))
    print('Фамилия: ', end='')
    ats[-1].append(str(input()))
    print('Имя: ', end='')
    ats[-1].append(str(input()))
    print('Год рождения: ', end='')
    ats[-1].append(int(input()))
    print('0 - Б/Р - без разряда\n1 - МС  - мастер спорта\n2 - КМС - кандидат в мастера спорта\n3 - I   - первый разряд\n'
        '4 - II  - второй разряд\n5 - III - третий разряд\n6 - 1юн - первый юношеский разряд\n7 - 2юн - второй юношеский разряд\n'
        '8 - 3юн - третий юношеский разряд')
    while True:
       print('Код разряда: ', end='')
       ats[-1].append(int(input()))
       if ats[-1][4] < 9 and ats[-1][4] > -1:
           break
    n = 0
    while n < len(trainers):
        print('%2i'%(trainers[n][0]), '-', trainers[n][1])
        n += 1
    while True:
       print('Код тренера: ', end='')
       ats[-1].append(int(input()))
       if ats[-1][5] < len(trainers) + 1 and ats[-1][5] > -1:
           break

def deleteAthletes(ats):
    num = int(input('Введите номер легкоатлета: '))
    k = 0
    flag = False
    while k < len(ats) and flag != True:
        if ats[k][0] == num:
            flag = True
            break
        else: 
            k += 1
    if flag != True:
        print('Номер не был найден')
        k = 0
        deleteAthletes(ats)
    else:
        print('Подтвердите удаление (да/нет - 0)')
        choice = input()
        if choice != 0:
            ats.pop(k)
            print('Спортсмен был удален')
        else:
            print('Спортсмен не был удален')

def searchByTrainer(ats):
    n = 0
    while n < len(trainers):
        print('%2i'%(trainers[n][0]), '-', trainers[n][1])
        n += 1
    num = int(input('Введите код тренера: '))
    k = 0
    flag = False
    while k < len(trainers) and flag != True:
        if trainers[k][0] == num:
            flag = True
            break
        else: 
            k += 1
    if flag != True:
        print('Тренер не был найден')
        k = 0
        searchByTrainer(ats)
    print('.' * 110)
    print(trainers[k][0],trainers[k][1])
    print('.' * 110)
    k = 0
    while k < len(ats):
        if ats[k][5] == num:
            print('%3s'%(ats[k][0]),ats[k][1],ats[k][2],
                    ats[k][3],'%3s'%sports_category.get(ats[k][4]),trainers[ats[k][5]][1], sep='\t  .  ')
        else:
            pass
        k += 1
    print('.' * 110)
#---------------------------------------------------------------------------------------------------------------

print('Загрузка базы данных...')

#Загрузка тренеров
print('Загрузка тренеров...')
with open('files\PythonRGRSport_trainers.csv', "r", newline="", encoding="utf8") as file:
    reader = csv.reader(file)
    k = 0
    for row in reader:
        trainers_.append(row)
        trainers.append([])
        if visio:
            print(trainers_[k])
            time.sleep(0.05)
        k += 1
        #row_.clear()
file.close()
k = 0
while k < len(trainers_):
    trainers[k].append(int(trainers_[k][0]))                                        #код
    trainers[k].append(trainers_[k][1]+' '+trainers_[k][2]+' '+trainers_[k][3])     #фамилия имя
    k += 1
if visio:
    print('Всего тренеров: ', len(trainers))

#Загрузка легкоатлетов
print('Загрузка легкоатлетов...')
with open('files\PythonRGRSport_athletes.csv', "r", newline="", encoding="utf8") as file:
    reader = csv.reader(file)
    k = 0
    for row in reader:
        athletes_.append(row)
        athletes.append([])
        if visio:
            print(athletes_[k])
            time.sleep(0.05)
        k += 1
        #row_.clear()
file.close()
k = 0
while k < len(athletes_):
    athletes[k].append(int(athletes_[k][0]))                    #номер
    athletes[k].append(athletes_[k][1])                         #фамилия
    athletes[k].append(athletes_[k][2])                         #имя
    athletes[k].append(int(athletes_[k][3]))                    #год рождения
    athletes[k].append(int(athletes_[k][4]))                    #разряд
    athletes[k].append(int(athletes_[k][5]))                    #код тренера
    k += 1
if visio:
    print('Всего легкоатлетов: ', len(athletes))

#---------------------------------------------------------------------------------------------------------------

printAthletes(athletes)
bottomPanel(athletes)
