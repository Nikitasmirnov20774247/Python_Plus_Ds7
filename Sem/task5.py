# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.


import random


def file_extensions(extensions, min_lenght=6, max_lenght=30, min_bytes=256, max_bytes=4096):
    for extension in extensions:
        for i in range(extensions[extension]):
            name = ''
            for j in range(random.randint(min_lenght, max_lenght)):
                tmp = chr(random.randint(97, 122))
                name = name + tmp
            with open(f'{name}.{extension}', 'w', encoding='UTF-8') as f:
                for k in range(random.randint(min_bytes, max_bytes)):
                    print(chr(random.randint(97, 122)), file=f, end='')


file_extensions({'jpg':1, 'pdf':2})