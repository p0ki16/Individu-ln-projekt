class Letadlo:
    def __init__(self, hrac_x, hrac_y, šířka, výška, zivoty, uhel):
        self.sirka = šířka
        self.vyska = výška
        self.x = hrac_x if hrac_x is not None else šířka * 1 / 4
        self.y = hrac_y if hrac_y is not None else výška / 2
        self.zivoty = zivoty
        self.uhel = uhel

    def pohyb_dolu(self):
        if self.y < self.vyska - 50:
            self.y += 10

    def pohyb_nahoru(self):
        if self.y > 0:
            self.y -= 10
            
    def znic_se(self):
        if self.uhel > -50:
            self.uhel -=1
            self.y += 10
        
        
                
        