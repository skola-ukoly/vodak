class Uzivatel:
    def __init__(self, nick: str, je_plavec: bool, kamarad_do_lode: str | None):
        self.nick = nick
        self.je_plavec = je_plavec
        self.kamarad_do_lode = kamarad_do_lode