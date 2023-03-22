import csv
import uuid
import pandas as pd
import fileinput
from csv import writer
read_notes = ''

def menu():
    print("Программа - Заметки")
    print("Введите ___ 1 - создать ; 2 - сохранить ; 3 - читать ; 4 - читать по ID; 5 - редоктировать ; 6 - удалить ; 7 - выход")
    comand = input()

    try:
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
        elif comand == '6':
            delete_notes()
        elif comand == '7':
            exit_notes()
        elif comand == '8':
            view_id()
        else:
            error_notes()
        return comand
    except Exception:
        error_notes()


def save_notes(notes):
    try:
        with open('data.csv', 'a', encoding='utf_8') as file:
            file.write(notes)
            print('Ваши данные успешно сохранены !!!'),
    except Exception:
        print("Создайте чтобы сохранить !!!"), menu()

def read_notes():
    try:
        with open('data.csv', 'r', encoding='utf_8') as file:
            return print(file.read())
    except Exception:
        error_notes()


def read_id_notes():
    try:
        temp = input('Введите номер ID ->   ')
        arr = view_id()
        temp_id = arr.index(temp)
        temp_array = int(temp_id)
        array = list()
        array1 = list()
        with open('data.csv', 'r', encoding='utf_8') as file:
            array.append(file.read().split())
            for i in array[0]:
                array1.append(i)
        print(*array1[temp_array])
        # array1[temp_array].clear()
        # print(array1)
        return array1[temp_array]
    except Exception:
                    error_notes()

def edit_notes():
    read_id_notes()
    print('Эти данные будут изменены !!! Введите новые данные : ')

# def delete_notes():
#     # read_id_notes()
#     del_id = read_id_notes()
#     print('Эти данные будут УДАЛЕНЫ !!! ')
#     comand = input('Подтвердить нажмите -> 1 ')
    # if comand == '1':

        # with open('data.csv', 'rb', encoding='utf_8') as inp, open('data.csv', 'wb', encoding='utf_8' ) as out:
        #     writer = csv.writer(out)
        #     for row in csv.reader(inp):
        #         if row[0] != del_id:
        #             writer.writerow(row)


def owerwriting():
    pass
def input_notes():
    array2 = view_id()
    try:

        id_int = abs(int(input('Введите натуральное число, новый id ->  ')))
        for i in array2:
            while i == str(id_int):
                print('id уже существует !!!')
                id_int = abs(int(input('Введите натуральное число, новый id ->  ')))
        id_str = str(id_int)
        head_n = input('Введите заголовок ->  ')
        body_n = input('Введите текст заметки ->  ')
        date_n = input('Введите дату ->  ')
        notes = (id_str + ';' + head_n + ';' + body_n + ';' + date_n + '\n')
        global read_notes
        read_notes = notes
        return notes, print(read_notes), print('СОХРАНИТЬ ДАННЫЕ ???-- НАЖМИТЕ --  2 -- ИЛИ ДАННЫЕ БУДУТ ПОТЕРЯНЫ !!!')
    except Exception:
        error_notes()
def error_notes():
    return print('No Comand !')

def exit_notes():
    return print('Goodbye !')

def delete_notes():
    array = read_id_notes()
    array1 = array.clear()
    print(array1)


def view_id():
    a = ''
    array = list()
    array1 = list()
    with open('data.csv', 'r', encoding='utf_8') as file:
        array.append(file.read().split())
        for i in array[0]:
            for j in i:
                if j != ';':
                    a += j
                elif j == ';':
                    break
            array1.append(a)
            a = ''
        print(array1)
        return array1


if __name__ == '__main__':
    menu()
    # add_notes(input_notes())5

