import csv

import pandas as pd
import fileinput
read_notes = ''

def menu():
    print("Программа - Заметки")
    print("Введите ___ 1 - создать ; 2 - сохранить ; 3 - читать ; 4 - редоктировать ; 5 - удалить ; 6 - выход")
    comand = input()

    if comand == '1':
        input_notes(), menu()
    elif comand == '2' and read_notes != '':
        save_notes(read_notes)
    elif comand == '3':
        read_notes()
    elif comand == '4':
        edit_notes()
    elif comand == '5':
        save_notes(input_notes())
    elif comand == '6':
        exit_notes()
    elif comand == '7':
        input()
    else:
        error_notes()

    return comand

def create_notes(notes):
    print(notes)

    with open('data.csv', 'w', encoding='utf_8') as file:
        file.write(notes)

    print("Введите ___ 1 - создать ; 2 - сохранить ; 3 - читать ; 4 - редоктировать ; 5 - удалить ; 6 - выход")

    return notes


def save_notes(notes):
    with open('data.csv', 'a', encoding='utf_8') as file:
        file.write(notes)

    return notes, print('Ваши данные успешно сохранены !!!')

def read_notes():
    with open('data.csv', 'r', encoding='utf_8') as file:
        return print(file.read())

def edit_notes():
    temp_id = int(input('Enter id note ->  '))
    array = list()
    array1 = list()
    with open('data.csv', 'r', encoding='utf_8') as file:
        array.append(file.read().split())
        for i in array:
            for j in i:
                array1.append(j.split(';'))

    temp_array = temp_id - 1
    return print(*array1[temp_array]), print('Эти данные будут изменены !!! Введите новые данные : ')
# def edit_notes():
#     df = pd.read_csv('data.csv')
#     df.loc[1, 'name'] = 'New text'
#     df.to_csv('data.csv')

# def edit_notes():
#     for file in fileinput.input():
#         print(file)
#     # with open('data.txt', 'w', encoding='utf_8') as file:
#     #     file_reader = csv.reader(file)
#     with open('data1.csv', newline='', encoding='utf_8') as file:
#         file_reader = csv.reader(file)
#         for i in file_reader:
#             print(', '.join(i))
#             break

def input_notes():
    id_n = input()
    head_n = input()
    body_n = input()
    date_n = input()
    notes = (id_n + ';' + head_n + ';' + body_n + ';' + date_n + '\n')
    global read_notes
    read_notes = notes
    return notes, print(read_notes), print('СОХРАНИТЬ ДАННЫЕ ???-- НАЖМИТЕ --  2 -- ИЛИ ДАННЫЕ БУДУТ ПОТЕРЯНЫ !!!')

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
