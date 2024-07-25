import pyodbc
from tkinter import messagebox

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

def listar_entidades():
    connection = None
    cursor = None
    entities = {}
    try:
        connection = get_connection()
        if connection is None:
            return entities
        cursor = connection.cursor()
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
        tables = [row[0] for row in cursor.fetchall()]
        for table in tables:
            cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}'")
            columns = [row[0] for row in cursor.fetchall()]
            entities[table] = columns
    except pyodbc.Error as e:
        print(f"Error al listar entidades y atributos: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return entities

def tabla_existe(table_name):
    connection = None
    cursor = None
    exists = False
    try:
        connection = get_connection()
        if connection is None:
            return exists
        cursor = connection.cursor()
        cursor.execute(f"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{table_name}'")
        exists = cursor.fetchone() is not None
    except pyodbc.Error as e:
        print(f"Error al verificar la existencia de la tabla: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return exists

def crear_tabla_auditoria():
    connection = None
    cursor = None
    try:
        connection = get_connection()
        if connection is None:
            return
        cursor = connection.cursor()

        if tabla_existe("AUDITORIA"):
            confirm = messagebox.askyesno("Confirmación", "La tabla 'Auditoria' ya existe. ¿Desea reemplazarla?")
            if not confirm:
                return

            # Eliminar la tabla si ya existe
            cursor.execute("DROP TABLE IF EXISTS AUDITORIA")

        # Crear la tabla de auditoría
        cursor.execute("""
        CREATE TABLE AUDITORIA (
            AUDITORIA_ID INT IDENTITY(1,1) PRIMARY KEY,
            AUDITORIA_TABLAAFECTADA NVARCHAR(100),
            AUDITORIA_FECHA DATETIME,
            AUDITORIA_USUARIO NVARCHAR(50),
            AUDITORIA_DETALLE NVARCHAR(200)
        )
        """)
        connection.commit()
        messagebox.showinfo("Éxito", "Tabla de auditoría creada correctamente.")
    except pyodbc.Error as e:
        messagebox.showerror("Error", f"Error al crear la tabla de auditoría: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def generar_triggers(entities):
    try:
        connection = get_connection()
        if connection is None:
            return
        cursor = connection.cursor()

        for entity in entities:
            triggers = {
                "INSERT": f"""
                CREATE TRIGGER trg_audit_{entity}_ins
                ON {entity}
                AFTER INSERT
                AS
                BEGIN
                    INSERT INTO AUDITORIA (AUDITORIA_TABLAAFECTADA, AUDITORIA_FECHA, AUDITORIA_USUARIO, AUDITORIA_DETALLE)
                    VALUES ('{entity}', GETDATE(), SYSTEM_USER, 'INSERT');
                END;""",
                "UPDATE": f"""
                CREATE TRIGGER trg_audit_{entity}_upd
                ON {entity}
                AFTER UPDATE
                AS
                BEGIN
                    INSERT INTO AUDITORIA (AUDITORIA_TABLAAFECTADA, AUDITORIA_FECHA, AUDITORIA_USUARIO, AUDITORIA_DETALLE)
                    VALUES ('{entity}', GETDATE(), SYSTEM_USER, 'UPDATE');
                END;""",
                "DELETE": f"""
                CREATE TRIGGER trg_audit_{entity}_del
                ON {entity}
                AFTER DELETE
                AS
                BEGIN
                    INSERT INTO AUDITORIA (AUDITORIA_TABLAAFECTADA, AUDITORIA_FECHA, AUDITORIA_USUARIO, AUDITORIA_DETALLE)
                    VALUES ('{entity}', GETDATE(), SYSTEM_USER, 'DELETE');
                END;"""
            }

            # Ejecutar los disparadores
            for trigger_sql in triggers.values():
                cursor.execute(trigger_sql)

            print(f"Disparadores para {entity} creados.")

        connection.commit()
        messagebox.showinfo("Éxito", "Disparadores de auditoría generados correctamente.")
    except pyodbc.Error as e:
        messagebox.showerror("Error", f"No se pudieron generar los disparadores: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
