# ----------------------- # Librerias # ----------------------- #
import tkinter as tk
from tkinter import ttk, messagebox
import math


# ----------------------- # Diccionario base legible → valor numérico # ----------------------- # 
base_map = {
    "Binario": 2,
    "Octal": 8,
    "Decimal": 10,
    "Hexadecimal": 16
}


# ----------------------- # Conversión de bases # ----------------------- # 
def to_binary(value, base):
    try:
        decimal = int(value, base)
        return bin(decimal)[2:]
    except ValueError:
        messagebox.showerror("Error", f"Número inválido para base {base}")
        return None

def binary_to_int(binary_str):
    try:
        return int(binary_str, 2)
    except ValueError:
        messagebox.showerror("Error", f"Binario inválido: {binary_str}")
        return None

def from_decimal(value, base):
    try:
        if base == 2:
            return bin(value)[2:]
        elif base == 8:
            return oct(value)[2:]
        elif base == 10:
            return str(value)
        elif base == 16:
            return hex(value)[2:].upper()
    except:
        return "Error"


# ----------------------- # Operaciones binarias # ----------------------- # 
def binary_add(a, b):
    return bin(int(a,2)+int(b,2))[2:]

def binary_subtract(a, b):
    res = int(a,2) - int(b,2)
    if res < 0:
        raise ValueError("Resultado negativo no soportado")
    return bin(res)[2:]

def binary_multiply(a, b):
    return bin(int(a,2)*int(b,2))[2:]

