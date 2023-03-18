def menu():
    print("Программа - Заметки")
    print("Введите ___ 1 - создать ; 2 - сохранить ; 3 - читать ; 4 - редоктировать ; 5 - удалить")
    comand = int(input())
    return comand
def add_notes(notes):
    with open('data.txt', 'w', encoding='utf_8') as file:
        file.write(notes)

    return notes

def input_notes():
    id_n = input()
    head_n = input()
    body_n = input()
    date_n = input()
    notes = id_n + ';' + head_n + ';' + body_n  + ';' + date_n
    return notes


def view():
    print(input_notes())


if __name__ == '__main__':
    menu()
    add_notes(input_notes())


