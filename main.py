import csv
import uuid
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
    elif comand == '3' and read_notes != '':
        read_notes(), menu()
    elif comand == '4':
        edit_notes()
    elif comand == '5':
        view_id()
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
    try:
        with open('data.csv', 'a', encoding='utf_8') as file:
            file.write(notes)
            print('Ваши данные успешно сохранены !!!')
    except Exception:
        print("Создайте чтобы сохранить !!!"), menu()

def read_notes():
    menu_id = input('Весь список нажмите - 1 ; Заметка по id нажмите - 2  ')
    if menu_id == '1':
        with open('data.csv', 'r', encoding='utf_8') as file:
            return print(file.read())
    elif menu_id == '2':
        temp_id = int(input('Введите номер ID ->   '))
        try:
            array = list()
            array1 = list()
            with open('data.csv', 'r', encoding='utf_8') as file:
                array.append(file.read().split())
                for i in array:
                    for j in i:
                        array1.append(j.split(';'))
            temp_array = int(temp_id) - 1
            print(array1)
            print(array1[temp_array])
        except Exception:
                        error_notes()
    else:
        read_notes()
def edit_notes():
    try:
        temp_id = int(input('Enter id note ->  '))
        array = list()
        array1 = list()
        with open('data.csv', 'r', encoding='utf_8') as file:
            array.append(file.read().split())
            for i in array:
                for j in i:
                    array1.append(j.split(';'))

        temp_array = temp_id - 1
        return print(*array1[temp_array]), print('Эти данные будут изменены !!! Введите новые данные : '), array1
    except Exception:
        error_notes()
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
    array2 = list()
    array = list()
    array1 = list()
    with open('data.csv', 'r', encoding='utf_8') as file:
        array.append(file.read().split())
        for i in array:
            for j in i:
                array1.append(j.split(';'))
    # edit_notes()
    for i in array1:
        for j in i:
            array2.append(j)
    array2 = array2[::4]
    print('Список id заметок: ')
    print(array2)
    # print('Введите новый id ')

    id_n = input('Введите новый id ->  ')
    for i in array2:
        while i == id_n:
            print('id уже существует !!!')
            id_n = input('Введите новый id ->  ')

    head_n = input('Введите заголовок ->  ')
    body_n = input('Введите текст заметки ->  ')
    date_n = input('Введите дату ->  ')
    notes = (id_n + ';' + head_n + ';' + body_n + ';' + date_n + '\n')
    global read_notes
    read_notes = notes
    return notes, print(read_notes), print('СОХРАНИТЬ ДАННЫЕ ???-- НАЖМИТЕ --  2 -- ИЛИ ДАННЫЕ БУДУТ ПОТЕРЯНЫ !!!')

def error_notes():
    return print('No Comand !')

def exit_notes():
    return print('Goodbye !')

def view_id():
    array2 = list()
    array = list()
    array1 = list()
    with open('data.csv', 'r', encoding='utf_8') as file:
        array.append(file.read().split())
        for i in array:
            for j in i:
                array1.append(j.split(';'))
    for i in array1:
        for j in i:
            array2.append(j)
    print(array2)
    array2 = array2[::4]
    print('Список id заметок: ')
    return print(array2)


if __name__ == '__main__':
    menu()
    # add_notes(input_notes())
