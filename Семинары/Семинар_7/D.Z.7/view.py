import sys

def add_abonent():
    abonent_first_name = input("Введите Фамилию ")
    abonent_name = input("Введите Имя ")
    abonent_tel = input("Введите номер телефона ")
    abonent_data = (abonent_first_name, abonent_name, abonent_tel)
    return abonent_data



def start():
    print("Выберте действие: ", end="\n")
    print("1 - Экспорт контактов в формате csv ")
    print("2 - Экспорт контактов в формате txt")
    print("3 - Импорт контактов из файла txt")
    print("4 - Импорт контактов из файла csv")
    print("5 - добавить контакт")
    print("0 - Выход")
    select = input_num(">> ")
    return select


def input_num(text):
    while True:
        try:
            num = int(input(text))
            return num
        except:
            print("Введите число!")


def user_exit():
    print("Вернуться в меню? Y/N ")
    userIn = input(">> ")
    if userIn in list("YyНн"):
        return True
    else:
        sys.exit()