calculation = list(input("Введите данные в следующем формате (арифметическое действие(+ - * /) число_1 число_2):").split())

def polish_notation(calculation):
    try:
        assert float(calculation[1]) >= 0 and float(calculation[2]) >= 0, "Введите положительное число"
        if calculation[0] == "+":
            print(float(calculation[1]) + float(calculation[2]))
        elif calculation[0] == "-":
            print(float(calculation[1]) - float(calculation[2]))
        elif calculation[0] == "*":
            print(float(calculation[1]) * float(calculation[2]))
        elif calculation[0] == "/":
            try:
                answer = 0
                answer = float(calculation[1]) / float(calculation[2])
                print(answer)
            except ZeroDivisionError:
                print("На ноль делить нельзя")
        else:
            print("Недоступное арифметическое действие")
    except IndexError:
        print("Не хватает данных")
        
polish_notation(calculation)