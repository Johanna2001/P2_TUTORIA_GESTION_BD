import os
from fpdf import FPDF
import tkinter as tk
from tkinter import messagebox, filedialog, ttk

def get_log_file_path():
    return r'C:\Program Files\Microsoft SQL Server\MSSQL16.SJCQ11\MSSQL\Log\ERRORLOG'

def leer_archivo_completo():
    log_file_path = get_log_file_path()

    if not os.path.exists(log_file_path):
        print(f"El archivo de log no se encontró en la ruta especificada: {log_file_path}")
        return ""

    try:
        with open(log_file_path, 'r') as file:
            contenido = file.read()
            return contenido
    except Exception as e:
        print(f"Error al leer el archivo de log: {e}")
        return ""

def buscar_logs(source=None, action=None):
    log_file_path = get_log_file_path()

    if not os.path.exists(log_file_path):
        print(f"El archivo de log no se encontró en la ruta especificada: {log_file_path}")
        return []

    logs = []
    try:
        with open(log_file_path, 'r', encoding='utf-16') as file:
            for line in file:
                line = line.strip()
                if line.startswith('2024-'):
                    parts = line.strip().split(' ', 3)
                    log_entry = {
                        "fecha": parts[0],
                        "hora": parts[1],
                        "source": parts[2],
                        "mensaje": parts[3] if len(parts) > 3 else ""
                    }

                    if (source and log_entry["source"] != source) or (action and action not in log_entry["mensaje"]):
                        continue

                    logs.append(log_entry)

        print(f"Logs encontrados: {len(logs)}")  # Depuración: cantidad de logs encontrados
    except Exception as e:
        print(f"Error al leer el archivo de log: {e}")

    return logs

def generar_pdf(logs, output_path="logs.pdf"):
    headers = ["fecha", "hora", "source", "mensaje"]
    header_widths = [40, 30, 30, 100]  # Ajusta los anchos de las columnas aquí

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Dibujar los encabezados de columna
    for i, header in enumerate(headers):
        pdf.cell(header_widths[i], 10, header.capitalize(), 1, 0, 'C')
    pdf.ln()

    # Agregar los registros
    for log in logs:
        pdf.cell(header_widths[0], 10, log[0], 1)
        pdf.cell(header_widths[1], 10, log[1], 1)
        pdf.cell(header_widths[2], 10, log[2], 1)
        pdf.multi_cell(header_widths[3], 10, log[3], 1)
        pdf.ln()

    pdf.output(output_path)
    messagebox.showinfo("Éxito", f"Logs filtrados guardados en {output_path}")

def filter_logs(entry_source, entry_action, tree):
    source = entry_source.get().strip()
    action = entry_action.get().strip()
    logs = buscar_logs(source=source, action=action)
    update_tree(logs, tree)

def update_tree(logs, tree):
    for item in tree.get_children():
        tree.delete(item)
    for log in logs:
        tree.insert("", "end", values=(log["fecha"], log["hora"], log["source"], log["mensaje"]))

def save_as_pdf(tree):
    logs = [tree.item(item)['values'] for item in tree.get_children()]
    if not logs:
        messagebox.showerror("Error", "No hay logs para guardar.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        generar_pdf(logs, output_path=file_path)

def leer_y_mostrar_archivo_completo():
    contenido = leer_archivo_completo()
    print(contenido)  # Imprimir el contenido del archivo en la consola
