import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from backend.procesoHilos import comparar_consultas, get_fixed_queries

class QueryComparisonWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Comparación de Consultas")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.option_var = tk.StringVar(value="fixed")

        self.fixed_option = tk.Radiobutton(self.frame, text="Usar consultas fijas", variable=self.option_var, value="fixed", command=self.toggle_option)
        self.fixed_option.pack(anchor=tk.W)

        self.custom_option = tk.Radiobutton(self.frame, text="Usar consultas personalizadas", variable=self.option_var, value="custom", command=self.toggle_option)
        self.custom_option.pack(anchor=tk.W)

        self.query_frame = tk.Frame(self.frame)
        self.query_frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.query_frame, text="Ingrese las consultas a comparar (una por línea):")
        self.label.pack()

        self.textbox = tk.Text(self.query_frame, height=10, width=50)
        self.textbox.pack()

        self.thread_label = tk.Label(self.frame, text="Cantidad de hilos:")
        self.thread_label.pack()

        self.thread_entry = tk.Entry(self.frame)
        self.thread_entry.pack()

        self.compare_button = tk.Button(self.frame, text="Comparar Consultas", command=self.comparar_consultas)
        self.compare_button.pack(pady=5)

        self.toggle_option()

    def toggle_option(self):
        if self.option_var.get() == "fixed":
            self.textbox.config(state=tk.DISABLED)
        else:
            self.textbox.config(state=tk.NORMAL)

    def comparar_consultas(self):
        num_threads = self.thread_entry.get()
        if not num_threads.isdigit():
            messagebox.showwarning("Advertencia", "Ingrese una cantidad válida de hilos.")
            return

        num_threads = int(num_threads)

        if self.option_var.get() == "fixed":
            queries = get_fixed_queries()
        else:
            queries_text = self.textbox.get("1.0", tk.END).strip()
            if not queries_text:
                messagebox.showwarning("Advertencia", "Ingrese al menos una consulta.")
                return
            queries = queries_text.split("\n")

        results = comparar_consultas(queries, num_threads)
        self.mostrar_resultados(queries, results)
    
    def mostrar_resultados(self, queries, results):
        result_window = tk.Toplevel(self.root)
        result_window.title("Resultados de Comparación de Consultas")

        columns = ["Consulta"] + [f"Hilo {i+1}" for i in range(len(results[0]))]
        tree = ttk.Treeview(result_window, columns=columns, show='headings')
        tree.pack(fill=tk.BOTH, expand=True)

        tree.heading("Consulta", text="Consulta")
        for i in range(len(results[0])):
            tree.heading(f"Hilo {i+1}", text=f"Hilo {i+1}")

        for i, query in enumerate(queries):
            row = [query] + [f"{results[i][j][1]:.4f}" if results[i][j] else "Error" for j in range(len(results[i]))]
            tree.insert("", tk.END, values=row)

        scrollbar = ttk.Scrollbar(result_window, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=scrollbar.set)
        scrollbar.pack(fill=tk.X, expand=False)

if __name__ == "__main__":
    root = tk.Tk()
    app = QueryComparisonWindow(root)
    root.mainloop()