def binary_divide(a, b):
    divisor = int(b,2)
    if divisor == 0:
        return None
    return bin(int(a,2)//divisor)[2:]


# ----------------------- # Funciones de cálculo # ----------------------- # 
def calculate():
    base1 = base_map[base1_var.get()]
    base2 = base_map[base2_var.get()]
    op = operation_var.get()

    bin1 = to_binary(entry1.get(), base1)
    if bin1 is None:
        return

    if op == "√":
        decimal_value = binary_to_int(bin1)

        bin2 = to_binary(entry2.get(), base2)
        if bin2 is None:
            return
        index_value = binary_to_int(bin2)

        if index_value <= 0:
            messagebox.showerror("Error", "El índice de raíz debe ser mayor que cero")
            return

        root_value = decimal_value ** (1 / index_value)
        floored_root = math.floor(root_value)

        result = bin(floored_root)[2:]
    else:
        bin2 = to_binary(entry2.get(), base2)
        if bin2 is None:
            return

        try:
            if op == "+":
                result = binary_add(bin1, bin2)
            elif op == "-":
                result = binary_subtract(bin1, bin2)
            elif op == "*":
                result = binary_multiply(bin1, bin2)
            elif op == "/":
                if bin2 == '0':
                    messagebox.showerror("Error", "División entre cero")
                    return
                result = binary_divide(bin1, bin2)
            elif op == "^":
                result = bin(binary_to_int(bin1) ** binary_to_int(bin2))[2:]
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

    global current_result_binary
    current_result_binary = result
    update_result_display(result)


# ----------------------- # Actualizar Resultado # ----------------------- # 
def update_result_display(bin_value):
    base_name = result_base_var.get()
    base = base_map[base_name]
    decimal_value = binary_to_int(bin_value)
    converted = from_decimal(decimal_value, base)
    result_label.config(text=f"Resultado en {base_name}: {converted}")


# ----------------------- # Actualizar Teclado Dinámico # ----------------------- # 
def update_numpad():
    for widget in numpad_frame.winfo_children():
        widget.destroy()

    selected_base = base_map[current_base_var.get()]

    if selected_base == 2:
        keys = ['0', '1']
    elif selected_base == 8:
        keys = [str(i) for i in range(8)]
    elif selected_base == 10:
        keys = [str(i) for i in range(10)]
    elif selected_base == 16:
        keys = [str(i) for i in range(10)] + list('ABCDEF')

    row = 0
    col = 0
    for key in keys:
        btn = tk.Button(numpad_frame, text=key, width=4, command=lambda k=key: insert_to_active_entry(k), bg="white", fg="black", relief="flat")
        btn.grid(row=row, column=col, padx=2, pady=2)
        col += 1
        if col > 3:
            col = 0
            row += 1

    tk.Button(numpad_frame, text="⌫", width=4, command=backspace, bg="#f0f0f0", relief="flat").grid(row=row+1, column=0, padx=2, pady=2)
    tk.Button(numpad_frame, text="C", width=4, command=clear_active_entry, bg="#f0f0f0", relief="flat").grid(row=row+1, column=1, padx=2, pady=2)
    tk.Button(numpad_frame, text="Resultado ➔", width=9, command=use_result_in_active, bg="#f0f0f0", relief="flat").grid(row=row+1, column=2, columnspan=2, padx=2, pady=2)


# ----------------------- # Helpers para Teclado # ----------------------- #
def insert_to_active_entry(value):
    if active_entry == 1:
        entry1.insert(tk.END, value)
    else:
        entry2.insert(tk.END, value)

def backspace():
    if active_entry == 1:
        current = entry1.get()
        entry1.delete(0, tk.END)
        entry1.insert(0, current[:-1])
    else:
        current = entry2.get()
        entry2.delete(0, tk.END)
        entry2.insert(0, current[:-1])

def clear_active_entry():
    if active_entry == 1:
        entry1.delete(0, tk.END)
    else:
        entry2.delete(0, tk.END)

def use_result_in_active():
    value_in_base = from_decimal(binary_to_int(current_result_binary), base_map[current_base_var.get()])
    if active_entry == 1:
        entry1.delete(0, tk.END)
        entry1.insert(0, value_in_base)
    else:
        entry2.delete(0, tk.END)
        entry2.insert(0, value_in_base)


# ----------------------- # Cambio de base # ----------------------- #
def on_entry1_base_change(event=None):
    global active_entry
    active_entry = 1
    current_base_var.set(base1_var.get())
    update_numpad()

def on_entry2_base_change(event=None):
    global active_entry
    active_entry = 2
    current_base_var.set(base2_var.get())
    update_numpad()

def on_result_base_change(event=None):
    update_result_display(current_result_binary)


# ----------------------- # Interfaz Gráfica # ----------------------- #
root = tk.Tk()
root.title("Calculadora")
root.configure(bg="#f5f5f5")

current_result_binary = '0'
active_entry = 1
current_base_var = tk.StringVar(value="Decimal")

## -------- Fila 1: Información -------- ##
info_label = tk.Label(root, text="Calculadora hecha por Jhanth Carlo Castillo Pérez", font=("Segoe UI", 9), anchor="w", bg="#f5f5f5")
info_label.grid(row=0, column=0, columnspan=4, sticky="w", padx=10, pady=5)

## -------- Fila 2: Bases y entradas -------- ##
base1_var = tk.StringVar(value="Decimal")
combo1 = ttk.Combobox(root, textvariable=base1_var, values=list(base_map.keys()), width=12)
combo1.grid(row=1, column=0, padx=5, pady=5)
combo1.bind("<<ComboboxSelected>>", on_entry1_base_change)

entry1 = tk.Entry(root, width=15)
entry1.grid(row=1, column=1, padx=5, pady=5)

base2_var = tk.StringVar(value="Decimal")
combo2 = ttk.Combobox(root, textvariable=base2_var, values=list(base_map.keys()), width=12)
combo2.grid(row=1, column=2, padx=5, pady=5)
combo2.bind("<<ComboboxSelected>>", on_entry2_base_change)

entry2 = tk.Entry(root, width=15)
entry2.grid(row=1, column=3, padx=5, pady=5)

## -------- Fila 3: Operaciones y calcular -------- ##
operation_var = tk.StringVar(value="+")
operation_menu = ttk.Combobox(root, textvariable=operation_var, values=["+", "-", "*", "/", "^", "√"], width=5)
operation_menu.grid(row=2, column=0, padx=5, pady=5)

tk.Button(root, text="Calcular", command=calculate, width=12, bg="white", relief="flat").grid(row=2, column=1)

result_base_var = tk.StringVar(value="Binario")
result_base_menu = ttk.Combobox(root, textvariable=result_base_var, values=list(base_map.keys()), width=12)
result_base_menu.grid(row=2, column=2)
result_base_menu.bind("<<ComboboxSelected>>", on_result_base_change)

## -------- Fila 4: Resultado -------- ##
result_frame = tk.Frame(root, relief="solid", borderwidth=1, bg="white")
result_frame.grid(row=3, column=0, columnspan=4, padx=5, pady=10, sticky="ew")

result_label = tk.Label(result_frame, text="Resultado en Binario:", font=("Segoe UI", 11, "bold"), bg="white")
result_label.pack(padx=10, pady=5, anchor="w")

## -------- Fila 5: Numpad Dinámico -------- ##
numpad_frame = tk.Frame(root, bg="#f5f5f5")
numpad_frame.grid(row=4, column=0, columnspan=4)

update_numpad()

# Ejecutar interfaz
root.mainloop()
