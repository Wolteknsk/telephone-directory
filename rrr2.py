import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

phone_book = {}

def load_phone_book():
  try:
    with open("phone_book.json", "r", encoding="utf-8") as f: # добавлена кодировка
      return json.load(f)
  except FileNotFoundError:
    return {}

def save_phone_book():
  with open("phone_book.json", "w", encoding="utf-8") as f: # добавлена кодировка
    json.dump(phone_book, f, ensure_ascii=False, indent=4) # ensure_ascii=False для кириллицы, indent для читаемости

def add_contact():
  def save_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
      phone_book[name] = phone
      messagebox.showinfo("Успех", f"Контакт {name} добавлен!")
      add_window.destroy()
      save_phone_book() # Сохранение сразу после добавления
    else:
      messagebox.showerror("Ошибка", "Пожалуйста, введите имя и номер телефона.")

  add_window = tk.Toplevel(root)
  add_window.title("Добавить контакт")
  add_window.geometry("300x150")

  name_label = ttk.Label(add_window, text="Имя:")
  name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W) # sticky для лучшего выравнивания
  name_entry = ttk.Entry(add_window)
  name_entry.grid(row=0, column=1, padx=5, pady=5)

  phone_label = ttk.Label(add_window, text="Телефон:")
  phone_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
  phone_entry = ttk.Entry(add_window)
  phone_entry.grid(row=1, column=1, padx=5, pady=5)

  save_button = ttk.Button(add_window, text="Сохранить", command=save_contact)
  save_button.grid(row=2, columnspan=2, padx=5, pady=10) # Увеличено pady для интервала


def find_contact():
  def show_result():
    name = find_name_entry.get() # Corrected variable name
    if name in phone_book:
      messagebox.showinfo("Результат", f"Номер телефона для {name}: {phone_book[name]}")
    else:
      messagebox.showerror("Ошибка", f"Контакт {name} не найден.")
    find_window.destroy() #Close window after search

  find_window = tk.Toplevel(root)
  find_window.title("Найти контакт")
  find_window.geometry("300x100")

  find_name_label = ttk.Label(find_window, text="Имя:") #Renamed for clarity
  find_name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
  find_name_entry = ttk.Entry(find_window) #Renamed for clarity. This is crucial!
  find_name_entry.grid(row=0, column=1, padx=5, pady=5)

  search_button = ttk.Button(find_window, text="Искать", command=show_result, style="TButton")
  search_button.grid(row=1, columnspan=2, padx=5, pady=10)

  search_button = ttk.Button(find_window, text="Искать", command=show_result)
  search_button.grid(row=1, columnspan=2, padx=5, pady=10)


def confirm_delete():
    name = name_entry.get()
    if name in phone_book:
      if messagebox.askyesno("Подтверждение", f"Удалить контакт {name}?"):
        del phone_book[name]
        messagebox.showinfo("Успех", f"Контакт {name} удален!")
        save_phone_book() #Сохранение после удаления
        delete_window.destroy()
      else:
        delete_window.destroy()
    else:
      messagebox.showerror("Ошибка", f"Контакт {name} не найден.")

    delete_window = tk.Toplevel(root)
    delete_window.title("Удалить контакт")
    delete_window.geometry("300x100")

    name_label = ttk.Label(delete_window, text="Имя:")
    name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    name_entry = ttk.Entry(delete_window)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    delete_button = ttk.Button(delete_window, text="Удалить", command=confirm_delete)
    delete_button.grid(row=1, columnspan=2, padx=5, pady=10)


def show_all_contacts():
  if phone_book:
    result = "Контакты:\n"
    for name, phone in phone_book.items():
      result += f"{name}: {phone}\n"
    messagebox.showinfo("Контакты", result)
  else:
    messagebox.showinfo("Контакты", "Телефонная книга пуста.")

root = tk.Tk()
root.title("Телефонная книга")
root.geometry("1000x500")

root.configure(bg="black") # Set background color to black

style = ttk.Style()
style.theme_use('clam') #or other theme that supports this kind of customization
style.configure("TButton", background="yellow", foreground="black", font=("Arial", 12), padding=6)
style.configure("TLabel", background="black", foreground="yellow", font=("Arial", 12))
style.configure("TEntry", background="yellow", foreground="black", font=("Arial", 12))


# Использование ttk для лучшего стиля
style = ttk.Style()
style.configure("TButton", padding=6, font=("Arial", 12)) #Добавлен padding

add_button = ttk.Button(root, text="Добавить контакт", command=add_contact, style="TButton")
add_button.pack(pady=10)

find_button = ttk.Button(root, text="Найти контакт", command=find_contact, style="TButton")
find_button.pack(pady=10)

delete_button = ttk.Button(root, text="Удалить контакт", style="TButton")
delete_button.pack(pady=10)

show_button = ttk.Button(root, text="Показать все контакты", command=show_all_contacts, style="TButton")
show_button.pack(pady=10)

phone_book = load_phone_book()
root.mainloop()