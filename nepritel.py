class Nepritel:
    def __init__(self,rychlost_pozadi,poloha_x,poloha_y,šířka, výška,vystrel):
        self.rychlost_pozadi = rychlost_pozadi
        self.sirka = šířka
        self.vyska = výška
        self.poloha_y = poloha_y
        self.poloha_x = šířka
        self.vystrel = vystrel
    def pohyb_kanonu(self):
        self.poloha_x -= self.rychlost_pozadi