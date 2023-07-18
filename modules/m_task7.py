# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.


import os
import shutil


def func_sort(d, folder):
    for dir, _, files in os.walk(folder):
        for file in files:
            ext = file.split('.')[-1]
            for item in d:
                if ext in d[item]:
                    if not os.path.isdir(item):
                        os.mkdir(item)
                    # shutil.move(f'{folder}/{dir}/{file}', item)
                    shutil.move(f'{folder}/{file}', item)     


func_sort({'video':['avi', 'mov'],
           'pictures':['jpg', 'png'], }, 'tmp1')