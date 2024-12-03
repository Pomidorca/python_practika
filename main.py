# Лабораторная работа № 1
# РАБОТА В IDLE. ИСПОЛЬЗОВАНИЕ
# АРИФМЕТИЧЕСКИХ ОПЕРАЦИЙ. СОЗДАНИЕ СПИСКОВ
# И СЛОВАРЕЙ. РАБОТА С ЦИКЛАМ

# Цель работы: научиться использовать IDLE при работе с
# Python; изучить списки и словари, освоить основные методы
# для работы с ними; изучить виды циклов в Python.

# 1. Написать функцию, которая принимает целочисленный
# список с количеством элементов 1 или более и возвращает
# True, если цифра 6 является первым или последним элементом
# списка.


# def checkingForTheNumberSix(mass):
#     if mass[0] == 6 or mass[-1] == 6:
#         return True
#     return False
#
# print(checkingForTheNumberSix([4, 1, 1]))


# Лабораторная работа №2
# РАБОТА С ОСНОВНЫМИ ВСТРОЕННЫМИ
# ФУНКЦИЯМИ

# Цель работы: рассмотреть основные встроенные функции
# языка программирования Python и научиться с ними работать.

# 1. Написать функцию, которая принимает целое число и
# возвращает сгенерированный список, содержащий количество
# элементов от 0 до входящего числа включительно.

# import random
#
# def listGenerator(n):
#     return [random.randint(0, n) for _ in range(n + 1)]
#
# print(listGenerator(6))


# Лабораторная работа №3
# РАБОТА С ИТЕРАТОРАМИ, ГЕНЕРАТОРАМИ.
# РАБОТА С ГЕНЕРАТОРНЫМИ ВЫРАЖЕНИЯМИ
# Цель работы: изучить понятия итератора и генератора в
# Python, а также их преимущества; ознакомиться с примерами
# их пользования.


# 1. Написать функцию, которая принимает целое число и с
# помощью генераторного выражения создает и возвращает но-
# вый список случайных чисел с длиной входящего числа.

# import random
#
# def generate_random_list_with_length(n):
#     return [random.randint(0, 100) for _ in range(n)]
#
# print(generate_random_list_with_length(5))


# Лабораторная работа №4
# РАБОТА С ОСНОВНЫМИ МОДУЛЯМИ
# Цель работы: изучить основные модули стандартной биб-
# лиотеки Python 3; рассмотреть модули os и datetime.

# 1. Написать функцию, которая принимает объект datetime
# и возвращает True, если год полученного значения високосный.

# import datetime
#
# def is_leap_year(date):
#     year = date.year
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
#
# date = datetime.datetime(2024, 1, 1)
# print(is_leap_year(date))  # True
#
# date = datetime.datetime(2023, 1, 1)
# print(is_leap_year(date))  # False


# Лабораторная работа №5
# РАБОТА С ФАЙЛАМИ. РАЗРАБОТКА
# СИНТАКСИЧЕСКОГО АНАЛИЗАТОРА. ВЫВОД
# ФОРМАТИРОВАННЫХ ДАННЫХ В ФОРМАТЕ JSON
# Цель работы: изучить работу с файлами с помощью
# функций из стандартной библиотеки; рассмотреть понятие син-
# таксического анализа текста и ознакомиться с его применением
# на языке Python; изучить возможности взаимодействия Python с
# форматом хранения данных JSON.

# 1. Написать функцию, которая принимает Json строку и
# конвертирует её в словарь.

# import json
#
# def json_to_dict(json_string):
#     return json.loads(json_string)
#
#
# json_string = '{"name": "John", "age": 30, "city": "New York"}'
# dictionary = json_to_dict(json_string)
# print(dictionary)


# Лабораторная работа №6
# РАЗРАБОТКА ПРИЛОЖЕНИЯ РАБОТЫ С БАЗОЙ
# ДАННЫХ
# Цель работы: изучить возможности взаимодействия Py-
# thon с реляционными базами данных с помощью DB-API 2.0.

# 1. Написать функцию, которая принимает наименование
# таблицы, поля и его значение и возвращает идентификатор за-
# писи, в которой значение полученного поля соответствует пе-
# реданному функции, или возвращает None
#
# import sqlite3
#
# def find_record_id_by_field(table_name, field_name, field_value):
#     # Подключаемся к базе данных
#     conn = sqlite3.connect('db_lab6.db')  # Здесь база данных
#     cursor = conn.cursor()
#
#     # Формируем SQL-запрос
#     query = f"SELECT id FROM {table_name} WHERE {field_name} = ?"
#
#     # Выполняем запрос с параметром
#     cursor.execute(query, (field_value,))
#
#     # Получаем результат
#     result = cursor.fetchone()
#
#     # Закрываем соединение с базой данных
#     conn.close()
#
#     # Возвращаем идентификатор записи или None
#     if result:
#         return result[0]  # Первый элемент - это ID записи
#     else:
#         return None
#
# record_id = find_record_id_by_field('users', 'email', 'john@example.com') #(users, 'email', 'john@example.com')(2, 'Jane Smith', 'jane@example.com')(3, 'Alice Johnson', 'alice@example.com')
# if record_id:
#     print(f"ID записи: {record_id}")
# else:
#     print(None)

