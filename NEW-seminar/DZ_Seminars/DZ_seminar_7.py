# Задание 1. Функцию группового переименования файлов.
# Напишите функцию группового переименования файлов. Она должна:
# 1. принимать параметр желаемое конечное имя файлов. При
# переименовании в конце имени добавляется порядковый номер.
# 2. принимать параметр количество цифр в порядковом номере.
# 3. принимать параметр расширение исходного файла. Переименование
# должно работать только для этих файлов внутри каталога.
# 4. принимать параметр расширение конечного файла.
# 5. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик
# файлов и расширение. 3.Соберите из созданных на уроке и в рамках домашнего
# задания функций пакет для работы с файлами.


# Задача 2. Создание архива каталога
# Напишите скрипт, который создает архив каталога в формате .zip. Скрипт
# должен принимать путь к исходному каталогу и путь к целевому архиву. Архив
# должен включать все файлы и подпапки исходного каталога.

# import os
# import zipfile
# def zip_directory(source_dir, output_zip):
#     """
#     Создает архив .zip из указанного каталога.
#     :param source_dir: Путь к исходному каталогу для архивирования.
#     :param output_zip: Путь к целевому архиву .zip.
#     """
#     # Создаем объект ZipFile для записи архива
#     with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
#         # Проходим по всем файлам и папкам в исходном каталоге
#         for root, dirs, files in os.walk(source_dir):
#             for file in files:
#                 # Полный путь к текущему файлу
#                 file_path = os.path.join(root, file)
#                 # Добавляем файл в архив с путем относительно исходного каталога
#                 zipf.write(file_path, os.path.relpath(file_path, source_dir))
#
# # Пример использования функции
# zip_directory('/path/to/source_dir', '/path/to/output.zip')


# Задача 3. Удаление старых файлов
# Напишите скрипт, который удаляет файлы в указанном каталоге, которые не
# изменялись более заданного количества дней. Скрипт должен принимать путь к
# каталогу и количество дней.
#
# import os
# import time
# def delete_old_files(directory, days_old):
#     """
#     Удаляет файлы в указанном каталоге, которые не изменялись более
#     заданного количества дней.
#     :param directory: Путь к каталогу, в котором нужно удалить
#     старые файлы.
#     :param days_old: Количество дней, после которых файлы считаются
#     старыми.
#     """
#     now = time.time() # Текущее время в секундах с начала эпохи
#     cutoff = now - (days_old * 86400) # Преобразуем количество дней в секунды (86400 секунд в дне)
#     # Проходим по всем каталогам и файлам в указанном каталоге
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             file_path = os.path.join(root, file) # Полный путь к файлу
#             file_mod_time = os.path.getmtime(file_path) # Время последнего изменения файла
#             # Если время последнего изменения меньше порогового значения, удаляем файл
#             if file_mod_time < cutoff:
#                 os.remove(file_path) # Удаляем файл
#                 print(f"Удален файл: {file_path}")
#
# # Пример использования функции
# delete_old_files('/path/to/directory', 30)


# Задача 4. Поиск файлов по расширению
# Напишите функцию, которая находит и перечисляет все файлы с заданным
# расширением в указанном каталоге и всех его подкаталогах. Функция должна
# принимать путь к каталогу и расширение файла.

import os

def find_files_by_extension(directory, extension):
    """
    Находит и перечисляет все файлы с заданным расширением в
    указанном каталоге и всех его подкаталогах.
    :param directory: Путь к каталогу, в котором нужно искать файлы.
    :param extension: Расширение файлов для поиска (например,
    '.txt').
    """
    # Проходим по всем каталогам и файлам в указанном каталоге
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Проверяем, заканчивается ли имя файла на заданное расширение
            if file.endswith(extension):
                # Формируем полный путь к файлу и выводим его
                print(os.path.join(root, file))

# Пример использования функции
find_files_by_extension('/path/to/directory', '.txt')
