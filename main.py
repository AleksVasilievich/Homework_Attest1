import csv
import uuid
import pandas as pd
import fileinput
read_notes = ''

def menu():
    print("Программа - Заметки")
    print("Введите ___ 1 - создать ; 2 - сохранить ; 3 - читать ; 4 - читать по ID; 5 - редоктировать ; 6 - удалить ; 7 - выход")
    comand = input()

    if comand == '1':
        input_notes(), menu()
    elif comand == '2' and read_notes != '':
        save_notes(read_notes)
    elif comand == '3':
        read_notes()
    elif comand == '4' and read_notes != '':
        read_id_notes(), menu()
    elif comand == '5':
        edit_notes()
    # elif comand == '6':
    #     dell_notes()
    elif comand == '7':
        exit_notes()
    else:
        error_notes()
    return comand

# def create_notes(notes):
#     print(notes)
#
#     with open('data.csv', 'w', encoding='utf_8') as file:
#         file.write(notes)
#
#     print("Введите ___ 1 - создать ; 2 - сохранить ; 3 - читать ; 4 - редоктировать ; 5 - удалить ; 6 - выход")
#
#     return notes

def save_notes(notes):
    try:
        with open('data.csv', 'a', encoding='utf_8') as file:
            file.write(notes)
            print('Ваши данные успешно сохранены !!!')
    except Exception:
        print("Создайте чтобы сохранить !!!"), menu()

def read_notes():
    try:
        with open('data.csv', 'r', encoding='utf_8') as file:
            return print(file.read())
    except Exception:
        error_notes()
#
def read_id_notes():
    temp = input('Введите номер ID ->   ')
    try:
        arr = view_id()
        temp_id = arr.index(temp)
        array = list()
        array1 = list()
        with open('data.csv', 'r', encoding='utf_8') as file:
            array.append(file.read().split())
            for i in array:
                for j in i:
                    array1.append(j.split(';'))
        temp_array = int(temp_id)
            # print(array1)
        print(array1[temp_array])
    except Exception:
                    error_notes()

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

def input_notes():
    array2 = view_id()

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
    # print(array)
    array2 = array2[::4]
    print('Список id заметок: ')
    print(array2)
    return array2


if __name__ == '__main__':
    menu()
    # add_notes(input_notes())5

