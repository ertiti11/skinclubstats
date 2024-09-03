import sqlite3, os
from utils import getAllCaseNames

def fetch_old_data(cursor, case):
    """Obtiene los datos de la tabla de la base de datos antigua."""
    query = f"""
    SELECT 
        price, 
        profit_chance, 
        profit_chanceX1dot5, 
        profit_chanceX2,
        profit_chanceX3,
        profit_chanceX10,
        real_price, 
        ev, 
        irb  
    FROM "{case}"
    """
    cursor.execute(query)
    return cursor.fetchall()

def insert_new_data(cursor, case_name, data):
    """Inserta los datos en la nueva base de datos."""
    query = """
    INSERT INTO cases 
    (case_name, price, profit_chance, profit_chanceX1dot5, profit_chanceX2, profit_chanceX3, 
    profit_chanceX10, real_price, ev, irb) 
    VALUES (?,?,?,?,?,?,?,?,?,?)
    """
    rows_to_insert = [(case_name,) + row for row in data]
    cursor.executemany(query, rows_to_insert)

def casenames_to_new_db():
    """Convierte los datos de la antigua base de datos a la nueva."""
    casenames = getAllCaseNames()

    with sqlite3.connect("./skin.sqlite") as old_conn, \
         sqlite3.connect("../skins_database.sqlite") as new_conn:
        
        old_cursor = old_conn.cursor()
        new_cursor = new_conn.cursor()

        for case in casenames:
            data = fetch_old_data(old_cursor, case)
            insert_new_data(new_cursor, case, data)

        new_conn.commit()

def get_all_skins():
    """obtiene todas las skins de la antigua base de datos y verifica que sean unicas en su nombre y las mete en la nueva base de datos"""
    casenames = getAllCaseNames()

    with sqlite3.connect("./skin.sqlite") as old_conn, \
         sqlite3.connect("../skins_database.sqlite") as new_conn:
        
        old_cursor = old_conn.cursor()
        new_cursor = new_conn.cursor()

        for casename in casenames:
            query = """
            SELECT 
                name, 
                price, 
                rarity, 
                finish
            
            FROM {casename}Weapons
            """
            old_cursor.execute(query)
            rows = old_cursor.fetchall()

            query = """
            INSERT INTO skins 
            (name, price, rarity, case_name, case_price, case_profit_chance, case_profit_chanceX1dot5, 
            case_profit_chanceX2, case_profit_chanceX3, case_profit_chanceX10, case_real_price, case_ev, case_irb) 
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """
            rows_to_insert = list(set(rows))
            new_cursor.executemany(query, rows_to_insert)
            new_conn.commit()




def create_db():
    delete_old = input("¿Quieres borrar la base de datos antigua? (y/n): ")
    if delete_old == "y":
        os.remove("../skins_database.sqlite")
    elif delete_old == "n":
        pass

    # Conectar a la base de datos (esto crea el archivo si no existe)
    conn = sqlite3.connect('../skins_database.sqlite')

    # Crear un cursor para ejecutar comandos SQL
    cursor = conn.cursor()

    # Leer el archivo SQL y ejecutar sus contenidos
    with open('../newdb.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    # Ejecutar el script SQL
    cursor.executescript(sql_script)

    # Confirmar los cambios
    conn.commit()

    # Cerrar la conexión
    conn.close()

    print("Base de datos y tablas creadas con éxito.")

def main_menu():
    while True:
        print("\n===== Menú Principal =====")
        print("1. Crear la base de datos")
        print("2. Migrar todas las cajas")
        print("0. Salir")
        
        choice = input("Selecciona una opción: ")
        
        if choice == '1':
            create_db()
        elif choice == '2':
            casenames_to_new_db()
            print("Migración completada con éxito.")
        elif choice == '0':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

# Ejecutar el menú principal
if __name__ == "__main__":
    main_menu()
