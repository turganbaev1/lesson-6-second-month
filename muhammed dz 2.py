while 1:
    a = str(input(" введите слова: "))
    b = len(a)
    print(" количество букв: ", b)
    vowels = 'AаЕеЁёИиОоУуЫыЭэЮюЯяAaEeIiOoUu'
    consotans = 'БбВвГгДдЖжЗзЙйКкЛлМмНнПпРрСсТтФфХхЦцЧчШшЩщBbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZZ'
    count_v = 0
    count_c = 0
    for i in a:
        if i in vowels:
            count_v+=1
        elif i in consotans:
            count_c+=1
    print(f'Гласные {count_v}')
    print('Согласные ',count_c )
    print('Согласные/Гласные ', round(count_v*100/b,2),'% /' , round(count_c*100/b,2),'%')
    m = input( ' продолжить?: ')
    if m == 1:
        continue
    else:
        break








