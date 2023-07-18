# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.


import random


def file_extension(extension, min_lenght=6, max_lenght=30, min_bytes=256, max_bytes=4096, num_files=42):
    for i in range(num_files):
        name = ''
        for j in range(random.randint(min_lenght, max_lenght)):
            tmp = chr(random.randint(97, 122))
            name = name + tmp
        with open(f'{name}.{extension}', 'w', encoding='UTF-8') as f:
            for k in range(random.randint(min_bytes, max_bytes)):
                print(chr(random.randint(97, 122)), file=f, end='')


file_extension('jpg', num_files=1)
