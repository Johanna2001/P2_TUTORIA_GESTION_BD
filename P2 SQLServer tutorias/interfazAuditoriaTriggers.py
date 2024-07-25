# audit_triggers.py
import tkinter as tk
from tkinter import ttk
from backend.auditoriaTriggers import crear_tabla_auditoria, generar_triggers, listar_entidades

class AuditTriggersWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Generar Disparadores de Auditoría")

        self.label = ttk.Label(root, text="Entidades y Atributos:")
        self.label.pack(pady=5)

        self.tree_frame = ttk.Frame(root)
        self.tree_frame.pack(pady=5, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.tree_frame, columns=("Atributos"), show="tree headings")
        self.tree.heading("#0", text="Entidad")
        self.tree.heading("Atributos", text="Atributos")
        self.tree.column("#0", width=200, anchor="w")
        self.tree.column("Atributos", width=900, anchor="w")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.populate_entities()

        self.create_table_button = ttk.Button(root, text="Crear Tabla de Auditoría", command=self.crear_tabla_auditoria)
        self.create_table_button.pack(pady=5)

        self.generate_button = ttk.Button(root, text="Generar Disparadores", command=self.generate_triggers)
        self.generate_button.pack(pady=5)

    def populate_entities(self):
        entities = listar_entidades()
        for entity, attributes in entities.items():
            attributes_str = ', '.join(attributes)
            self.tree.insert("", tk.END, text=entity, values=(attributes_str,))

    def crear_tabla_auditoria(self):
        crear_tabla_auditoria()

    def generate_triggers(self):
        selected_items = self.tree.selection()
        entities = [self.tree.item(item, "text") for item in selected_items]
        generar_triggers(entities)

if __name__ == "__main__":
    root = tk.Tk()
    app = AuditTriggersWindow(root)
    root.mainloop()
