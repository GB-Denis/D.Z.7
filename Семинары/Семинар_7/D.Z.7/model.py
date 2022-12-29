import csv

default_phone_book = [["Юсупова", "Анна", 89234519323], ["Озеров", "Николай", 89102111263], ["Стрелков", "Игорь", 89580203005]]


def export_contact_cvs():
    with open("phone_book_csv", mode="w", encoding="utf-8") as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        for row in default_phone_book:
            file_writer.writerow(row)


def export_contact_txt():
    with open('phone_book_txt.txt', 'w', encoding="utf-8") as data:
        for i in default_phone_book:
            for j in i:
                data.write(str(j))
                data.write('\n')
            data.write('\n')


def import_contact_from_txt():
    with open('phone_book_txt.txt', 'r', encoding="utf-8") as data:
        for line in data:
            print(line)


def import_contact_from_cvs():
    export_csv_list = []
    with open("phone_book_csv", encoding="utf-8") as r_file:
        reader_object = csv.reader(r_file, delimiter=';')
        for row in reader_object:
            export_csv_list.append(row)
            print(row)


def insert_abonent(abonent_first_name, abonent_name, abonent_tel):
    with open("phone_book_csv", mode="a", encoding="utf-8") as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        file_writer.writerow([abonent_first_name, abonent_name, int(abonent_tel)])