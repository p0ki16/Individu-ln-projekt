# Importy a inicializace
import pygame
import sys
import random
import math

from strela import Strela,Raketa
from letadlo import Letadlo
from nepritel import Nepritel
from Shop import Shop    


pygame.font.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 48)


text_color = (0, 0, 0)



firerate = 0


# Inicializace proměnných
angle_kanon = 180
pohyb_pozadí = 0
rozdil_pozadi = 1920
výška, šířka = 1080, 1920
hrac_x = šířka * 1 / 5
hrac_y = výška / 2

zivoty = 5
zivoty_nepritel = 20
uhel = 1

smrt = False
raketa_vystrelena =0
vystrel = 0
speed_strela = 5
rychlost_pozadi = 10
poloha_x = šířka
poloha_y = výška - 210
firerate_rakety =0
vystreleni = []
raketa_vystrel =[]
pocet_raket=12
skore=0


# Inicializace Pygame
obrazovka = pygame.display.set_mode((šířka, výška))
pygame.display.set_caption("zkouška")
pozadi_barva = (100, 100, 255)
loading_screen = pygame.image.load("loading_screen.png")
obrazovka.blit(loading_screen,(0,0))

pygame.display.flip()


# Načtení obrázků

Raketa_image = pygame.image.load('Raketa.png')


Pohyblive_pozadi = pygame.image.load("Pozadí_pohyblivé.png")

kanon13 = pygame.image.load("kanon_1l3.png")
kanon23 = pygame.image.load("kanon_2l3.png")
kanon33 = pygame.image.load("kanon_3l3.png")
kanon43 = pygame.image.load("kanon_4l3.png")

kanon_destroyed = pygame.image.load("kanon_destroyed.png")

strela_image = pygame.image.load("strela.png")
vybuch_image = pygame.image.load("výbuch_strely.png")

beam3l3 = pygame.image.load("beam.png")
vybuch = pygame.image.load("výbuch.png")

Lobby_image = pygame.image.load("Lobby.png")

Button_leave = pygame.image.load("Button_back.png")


button_play = pygame.image.load("button_play.png")  
pozice_play = button_play.get_rect(topleft=(600, 100))

button_shop = pygame.image.load("button_shop.png")  
pozice_shop= button_shop.get_rect(topleft=(600, 200))

button_infinity = pygame.image.load("button_infinity.png")  
pozice_infinity = button_infinity.get_rect(topleft=(600, 300))

button_rockets = pygame.image.load("Shop_Button_Rockets.png")  
pozice_rockets = button_rockets.get_rect(topleft=(1250, 50))

button_planes = pygame.image.load("Shop_Button_planes.png")  
pozice_planes= button_planes.get_rect(topleft=(1250, 200))

button_upgrades = pygame.image.load("Shop_Button_upgrades.png")  
pozice_upgrades = button_upgrades.get_rect(topleft=(1250, 350))

shop_image = pygame.image.load("Shop.png")

fockerfox = pygame.image.load("Fockerfox.png")
fockerfox13=pygame.image.load("Fockerfox13.png")
fockerfox23=pygame.image.load("Fockerfox23.png")
fockerfox33=pygame.image.load("Fockerfox33.png")
fockerfox_button=pygame.image.load("Button_Fockerfox.png")
pozice1 =  fockerfox_button.get_rect(topleft=(200, 878))

myg = pygame.image.load("MYG-15.png")
myg13 = pygame.image.load("myg13.png")
myg23=pygame.image.load("myg23.png")
myg33=pygame.image.load("myg33.png")
myg_button=pygame.image.load("Button_Myg.png")
pozice2 =  myg_button.get_rect(topleft=(200, 744))

f=pygame.image.load("E-23.png")
f13=pygame.image.load("f13.png")
f23=pygame.image.load("f23.png")
f33=pygame.image.load("f33.png")
fbutton = pygame.image.load("Button_F23.png")
pozice3 =  fbutton.get_rect(topleft=(200, 615))


