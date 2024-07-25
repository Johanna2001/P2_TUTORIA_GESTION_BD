import pyodbc

# Configura tu conexión
server = 'SANDY-CQ11\SJCQ11'  # El nombre del servidor o la dirección IP
database = 'Kinder_Parcial2'  # El nombre de tu base de datos
username = 'SANDY-CQ11\1116'  # Tu nombre de usuario
password = 'Sandy1116'  # Tu contraseña
try:
    connection = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}; Trusted_Connection=yes'
    )
    print("Conexión exitosa")
    connection.close()
except pyodbc.Error as e:
    print(f"Error al conectar a la base de datos: {e}")
