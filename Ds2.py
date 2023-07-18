# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.


import os
from sys import argv
from modules import fill_file, fill_file2, func, file_extension, file_extensions, file_extensions_folder, func_sort, rename_files


if __name__ == '__main__':
    
    fill_file('1.txt', 10)

    fill_file2('2.txt', 10)

    func('1.txt', '2.txt', '3.txt')

    file_extension('jpg', num_files=1)

    file_extensions({'jpg':1, 'pdf':2})

    file_extensions_folder('tmp1', {'jpg':1, 'pdf':2})

    func_sort({'video':['avi', 'mov'],
            'pictures':['jpg', 'png'], }, 'tmp1')

    try:
        os.chdir("..")
        os.chdir("..")
        if len(argv) > 1:
            dir = argv[1]
        else:
            if not os.path.isdir('test2'):
                os.mkdir('test2')
            dir = f'{os.getcwd()}\\test2'
        count = rename_files(dir, 'file', 3, 'jpg', 'png', (3, 6))
        print(f'Переименовано файлов: {count}')
    except Exception as e:
        print(f'!! Введён некорректный путь до файла !!\n{e}')