fockerfox_animace=[fockerfox13,fockerfox23,fockerfox33]
myg_animace=[myg13 ,myg23,myg33]
f_animace=[f13,f23,f33]

main_buttony = {
    "letadla":button_planes,
    "pozice_letadla":pozice_planes,
    
    "rakety": button_rockets,
    "pozice_rakety":pozice_rockets,
    
    "upgrady":button_upgrades,
    "pozice_upgrady":pozice_upgrades,
    
    "myg25":myg,
    "fockerfox":fockerfox,
    "F23": f,
    
    "myg_button":myg_button,
    "f_button":fbutton,
    "fockerfox_button":fockerfox_button,
    
    "pozice_buttonu1":pozice1,
    "pozice_buttonu2":pozice2,
    "pozice_buttonu3":pozice3,
    

    }






Lobby = True
Infinite_mode = False 
shop = False 



# Vytvoření instancí tříd
letadlo = Letadlo(hrac_x, hrac_y, šířka, výška, zivoty, uhel, smrt, 0, 0, vystrel, angle_kanon)
nepritel = Nepritel(rychlost_pozadi, poloha_x, poloha_y, šířka, výška, vystrel, zivoty_nepritel, obrazovka, zivoty)
Obchod = Shop(main_buttony,shop_image)
while True:
    
    while Lobby:
        
        for udalost in pygame.event.get():
            
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if udalost.type == pygame.MOUSEBUTTONDOWN:
                
                if pozice_play.collidepoint(udalost.pos):  # Kontrola, zda kliknutí bylo na obrázku tlačítka
                    Lobby = False
                    play=True
                    
                if pozice_shop.collidepoint(udalost.pos):  # Kontrola, zda kliknutí bylo na obrázku tlačítka
                    Lobby = False
                    shop = True
                    
                if pozice_infinity.collidepoint(udalost.pos):  # Kontrola, zda kliknutí bylo na obrázku tlačítka
                    Lobby = False
                    Infinite_mode = True
                    
        umisteni_pozadi1 = pohyb_pozadí % rozdil_pozadi
        umisteni_pozadi2 = (pohyb_pozadí % rozdil_pozadi) - rozdil_pozadi
        
         # Vypočítej ofset od středu obrázku k pravému hornímu rohu
        
        
        
        
        
        # Poté vyplníme pozadí
        obrazovka.fill(pozadi_barva)
        obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi1, výška - 100))
        obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi2, výška - 100))
        
        # Vykreslíme ostatní obrázky (např. pozadí Lobby)
        obrazovka.blit(Lobby_image, (-20, 0))
        # Nejprve vykreslíme tlačítka
        obrazovka.blit(button_play, pozice_play)
        obrazovka.blit(button_shop, pozice_shop)
        obrazovka.blit(button_infinity, pozice_infinity)

        # Aktualizace obrazovky
        pygame.display.flip()
        
        # Nastavení FPS
        clock.tick(60)
        
    while shop:
        
        for udalost in pygame.event.get():
    
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        white = (255,255,255)    
        obrazovka.fill( white )        
        Obchod.draw_shop(obrazovka)
        Obchod.choose(udalost,obrazovka)
        Obchod.opustit_shop(obrazovka,Button_leave,udalost)
        
        shop = Obchod.shop
        Lobby = Obchod.lobby
        
        
        
        
        
        
        
        
        pygame.display.flip()
        
        # Nastavení FPS
        clock.tick(60)
    
            
        
        
        

        
    while Infinite_mode:
        
        text = f" skóre: {skore} počet raket :{pocet_raket} životy:{nepritel.zivoty} "
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(500, 50))
        
        
        for i in range(vystrel):
            strela_x = letadlo.x + 17
            strela_y = letadlo.y + 17
            zasazeni = False
            strela = Strela(strela_x, strela_y, letadlo.uhel, zasazeni)
            vystreleni.append(strela)
            
        for j in range(raketa_vystrelena):
            Raketa_x = letadlo.x
            Raketa_y = letadlo.y
            zasazeni = False
            raketa = Raketa(Raketa_x, Raketa_y, zasazeni)
            raketa_vystrel.append(raketa)
            
            
        for udalost in pygame.event.get():
                if udalost.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        if letadlo.y > 1080:
            nepritel.zivoty=0
          
        
        if nepritel.zivoty <= 0:
                letadlo.znic_se(Lobby,Infinite_mode)
        else:       
        
            
            
           
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                letadlo.pohyb_dolu(Obchod.obratnost)
        
            letadlo.pohyb_jiným_směrem()
            
            if firerate > 0:  # Delay mezi střelami
                firerate -= 1
                
            if firerate_rakety > 0:  # Delay mezi raketami
                firerate_rakety -= 1
                
            vystrel = 0    
            if keys[pygame.K_SPACE] and firerate == 0:
                firerate = Obchod.firerate  # Nastavení hodnoty delay
                vystrel = 1
                
            raketa_vystrelena = 0
            
            if keys[pygame.K_LALT] and firerate_rakety == 0 and pocet_raket>0:
                firerate_rakety = 100  # Nastavení hodnoty delay
                raketa_vystrelena = 1
                pocet_raket-=1
            
            if keys[pygame.K_UP]:
                letadlo.pohyb_nahoru(Obchod.obratnost)
            nepritel.rychlost_pozadi =6   #počítání pohybu pod úhlem
            
            if 270>letadlo.uhel and letadlo.uhel  < 90:   
                nepritel.rychlost_pozadi =-nepritel.rychlost_pozadi * math.sin(math.radians(letadlo.uhel-90))#90je zde k pootočení osy
                
            else:
                nepritel.rychlost_pozadi =-nepritel.rychlost_pozadi * math.sin(math.radians(letadlo.uhel-90))
                
            
        
        
            
            
        if letadlo.smrt == False:  # Kontrola jestli letadlo žije
            nepritel.pohyb_kanonu()
            pohyb_pozadí -= nepritel.rychlost_pozadi
            umisteni_pozadi1 = pohyb_pozadí % rozdil_pozadi
            umisteni_pozadi2 = (pohyb_pozadí % rozdil_pozadi) - rozdil_pozadi
            
        
            
        
       

        obrazovka.fill(pozadi_barva)
        obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi1, výška - 100))
        obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi2, výška - 100))
        
        nepritel.nabíjení(obrazovka, kanon13, kanon23, kanon33 , kanon43, beam3l3,kanon_destroyed)
       
        for strela in vystreleni:
            
            if strela.zasazeni == False :
                
                strela.zasah(nepritel)
            strela.move( nepritel.rychlost_pozadi)
            strela.draw(obrazovka, strela_image, vybuch_image,vybuch)
            
        for raketa in raketa_vystrel:
            
            if raketa.zasazeni == False:
                raketa.zasah(nepritel)
            raketa.navádění(nepritel,obrazovka,Raketa_image,výška,nepritel.rychlost_pozadi)
            raketa.draw(obrazovka, Raketa_image, vybuch_image,vybuch, nepritel.rychlost_pozadi)
            
        if nepritel.zivoty_self > 0:
            pricteni =True
            
        if nepritel.zivoty_self < 0 and pricteni ==True:
            skore+=1000
            pricteni =False
    
                
            
                
        
        Obchod.animace(fockerfox_animace,f_animace,myg_animace)
        otočená_stíhačka = pygame.transform.rotate(Obchod.letadlo, letadlo.uhel)
            

        rect = otočená_stíhačka.get_rect(center=(letadlo.x, letadlo.y))
        obrazovka.blit(otočená_stíhačka, rect.topleft)
        obrazovka.blit(text_surface, text_rect)
        
        letadlo.neutíkej()
        pygame.display.flip()
        clock.tick(60)

        
