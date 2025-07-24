import sqlite3
from models import Sala, Usuario, Reserva

class SistemaReservas:
    def __init__(self, db_path="reservas.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def adicionar_sala(self, sala: Sala):
        try:
            self.cursor.execute("INSERT INTO salas (nome) VALUES (?)", (sala.nome,))
            self.conn.commit()
        except sqlite3.IntegrityError:
            pass

    def listar_salas(self):
        self.cursor.execute("SELECT id, nome FROM salas")
        return [Sala(id=row[0], nome=row[1]) for row in self.cursor.fetchall()]

    def adicionar_usuario(self, usuario: Usuario):
        try:
            self.cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (usuario.nome, usuario.email))
            self.conn.commit()
        except sqlite3.IntegrityError:
            pass

    def listar_usuarios(self):
        self.cursor.execute("SELECT id, nome, email FROM usuarios")
        return [Usuario(id=row[0], nome=row[1], email=row[2]) for row in self.cursor.fetchall()]

    def verificar_conflito(self, sala_id, data, inicio, fim):
        query = """
        SELECT COUNT(*) FROM reservas WHERE sala_id = ? AND data = ?
          AND NOT (fim <= ? OR inicio >= ?)
        """
        self.cursor.execute(query, (sala_id, data, inicio, fim))
        count = self.cursor.fetchone()[0]
        return count > 0

    def adicionar_reserva(self, reserva: Reserva):
        if self.verificar_conflito(reserva.sala_id, reserva.data, reserva.inicio, reserva.fim):
            return False
        self.cursor.execute(
            "INSERT INTO reservas (sala_id, usuario_id, data, inicio, fim) VALUES (?, ?, ?, ?, ?)",
            (reserva.sala_id, reserva.usuario_id, reserva.data, reserva.inicio, reserva.fim)
        )
        self.conn.commit()
        return True

    def listar_reservas(self, data=None):
        if data:
            self.cursor.execute("""
            SELECT r.id, s.nome, u.nome, r.data, r.inicio, r.fim
            FROM reservas r
            JOIN salas s ON r.sala_id = s.id
            JOIN usuarios u ON r.usuario_id = u.id
            WHERE r.data = ?
            ORDER BY r.inicio
            """, (data,))
        else:
            self.cursor.execute("""
            SELECT r.id, s.nome, u.nome, r.data, r.inicio, r.fim
            FROM reservas r
            JOIN salas s ON r.sala_id = s.id
            JOIN usuarios u ON r.usuario_id = u.id
            ORDER BY r.data, r.inicio
            """)
        return self.cursor.fetchall()

    def cancelar_reserva(self, reserva_id):
        self.cursor.execute("DELETE FROM reservas WHERE id = ?", (reserva_id,))
        self.conn.commit()
