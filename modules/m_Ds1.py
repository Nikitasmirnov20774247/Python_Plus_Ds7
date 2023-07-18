# Напишите функцию группового переименования файлов.
# Она должна:
# ✔ Принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# ✔ Принимать параметр количество цифр в порядковом номере.
# ✔ Принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# ✔ Принимать параметр расширение конечного файла.
# ✔ Принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.


from sys import argv
import os


def rename_files(dir, desired_name, enumerate_i, orig_ext, new_ext, range):
    count = 0
    for elem in os.listdir(dir):
        if not os.path.isdir(elem):
            ext = elem.split('.')[-1]
            if ext == orig_ext:
                old_name = elem.split('.')[0][range[0]:range[1] + 1]
                if old_name != '':
                    new_name = f'{old_name}_{desired_name}_{count:0{enumerate_i}d}.{new_ext}'
                else:
                    new_name = f'{desired_name}_{count:0{enumerate_i}d}.{new_ext}'
                os.rename(os.path.join(dir, elem), os.path.join(dir, new_name))
                count += 1
    return count


if __name__ == '__main__':
    try:
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