#
# Лабораторная работа №7
# РАЗРАБОТКА ПРИЛОЖЕНИЯ С ИСПОЛЬЗОВАНИЕМ
# ООП


# 1. Написать родительский и дочерний классы с методами
# «display». В каждом методе в консоль выводится различная
# строка.

# class Parent:
#     def display(self):
#         print("Это метод display родительского класса.")
#
# class Child(Parent):
#     def display(self):
#         print("Это метод display дочернего класса.")
#
# # Создаем экземпляры классов
# parent_instance = Parent()
# child_instance = Child()
#
# # Вызываем методы display
# parent_instance.display()  # Вывод: Это метод display родительского класса.
# child_instance.display()   # Вывод: Это метод display дочернего класса.


# Лабораторная работа №8
# ОБРАБОТКА ИЗОБРАЖЕНИЙ С ПРИМЕНЕНИЕМ
# БИБЛИОТЕКИ PIL

# 1. Написать функцию, которая принимает путь к дирек-
# тории и создает новую директорию по тому же пути с именем
# thumbnail, в которую записывает иконки изображений, находя-
# щихся в принятой функцией директории.


# from PIL import Image
# import os
#
# def create_thumbnails(directory):
#
#     # Проверяем, существует ли переданная директория
#     if not os.path.isdir(directory):
#         print("Указанный путь не является директорией.")
#         return
#
#     # Создаем директорию для сохранения иконок
#     thumbnail_dir = os.path.join(directory, "thumbnail")
#     os.makedirs(thumbnail_dir, exist_ok=True)
#
#     # Перебираем все файлы в директории
#     for filename in os.listdir(directory):
#         file_path = os.path.join(directory, filename)
#
#         # Проверяем, является ли файл изображением
#         if os.path.isfile(file_path) and filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
#             try:
#                 # Открываем изображение
#                 with Image.open(file_path) as img:
#                     # Создаем иконку размером 128x128
#                     img.thumbnail((128, 128))
#
#                     # Сохраняем иконку в новую директорию
#                     thumbnail_path = os.path.join(thumbnail_dir, filename)
#                     img.save(thumbnail_path)
#
#                     print(f"Иконка для файла '{filename}' успешно создана.")
#             except Exception as e:
#                 print(f"Ошибка при обработке файла '{filename}': {e}")
#
#
# create_thumbnails("C:/Users/торо/Desktop/python_practik/")

# Лабораторная работа №9
# РАЗРАБОТКА GUI ПРИЛОЖЕНИЯ С ПОМОЩЬЮ
# ГРАФИЧЕСКИХ БИБЛИОТЕК

# 1. Написать GUI приложение, которое имеет текстовое
# поле и кнопку для сохранения текста, при нажатии на которую
# открывается модальное окно указания пути для сохранения
# текстового файла.

#
# import tkinter as tk
# from tkinter import filedialog, messagebox
#
# def save_text():
#     # Получаем текст из текстового поля
#     text = text_field.get("1.0", tk.END).strip()
#
#     if not text:
#         messagebox.showwarning("Предупреждение", "Текстовое поле пустое! Пожалуйста, введите текст для сохранения.")
#         return
#
#     # Открываем модальное окно для выбора пути сохранения файла
#     file_path = filedialog.asksaveasfilename(
#         title="Сохранить текстовый файл",
#         defaultextension=".txt",
#         filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
#     )
#
#     if file_path:
#         try:
#             # Сохраняем текст в указанный файл
#             with open(file_path, "w", encoding="utf-8") as file:
#                 file.write(text)
#             messagebox.showinfo("Успех", f"Файл успешно сохранён: {file_path}")
#         except Exception as e:
#             messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")
#
# # Создаём основное окно приложения
# root = tk.Tk()
# root.title("Сохранение текста")
# root.geometry("400x300")
#
# # Добавляем текстовое поле
# text_field = tk.Text(root, wrap=tk.WORD, width=40, height=10)
# text_field.pack(pady=10)
#
# # Добавляем кнопку сохранения
# save_button = tk.Button(root, text="Сохранить текст", command=save_text)
# save_button.pack(pady=5)
#
# # Запускаем главное событие приложения
# root.mainloop()


# Лабораторная работа №10
# ВИЗУАЛИЗАЦИЯ РЕЗУЛЬТАТОВ РАБОТЫ
# МАТЕМАТИЧЕСКИХ АЛГОРИТМОВ
# С ИСПОЛЬЗОВАНИЕМ NUMPY И MATPLOTLIB

# 1. Написать функцию, которая принимает список целых чи-
# сел и возвращает True, если в списке отсутствуют нули, в про-
# тивном случае возвращает False.

import numpy as np

def has_no_zeros_numpy(int_list):

    array = np.array(int_list)
    return np.all(array != 0)

# Пример использования
example_list = [1, 2, 3, 4, 5]
print(has_no_zeros_numpy(example_list))  # Вывод: True

example_list_with_zero = [1, 2, 0, 4, 5]
print(has_no_zeros_numpy(example_list_with_zero))  # Вывод: False
