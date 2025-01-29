class Nepritel:
    def __init__(self, rychlost_pozadi, poloha_x, poloha_y, šířka, výška, vystrel):
        self.rychlost_pozadi = rychlost_pozadi
        self.sirka = šířka
        self.vyska = výška
        self.poloha_y = poloha_y
        self.poloha_x = poloha_x  # Oprava: Použití správné proměnné
        self.vystrel = vystrel

    def pohyb_kanonu(self):
        self.poloha_x -= self.rychlost_pozadi
    
    def nabíjení(self):
        vzdalenost_pred_vystrelem = self.sirka
        vzdalenost_pred_vystrelem -= self.sirka * 1 / 5
        vzdalenost_pred_vystrelem = vzdalenost_pred_vystrelem / 3
        vzdalenost_pred_vystrelem1 = vzdalenost_pred_vystrelem + self.sirka * 1 / 5
        vzdalenost_pred_vystrelem2 = vzdalenost_pred_vystrelem * 2 + self.sirka * 1 / 5
        
        if self.poloha_x > vzdalenost_pred_vystrelem2:
            self.vystrel = 1
        elif self.poloha_x > vzdalenost_pred_vystrelem1:
            self.vystrel = 2
        elif self.poloha_x > self.sirka * 1 / 5:
            self.vystrel = 3
        elif self.poloha_x-100 < self.sirka * 1 / 5 and self.poloha_x+50 > self.sirka * 1 / 5:
            self.vystrel = 4
        elif self.poloha_x + 200 > 0:
            self.vystrel = 5
        else:
            self.vystrel = 0
