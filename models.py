class Sala:
    def __init__(self, nome, id=None):
        self.id = id
        self.nome = nome

class Usuario:
    def __init__(self, nome, email, id=None):
        self.id = id
        self.nome = nome
        self.email = email

class Reserva:
    def __init__(self, sala_id, usuario_id, data, inicio, fim, id=None):
        self.id = id
        self.sala_id = sala_id
        self.usuario_id = usuario_id
        self.data = data
        self.inicio = inicio
        self.fim = fim
