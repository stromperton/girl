import random

print("Тян V 1.0.5")
print("Для просмотра команд введите 0")

interes = 0
tyn = 0
money = 10000
year = 2015
mounth = 6
day = 0
allday = 0
tallday = 0
zarp = 10000
rab = 'Расклейщик'

coltyn = 0

dayh = -7
dayf = -7
dayp = -7
dayk = -7
dayf = 0

rhobb = 0
rflow = 0
rpresent = 0
rhate = 0
rkino = 0
rdatavstrd = 0
rdatavstrm = 0

tt = 0
tt2 = 0
tt3 = 0
tt4 = 0
tt5 = 0
tt6 = 0

gg = 0

pov = 0

hobb = '?неизвестно?'
flow = '?неизвестно?'
present = '?неизвестно?'
hate = '?неизвестно?'
kino = '?неизвестно?'
datavstr = '?неизвестно?'

while True:
    day = day+1
    allday = allday+1
    tallday = tallday+1
    dayf = dayf+1
    money = money-random.randint(250, 350)
    
    if coltyn > 4:
        print("Так часто тян менять нельзя")
        break 
   
    if money <= 0:
        print("Вы бомж, игра окончена")
        break
    
    if interes <= 0:
        tyn = 0
        interes = 0
        print("Она вас бросает, увы!")
    if interes > 100:
        interes = 100
    rs = random.randint(1, 100)
    if tyn == 1:
        if rs < 9:
            rss = random.randint(1, 100)
            if rss < 20:
                print("Вам предложила секс другая тян\nЕсли вы согласитесь, она заплатит 18000\nНо ваша тян может узнать об этом")
                print("1 Согласиться")
                print("2 Отказаться")
                vs = input()
                if vs == '1':
                    money = money+18000
                    rt = random.randint(1, 3)
                    if rt == '1':
                        print("Вы согласились, девушка ничего не узнала")
                    else:
                        print("Вы согласились, но девушка все узнала")
                        tyn = 0
                else:
                    print("Вы отказались")
            input('Введите Enter')
    if rdatavstrd == (day-1):
        if rdatavstrm == mounth:
            if rdatavstry < year:
                if gg == 0:
                    print("Вы забыли поздравить ее с годовщиной\nвстречи")
                    interes = interes-23
                    input('Введите Enter')
    
    if day > 30:
        mounth = mounth+1
        money = money+zarp
        day = 1
    if mounth > 12:
        year = year+1
        mounth = 1
    if day == 0:
        mounth = mounth-1
        day = 30
    if mounth == 0:
        year = year-1
        mounth = 12
    if dayf >= 60:
        rflow = random.randint(1, 10)
        flow = '?неизвестно?'
        dayf = 0
    print("\nЗаинтересованность:", round(interes), "%")
    print("Деньги:", money, "руб.")
    
    if mounth < 10:
        if day < 10:
            print("Дата: 0"+str(day)+".0"+str(mounth)+"."+str(year))
        
    if mounth >= 10:
        if day < 10:
            print( "Дата: 0"+str(day)+"."+str(mounth)+"."+str(year))
        
    if mounth < 10:
        if day >= 10:
            print( "Дата: "+str(day)+".0"+str(mounth)+"."+str(year))
        
    if mounth >= 10:
        if day >= 10:
            print( "Дата: "+str(day)+"."+str(mounth)+"."+str(year))
        
        
    if tyn == 0:
        print("Пока у вас нету тян.")
        if tallday > 90:
            print("Жизнь боль когда нету тян")
            print("Вы покончили жизнь самоубийством")
            break
        
    if tyn == 1:
        print("У вас есть тян")
        print("Она увлекается", hobb)
        print("Из цветов она предпочитает", flow)
        print("В подарок она хочет", present)
        print("Она ненавидит", hate)
        print("Она хочет сходить на", kino)
        print("Дата встречи:", datavstr)
        interes = interes-0.2
        tallday = 0
        
        
    cmd = input()
    
    if cmd == '&%@#$':
        interes = interes + 30
    if cmd == '#@&%$':
        money = money+10000
 
    if cmd == '0':
        day = day-1
        allday = allday-1
        print("1 Искать тян")
        print("2 Заняться ее любимым делом")
        print("3 Подарить цветы")
        print("4 Подарить подарок")
        print("5 Сходить в кино")
        print("6 Поздравить с годовщиной встечи")
        print("7 Поговорить с тян")
        print("8 Предложить секс")
        print("9 Информация о работе")
        input("Введите Enter")
        
    if cmd == '1':
        coltyn = coltyn+1
        rname = random.randint(1, 16)
        rpresent = random.randint(1, 10)
        tyn = 1
        if rname == 1:
            name = 'Настя'
        if rname == 2:
            name = 'Маша'
        if rname == 3:
            name = 'Кристина'
        if rname == 4:
            name = 'Карина'
        if rname == 5:
            name = 'Света'
        if rname == 6:
            name = 'Катя'
        if rname == 7:
            name = 'Саша'
        if rname == 8:
            name = 'Женя'
        if rname == 9:
            name = 'Ева'
        if rname == 10:
            name = 'Лена'
        if rname == 11:
            name = 'Рита'
        if rname == 12:
            name = 'Даша'
        if rname == 13:
            name = 'Ира'
        if rname == 14:
            name = 'Лера'
        if rname == 15:
            name = 'Оля'
        if rname == 16:
            name = 'Алена'
            
        interes = 10
        rhobb = random.randint(1, 10)
        if rhobb > 8:
            rhobb = 8
        rflow = random.randint(1, 10)
        rpresent = random.randint(1, 10)
        rhate = random.randint(1, 8)
        rkino = random.randint(1, 10)
        rdatavstrd = day
        rdatavstrm = mounth
        rdatavstry = year
        
        hobb = '?неизвестно?'
        flow = '?неизвестно?'
        present = '?неизвестно?'
        hate = '?неизвестно?'
        kino = '?неизвестно?'
        datavstr = '?неизвестно?'

        if rhobb == rhate:
            rhate = 0
            hate = 'ничего'
        if mounth < 10:
            if day < 10:
                datavstr = "0"+str(day)+".0"+str(mounth)+"."+str(year)
        
        if mounth >= 10:
            if day < 10:
                datavstr = "0"+str(day)+"."+str(mounth)+"."+str(year)
        
        if mounth < 10:
            if day >= 10:
                datavstr = str(day)+".0"+str(mounth)+"."+str(year)
        
        if mounth >= 10:
            if day >= 10:
                datavstr = str(day)+"."+str(mounth)+"."+str(year)
       
        print("Вы нашли девушку по имени", name)
        input("Введите Enter")
        
    if cmd == '2':
        razh = allday-dayh
        if razh >= 7:
            print("1 Кататься на роликах")
            print("2 Кататься на велосипеде")
            print("3 Рисовать")
            print("4 Программировать")
            print("5 Играть в ностольные игры")
            print("6 Играть в Пинг-Понг")
            print("7 Играть в воллейбол")
            print("8 Ходить по магазинам |7000р.")
            
            vh = input()
            if vh == str(rhobb):
                print("Вы угадали, это ее любимое занятие")
                if rhobb == '1':
                    hobb = 'катанием на роликах'
                if rhobb == '2':
                    hobb = 'катанием на велосипеде'
                if rhobb == '3':
                    hobb = 'рисованием'
                if rhobb == '4':
                    hobb = 'программированием'
                if rhobb == '5':
                    hobb = 'настольными играми'
                if rhobb == '6':
                    hobb = 'Пинг-Понгом'
                if rhobb == '7':
                    hobb = 'воллейболом'
                if rhobb == '8':
                    hobb = 'шопингом'
                interes = interes+5
                dayh = allday
                if vh == '8':
                    money = money-7000
            elif vh == str(rhate):
                print("Как вы могли? Она это ненавидит!")
                interes = interes-30
                if rhate == 1:
                    hate = 'катание на роликах'
                if rhate == 2:
                    hate = 'катание на велосипеде'
                if rhate == 3:
                    hate = 'рисование'
                if rhate == 4:
                    hate = 'программирование'
                if rhate == 5:
                    hate = 'настольные игры'
                if rhate == 6:
                    hate = 'Пинг-Понг'
                if rhate == 7:
                    hate = 'воллейбол'
                if rhate == 8:
                    hate = 'шопинг'
            else:
                print("Ей скучно, вы не угадали")
                interes = interes-5
        else:
            print("Заниматься хобби можно лишь раз в неделю")
        input("Введите Enter")   
            
           
    if cmd == '3':
        print("1 Розы |7000 р.")
        print("2 Хризантемы |4000 р.")
        print("3 Ромашки |1000 р.")
        print("4 Тюльпаны |5500 р.")
        print("5 Архидеи |6000 р.")
        print("6 Фиалки |2000 р.")
        print("7 Пионы |3500 р.")
        print("8 Сирень |1500 р.")
        print("9 Нарцисы |4500 р.")
        print("10 Астры |5000 р.")
            
        vf = input()
        if vf == '1':
            money = money-7000
        if vf == '2':
            money = money-4000 
        if vf == '3':
            money = money-1000
        if vf == '4':
            money = money-5500  
        if vf == '5':
            money = money-6000
        if vf == '6':
            money = money-2000
        if vf == '7':
            money = money-3500
        if vf == '8':
            money = money-1500
        if vf == '9':
            money = money-4500
        if vf == '10':
            money = money-5000
       
        if vf == str(rflow):
            print("Вы угадали, это ее любимые цветы")
            if rflow == 1:
                flow = 'розы'
            if rflow == 2:
                flow = 'хризантемы'
            if rflow == 3:
                flow = 'ромашки'
            if rflow == 4:
                flow = 'тюльпаны'
            if rflow == 5:
                flow = 'архидеи'
            if rflow == 6:
                flow = 'фиалки'
            if rflow == 7:
                flow = 'пионы'
            if rflow == 8:
                flow = 'сирень'
            if rflow == 9:
                flow = 'нарцисы'
            if rflow == 10:
                flow = 'астры'
            interes = interes+5
        else:
            print("Это не ее любимые цветы, вы не угадали")
        input("Введите Enter")   
            
    if cmd == '4':
        print("1 IPhone |44000 р.")
        print("2 Большой Плюшевый мишка |5000 р.")
        print("3 Платье |9000 р.")
        print("4 Шуба |50500 р.")
        print("5 Духи |6000 р.")
        print("6 Золотое кольцо |14000 р.")
        print("7 Золотые серьги |7500 р.")
        print("8 Коробка конфет |4700 р.")
        print("9 Наручные часы |5500 р.")
        print("10 Наушники Beats |12000 р.")
        vp = input()
        if vp == '1':
            money = money-44000
        if vp == '2':
            money = money-5000 
        if vp == '3':
            money = money-9000
        if vp == '4':
            money = money-50500  
        if vp == '5':
            money = money-6000
        if vp == '6':
            money = money-14000
        if vp == '7':
            money = money-7500
        if vp == '8':
            money = money-4700
        if vp == '9':
            money = money-5500
        if vp == '10':
            money = money-12000
       
        if vp == str(rpresent):
            rpresent = random.randint(1, 10)
            interes = interes+7
            print("Это именно то, что она хотела!")
            present = '?неизвестно?'
        else:
            print("Ваш подарок ей не понравился")
            interes = interes-2
        input('Введите Enter')

    if cmd == '5':
        print("1 Форсаж 7 |500 р.")
        print("2 Миньоны |470 р.")
        print("3 Терминатор 5 |580 р.")
        print("4 Кунг-Фу Панда 3 |440 р.")
        print("5 Аватар 2 |580 р.")
        print("6 Звездные войны VII |600 р.")
        print("7 Три Богатыря 5 |300 р.")
        print("8 Третий Лишний 2 |380 р.")
        print("9 Мстители |400 р.")
        print("10 Головоломка |400 р.")
        vk = input()
        if vk == '1':
            money = money-500
        if vk == '2':
            money = money-470
        if vk == '3':
            money = money-580
        if vk == '4':
            money = money-440
        if vk == '5':
            money = money-580
        if vk == '6':
            money = money-600
        if vk == '7':
            money = money-300
        if vk == '8':
            money = money-380
        if vk == '9':
            money = money-400
        if vk == '10':
            money = money-400
       
        if vk == str(rkino):
            print("Ей понравилось, вас повезло!")
            interes = interes+5
            rkino = random.randint(1, 10)
            kino = '?неизвестно?'
        else:
            print("Ей скучно, ей не понравилось")
            interes = interes-4
        input('Введите Enter')
 
    if cmd == '6':
        if rdatavstrd == day:
            if rdatavstrm == mounth:
                gg = 1
                print("Она очень рада вашему поздравлению")
                interes = interes+30
            else:
                print("Она очень расстроена!\nКак можно забыть дату встречи?")
                interes = interes-20
        else:
            print("Она очень расстроена!\nКак можно забыть дату встречи?")
            interes = interes-20
        input('Введите Enter')

    if cmd == '7':
        rr = random.randint(1, 100)
        if rr < 21:
            print("Во время разговора началась ссора.\nЗаговорившись, вы случайно перепутали ее имя.\nВам срочно нужно вспомнить ее имя.\nИначе она окончательно обидется")
            print("Как зовут вашу тян?")
            rn = random.randint(1, 5)
            if rn == 1:
                name1 = name
                name2 = 'Лена'
                name3 = 'Карина'
                name4 = 'Рита'
                name5 = 'Маша'
                if name == name2:
                    name2 = 'Света'
                if name == name3:
                    name3 = 'Света'
                if name == name4:
                    name4 = 'Света'
                if name == name5:
                    name5 = 'Света'
            if rn == 2:
                name1 = 'Света'
                name2 = name
                name3 = 'Оля'
                name4 = 'Кристина'
                name5 = 'Лена'
                if name == name1:
                    name1 = 'Даша'
                if name == name3:
                    name3 = 'Даша'
                if name == name4:
                    name4 = 'Даша'
                if name == name5:
                    name5 = 'Даша'
            if rn == 3:
                name1 = 'Карина'
                name2 = 'Света'
                name3 = name
                name4 = 'Даша'
                name5 = 'Маша'
                if name == name1:
                    name1 = 'Кристина'
                if name == name2:
                    name2 = 'Кристина'
                if name == name4:
                    name4 = 'Кристина'
                if name == name5:
                    name5 = 'Кристина'
            if rn == 4:
                name1 = 'Рита'
                name2 = 'Даша'
                name3 = 'Оля'
                name4 = name
                name5 = 'Ира'
                if name == name1:
                    name1 = 'Карина'
                if name == name2:
                    name2 = 'Карина'
                if name == name3:
                    name3 = 'Карина'
                if name == name5:
                    name5 = 'Карина'
            if rn == 5:
                name1 = 'Ира'
                name2 = 'Кристина'
                name3 = 'Карина'
                name4 = 'Маша'
                name5 = name
                if name == name1:
                    name1 = 'Даша'
                if name == name2:
                    name2 = 'Даша'
                if name == name3:
                    name3 = 'Даша'
                if name == name4:
                    name4 = 'Даша'
            
            print("1", name1)
            print("2", name2)
            print("3", name3)
            print("4", name4)
            print("5", name5)
            vn = int(input())
            if vn == rn:
                print("Вы ответили правильно")
            else:
                print("Вы ответили неверно, увы")
                interes = interes-34
            input('Введите Enter')
        if rr > 20:
            rrr = random.randint(1, 100)
            if rrr <= 10:
                print("Из разговора вы узнали\nчего она хочет в подарок.")
                if rpresent == 1:
                    present = 'IPhone'
                if rpresent == 2:
                    present = 'большого плюшевого мишку'
                if rpresent == 3:
                    present = 'платье'
                if rpresent == 4:
                    present = 'шубу'
                if rpresent == 5:
                    present = 'духи'
                if rpresent == 6:
                    present = 'золотое кольцо'
                if rpresent == 7:
                    present = 'золотые серьги'
                if rpresent == 8:
                    present = 'коробку конфет'
                if rpresent == 9:
                    present = 'наручные часы'
                if rpresent == 10:
                    present = 'наушники Beats'
                    
            if 10 < rrr <= 15:
                print("Из разговора вы узнали\nна что она хочет пойти в кино.")
                if rkino == 1:
                    kino = 'Форсаж 7'
                if rkino == 2:
                    kino = 'Миньоны'
                if rkino == 3:
                    kino = 'Терминатор 5'
                if rkino == 4:
                    kino = 'Кунг-Фу Панда 3'
                if rkino == 5:
                    kino = 'Аватар 2'
                if rkino == 6:
                    kino = 'Звездные Войны VII'
                if rkino == 7:
                    kino = 'Три Богатыря 5'
                if rkino == 8:
                    kino = 'Третий лишний 2'
                if rkino == 9:
                    kino = 'Мстители'
                if rkino == 10:
                    kino = 'Головоломка'

            if 15 < rrr <=20 :
                print("Разговор понравился ей")
                interes = interes+3
            if 20 < rrr <=50:
                print("Во время разговора она попросила 5000 р.")
                print("1 Отдать")
                print("2 Не давать")
                vm = input()
                if vm == '1':
                    money = money-5000
                    interes = interes+2
                    print("Теперь она довольна")
                else:
                    interes = interes-5
                    print("Она немного обиделась")
            if 50 < rrr <=57:
                interes = interes-3
                print("Разговор ей не понравился")
            if 57 < rrr <= 60:
                print("Разговор перешел в ласки с поцелуями")
                interes = interes+5
            if 60 < rrr <=62:
                print("Из разговора вы узнали, что она хочет на море.")
                print("1 Поехать |9550 р.")
                print("2 Не ехать")
                vm = input()
                if vm == '1':
                    print("Вы поехали на море")
                    money = money-9550
                    interes = interes+7
                else:
                    print("Вы никуда не поехали")
                    interes = interes-3
            if 62 < rrr <= 65:
                print("Во время разговора тян стало плохо")
                print("1 Сходить за лекарствами |1020 р.")
                print("2 Не ходить никуда")
                vl = input()
                if vl == '1':
                    print("Вы сходили за лекарствами")
                    money = money-1020
                    interes = interes+2
                else:
                    print("Вы никуда не пошли")
                    interes = interes-3
           
            if 65 < rrr <= 70:
                print("Загадка")
            if 70 < rrr <= 100:
                print("Вы решили играть в кости")
                rvp = random.randint(1, 12)
                rvd = random.randint(1, 12)
                print("У вас выпало", rvp)
                print("У нее выпало", rvd)
                if rvp > rvd:
                    print("Вы победили, тян расстроена")
                    interes = interes-3
                if rvp < rvd:
                    print("Вы проиграли, тян рада")
                    interes = interes+3
                if rvd == rvp:
                    print("Ничья")
            input('Введите Enter')
            
    if cmd == '8':
        if interes > 99:
            print("Она согласилась на секс! Вы победили!")
            print("")
            print("     //''''\\\      ")
            print("    //|•  •|\\\     ")
            print("   // \ [] / \\\    ")
            print("      _ | | _       ")
            print("    / /     \ \     ")
            print("   /（。 ㅅ 。）\    ")
            print("  / / |     | \ \   ")
            print("   /  |     |  \ \  ")
            print("      |  '  |       ")
            print("     /  {|}  \      ")
            print("    /  /| |\  \     ")
            print("   /  / | | \  \    ")
            print("______(*) (*)_______")
            
        else:
            print("Какая наглость! Как вы могли?\nОна вас бросает!")
            tyn = 0   
            interes = 0
        input('Введите Enter') 	
    
    if (cmd == '9') and (tyn == 1):
        print("\nВаша зарплата:", zarp, "руб.")
        print("Вы работаете:", rab)          
        print("1 Попросить повышения")
        print("2 Сменить работу") 
        vrr = input()
        if vrr == '1':
            proc = random.randint(30, 50)
            print("Вероятность повышения:", proc, " %")
            print("1 Повысить вероятность 1% - 500 р.")
            print("2 Попросить повышения")
            vvr = input()
            prr = random.randint(1, 100)
            if vvr == '1':
                if pov < 3:
                    print("Введите кол-во %")
                    plproc = int(input())
                    if money >= (plproc*500):
                        proc = proc+plproc
                        money = money-plproc*500
                        if prr < proc:
                            print("Вас повысили")
                            zarp = zarp+5000
                            pov = pov+1
                        else:
                            print("Вы не прошли, вас уволили")
                            zarp = 0
                            rab = 'Нет работы'
                    else:
                        print("Не хватает денег")
                    
                        if prr < proc:
                            print("Вас повысили")
                            zarp = zarp+5000
                        else:
                            print("Вы не прошли, вас уволили")
                            zarp = 0
                            rab = 'нет работы'
            else:
                if pov < 3:
                    if prr < proc:
                            print("Вас повысили")
                            zarp = zarp+5000
                    else:
                        print("Вы не прошли, вас уволили")
                        zarp = 0
                        rab = 'нет работы'
          
        if vrr == '2':
            print("1 Расклейщик |10000 р.")
            print("2 Программист |45000 р.")
            print("3 Проектировщик |30000 р.")
            print("4 Авто Механик |24000 р.")
            print("5 Менеджер |40000 р.")
            print("6 Кассир |23000 р.")
            vrab = input()
            if vrab == '1':
                rab = 'Расклейщик'
                zarp = 10000
            if vrab == '2':
                if tt == 0:
                    proc = random.randint(1, 10)
                    print("Вероятность принятия:", proc, " %")
                    print("1 Повысить вероятность 1% - 2000 р.")
                    print("2 Устроится на работу")
                    vvr = input()
                    prr = random.randint(1, 100)
                    if vvr == '1':
                        print("Введите кол-во %")
                        plproc = int(input())
                        if money >= (plproc*2000):
                            proc = proc+plproc
                            money = money-plproc*2000
                            if prr < proc:
                                print("Вас приняли")
                                zarp = 45000
                                rab = 'Программист'
                            else:
                                print("Вас не взяли")
                                tt = 1
                        else:
                            print("Не хватает денег")
                            
                            if prr < proc:
                                print("Вас приняли")
                                zarp = 45000
                            else:
                                print("Вас не приняли")
                                tt = 1
                    
                    else:
                        if prr < proc:
                            print("Вас приняли")
                            zarp = 45000
                            rab = 'Программист'
                        else:
                            print("Вас не взяли")
                            tt = 1
                else:
                    print("Вы уже пробовали")                         
            if vrab == '3':
                if tt2 == 0:
                    proc = random.randint(1, 30)
                    print("Вероятность принятия:", proc, " %")
                    print("1 Повысить вероятность 1% - 1000 р.")
                    print("2 Устроится на работу")
                    vvr = input()
                    prr = random.randint(1, 100)
                    if vvr == '1':
                        print("Введите кол-во %")
                        plproc = int(input())
                        if money >= (plproc*1000):
                            proc = proc+plproc
                            money = money-plproc*1000
                            if prr < proc:
                                print("Вас приняли")
                                zarp = 30000
                                rab = 'Проектировщик'
                            else:
                                print("Вас не взяли")
                                tt2 = 1
                        else:
                            print("Не хватает денег")
                            
                            if prr < proc:
                                print("Вас приняли")
                                zarp = 30000
                                rab = "Проектировщик"
                            else:
                                print("Вас не приняли")
                                tt2 = 1
                    
                    
                    else:
                        if prr < proc:
                            print("Вас приняли")
                            zarp = 30000
                            rab = 'Проектировщик'
                        else:
                            print("Вас не взяли")
                            tt2 = 1
                else:
                    print("Вы уже пробовали")
            
            if vrab == '4':
                if tt3 == 0:
                    proc = random.randint(1, 30)
                    print("Вероятность принятия:", proc, " %")
                    print("1 Повысить вероятность 1% - 800 р.")
                    print("2 Устроится на работу")
                    vvr = input()
                    prr = random.randint(1, 100)
                    if vvr == '1':
                        print("Введите кол-во %")
                        plproc = int(input())
                        if money >= (plproc*800):
                            proc = proc+plproc
                            money = money-plproc*800
                            if prr < proc:
                                print("Вас приняли")
                                zarp = 24000
                                rab = 'Авто Механик'
                            else:
                                print("Вас не взяли")
                                tt3 = 1
                        else:
                            print("Не хватает денег")
                            
                            if prr < proc:
                                print("Вас приняли")
                                zarp = 24000
                                rab = "Авто Механик"
                            else:
                                print("Вас не приняли")
                                tt3 = 1
                    
                    
                    else:
                        if prr < proc:
                            print("Вас приняли")
                            zarp = 24000
                            rab = 'Авто Механик'
                        else:
                            print("Вас не взяли")
                            tt3 = 1
                else:
                    print("Вы уже пробовали")

            if vrab == '5':
                if tt4 == 0:
                    proc = random.randint(1, 10)
                    print("Вероятность принятия:", proc, " %")
                    print("1 Повысить вероятность 1% - 2000 р.")
                    print("2 Устроится на работу")
                    vvr = input()
                    prr = random.randint(1, 100)
                    if vvr == '1':
                        print("Введите кол-во %")
                        plproc = int(input())
                        if money >= (plproc*2000):
                            proc = proc+plproc
                            money = money-plproc*2000
                            if prr < proc:
                                print("Вас приняли")
                                zarp = 40000
                                rab = 'Менеджер'
                            else:
                                print("Вас не взяли")
                                tt4 = 1
                        else:
                            print("Не хватает денег")
                            
                            if prr < proc:
                                print("Вас приняли")
                                zarp = 40000
                                rab = "Менеджер"
                            else:
                                print("Вас не приняли")
                                tt4 = 1
                    
                    
                    else:
                        if prr < proc:
                            print("Вас приняли")
                            zarp = 40000
                            rab = 'Менеджер'
                        else:
                            print("Вас не взяли")
                            tt4 = 1
                else:
                    print("Вы уже пробовали")

            if vrab == '6':
                if tt5 == 0:
                    proc = random.randint(1, 30)
                    print("Вероятность принятия:", proc, " %")
                    print("1 Повысить вероятность 1% - 1100 р.")
                    print("2 Устроится на работу")
                    vvr = input()
                    prr = random.randint(1, 100)
                    if vvr == '1':
                        print("Введите кол-во %")
                        plproc = int(input())
                        if money >= (plproc*1100):
                            proc = proc+plproc
                            money = money-plproc*1000
                            if prr < proc:
                                print("Вас приняли")
                                zarp = 23000
                                rab = 'Кассир'
                            else:
                                print("Вас не взяли")
                                tt5 = 1
                        else:
                            print("Не хватает денег")
                            
                            if prr < proc:
                                print("Вас приняли")
                                zarp = 23000
                                rab = "Кассир"
                            else:
                                print("Вас не приняли")
                                tt5 = 1
                    
                    
                    else:
                        if prr < proc:
                            print("Вас приняли")
                            zarp = 23000
                            rab = 'Кассир'
                        else:
                            print("Вас не взяли")
                            tt5 = 1
                else:
                    print("Вы уже пробовали")
        input('Введите Enter')





