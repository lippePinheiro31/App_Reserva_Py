import sqlite3

def criar_banco():
    conn = sqlite3.connect("reservas.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS salas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE NOT NULL
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reservas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sala_id INTEGER NOT NULL,
        usuario_id INTEGER NOT NULL,
        data TEXT NOT NULL,
        inicio TEXT NOT NULL,
        fim TEXT NOT NULL,
        FOREIGN KEY (sala_id) REFERENCES salas(id),
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    )""")

    conn.commit()
    conn.close()
