def menu():
    print("Программа - Заметки")
    print("Введите ___ 1 - создать ; 2 - сохранить ; 3 - читать ; 4 - редоктировать ; 5 - удалить ; 6 - выход")
    comand = input()

    if comand == '1':
        create_notes(input_notes())
    elif comand == '2':
        save_notes(input_notes())
    elif comand == '3':
        save_notes(input_notes())
    elif comand == '4':
        save_notes(input_notes())
    elif comand == '5':
        save_notes(input_notes())
    elif comand == '6':
        exit_notes()
    else:
        error_notes()

    return comand
def create_notes(notes):
    with open('data.txt', 'w', encoding='utf_8') as file:
        file.write(notes)

    return notes,  print(notes), menu()
def save_notes(notes):
    with open('data.txt', 'a', encoding='utf_8') as file:
        file.write(notes)

    return notes


def input_notes():
    id_n = input()
    head_n = input()
    body_n = input()
    date_n = input()
    notes = (id_n + ';' + head_n + ';' + body_n  + ';' + date_n + '\n')
    return notes


def error_notes():
    return print('No Comand !')

def exit_notes():
    return print('Goodbye')


def view():
    print()
    # print(input_notes())


if __name__ == '__main__':
    menu()
    # add_notes(input_notes())


