class Evento:
    id = 1

    def __init__(self, nome, local=""):
        self.nome = nome
        self.local = local
        self.id = Evento.id
        Evento.id += 1

    def imprime_informacao(self):
        print("ID do evento:", self.id)
        print("Nome do evento:", self.nome)
        print("Local do evento:", self.local)

    @classmethod
    def cria_evento_online(cls, nome):
        evento = cls(nome, local=f"htttps://tamarcado.com/eventos?id={cls.id}")
        return evento

    @staticmethod
    def calcula_limite_pessoas_area(area):
        if 5 <= area < 10:
            return 5
        elif 10 <= area < 20:
            return 15
        elif area >= 20:
            return 30
        else:
            return 0


ev_online = Evento.cria_evento_online("Live de python")
ev2_online = Evento.cria_evento_online("Live de Javascript")
ev_online.imprime_informacao()
ev2_online.imprime_informacao()

print(ev2_online.id)
print(Evento.id)