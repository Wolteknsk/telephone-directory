import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

phone_book = {}

def load_phone_book():
 """Загружает телефонный справочник из файла"""
 try:
  with open("phone_book.json", "r") as f:
   return json.load(f)
 except FileNotFoundError:
  return {}

def save_phone_book(phone_book):
 """Сохраняет телефонный справочник в файл"""
 with open("phone_book.json", "w") as f:
  json.dump(phone_book, f)

def add_contact():
 """Добавляет новый контакт в телефонный справочник"""
 def save_contact():
  name = name_entry.get()
  phone = phone_entry.get()
  if name and phone:
   phone_book[name] = phone
   messagebox.showinfo("Успех", f"Контакт {name} добавлен!")
   add_window.destroy()
  else:
   messagebox.showerror("Ошибка", "Введите имя и номер телефона.")

 add_window = tk.Toplevel(root)
 add_window.title("Добавить контакт")
 add_window.geometry("300x150")

 name_label = tk.Label(add_window, text="Имя:")
 name_label.grid(row=0, column=0, padx=5, pady=5)
 name_entry = tk.Entry(add_window)
 name_entry.grid(row=0, column=1, padx=5, pady=5)

 phone_label = tk.Label(add_window, text="Телефон:")
 phone_label.grid(row=1, column=0, padx=5, pady=5)
 phone_entry = tk.Entry(add_window)
 phone_entry.grid(row=1, column=1, padx=5, pady=5)

 save_button = tk.Button(add_window, text="Сохранить", command=save_contact)
 save_button.grid(row=2, columnspan=2, padx=5, pady=5)

def find_contact():
 """Ищет контакт в телефонном справочнике."""
 def show_result():
  name = name_entry.get()
  if name in phone_book:
   messagebox.showinfo("Результат", f"Номер телефона {name}: {phone_book[name]}")
  else:
   messagebox.showerror("Ошибка", f"Контакт {name} не найден.")

 find_window = tk.Toplevel(root)
 find_window.title("Найти контакт")
 find_window.geometry("300x100")

 name_label = tk.Label(find_window, text="Имя:")
 name_label.grid(row=0, column=0, padx=5, pady=5)
 name_entry = tk.Entry(find_window)
 name_entry.grid(row=0, column=1, padx=5, pady=5)

 search_button = tk.Button(find_window, text="Искать", command=show_result , color= green)
 search_button.grid(row=1, columnspan=2, padx=5, pady=5)

def delete_contact():
 """Удаляет контакт из телефонного справочника."""
 def confirm_delete():
  name = name_entry.get()
  if name in phone_book:
   if messagebox.askyesno("Подтверждение", f"Удалить контакт {name}?"):
    del phone_book[name]
    messagebox.showinfo("Успех", f"Контакт {name} удален!")
    delete_window.destroy()
   else:
    delete_window.destroy()
  else:
   messagebox.showerror("Ошибка", f"Контакт {name} не найден.")

 delete_window = tk.Toplevel(root)
 delete_window.title("Удалить контакт")
 delete_window.geometry("300x100")

 name_label = tk.Label(delete_window, text="Имя:")
 name_label.grid(row=0, column=0, padx=5, pady=5)
 name_entry = tk.Entry(delete_window)
 name_entry.grid(row=0, column=1, padx=5, pady=5)

 delete_button = tk.Button(delete_window, text="Удалить", command=confirm_delete)
 delete_button.grid(row=1, columnspan=2, padx=5, pady=5)

def show_all_contacts():
 """Показывает все контакты в телефонном справочнике."""
 if phone_book:
  result = "Список контактов:\n"
  for name, phone in phone_book.items():
   result += f"{name}: {phone}\n"
  messagebox.showinfo("Контакты", result)
 else:
  messagebox.showinfo("Контакты", "Телефонный справочник пуст.")

root = tk.Tk()
root.title("Телефонный справочник")
root.geometry("300x250")

# Изменение шрифта
style = ttk.Style()
style.configure("TButton", font=("Arial", 12))

add_button = tk.Button(root, text="Добавить контакт", command=add_contact)
add_button.pack(pady=10)

find_button = tk.Button(root, text="Найти контакт", command=find_contact)
find_button.pack(pady=10)

delete_button = tk.Button(root, text="Удалить контакт", command=delete_contact)
delete_button.pack(pady=10)

show_button = tk.Button(root, text="Показать все контакты", command=show_all_contacts)
show_button.pack(pady=10)

# Загрузка телефонного справочника при запуске
phone_book = load_phone_book()

# Сохранение телефонного справочника при закрытии окна
root.protocol("WM_DELETE_WINDOW", lambda: save_phone_book(phone_book))

root.mainloop()
