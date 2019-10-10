#задача1
import os

dir_name = [('dir_' + str(i + 1)) for i in range(9)]
def make_dir(path):
    dir_loc = os.path.join(os.getcwd(), path)
    try:
        os.mkdir(dir_loc)
        print(' — папка успешно создана')
    except:
        print(dir_loc + ' — папка уже существует')
for i in dir_name:
    make_dir(i)


#задача2
import os
list = os.listdir()
for i in list:
    print(i)

#задача3
import shutil
shutil.copy('ДЗ Соломатова урок 5.py','ДЗ Соломатова урок 5 копия.py')

#задача1
import os
def change_dir(dir_path):
    try:
        os.chdir(dir_path)
        print(os.getcwd() + ' - текущая директория')
    except:
        print(dir_path + ' - такой директории нет')
        import easy
        exit_os = 'a'
        while exit_os != '0':
            print('Перейти в папку: 1')
            print('Просмотреть содержимое текущей папки: 2')
            print('Удалить папку: 3')
            print('Создать папку: 4')
            print('Для выхода: 0')
            exit_os = input('Выбрать: ')
            print(exit_os)
            if exit_os == '1':
                dir_name = input('Введите полный путь папки: ')
                easy.change_dir(dir_name)
            elif exit_os == '2':
                dir_name = os.getcwd()
                easy.list_dir(dir_name)
            elif exit_os == '3':
                dir_name = input('Введите полный путь папки: ')
                easy.delete_dir(dir_name)
            elif exit_os == '4':
                dir_name = input('Введите полный путь папки: ')
                easy.make_dir(dir_name)
            elif exit_os == '0':
                pass
            else:
                print('Ошибка!')