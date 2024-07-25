import pyodbc
import threading
import time
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

def get_connection():
    try:
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=SANDY-CQ11\SJCQ11;'
        'DATABASE=Kinder_Parcial2;'
        'UID=SANDY-CQ11\1116;'
        'PWD=Sandy1116;'
        'Trusted_Connection=yes'
        )
        print("Conexión exitosa")
        return connection
    except pyodbc.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def ejecutar_consulta(query, results, index, thread_id):
    connection = None
    cursor = None
    start_time = time.time()
    try:
        connection = get_connection()
        if connection is None:
            results[index][thread_id] = ("Error de conexión", 0)
            return
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.fetchall()
        end_time = time.time()
        elapsed_time = end_time - start_time
        results[index][thread_id] = (query, elapsed_time)
    except pyodbc.Error as e:
        results[index][thread_id] = (f"Error: {e}", 0)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def comparar_consultas(queries, num_threads):
    results = [[None] * num_threads for _ in range(len(queries))]
    
    def worker(query, index, thread_id):
        ejecutar_consulta(query, results, index, thread_id)
    
    for i, query in enumerate(queries):
        threads = []
        for thread_id in range(num_threads):
            thread = threading.Thread(target=worker, args=(query, i, thread_id))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
    
    return results

def get_fixed_queries():
    return [
        "SELECT * FROM CUIDADOR",
        "SELECT * FROM CURSO",
        "SELECT * FROM HORARIO",
        "SELECT * FROM MATRICULA",
        "SELECT * FROM TUTOR"
    ]
