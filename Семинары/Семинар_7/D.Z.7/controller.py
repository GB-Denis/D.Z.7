import sys
import view
import model
import xml_generator


def main():
    select = view.start()
    if select == 1:
        model.export_contact_cvs()

    elif select == 2:
       model.export_contact_txt()

    elif select == 3:
       model.import_contact_from_txt()

    elif select == 4:
        model.import_contact_from_cvs()

    elif select == 5:
        temp = view.add_abonent()
        abonent_first_name, abonent_name, abonent_tel = temp[0], temp[1], temp[2]
        model.insert_abonent(abonent_first_name, abonent_name, abonent_tel)
        answer = input("Хотите добавить запись в xml файл? Если да, нажмите 1 ")
        if answer == '1':
            xml_generator.create(abonent_first_name, abonent_name, abonent_tel)

    elif select == 0:
        sys.exit()