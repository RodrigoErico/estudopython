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


class EventoOnline(Evento):
    def __init__(self, nome, _=""):  # _="" parametro ignorado
        local = f"https://tamarcado.com/eventos?id={EventoOnline.id}"
        # Evento.__init__(self, nome, local)
        super().__init__(nome, local)

    def imprime_informacao(self):
        print(f"ID do evento:{self.id}")
        print(f"Nome do evento: {self.nome}")
        print(f"Link para acessar o evento: {self.local}")
        print("---------------")


ev_online = EventoOnline("Live de python")
ev2_online = EventoOnline("Live de Javascript")
ev_online.imprime_informacao()
ev2_online.imprime_informacao()

ev = Evento("Aula de python", "Cuiaba")
ev.imprime_informacao()
