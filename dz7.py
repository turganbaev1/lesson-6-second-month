class In:
    while True:
        try:
            string = int(input("Введите число:"))
            if string > 999 or string < 100:
                raise ValueError
            break
        except ValueError:
            print('Вводить только 3значные целые числа!')

    if string < 0 or str(string) != str(string)[:: -1]:
        print("Непалидромное число")
    else:
        print("Палидромное число")
