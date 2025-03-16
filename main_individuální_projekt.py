     # Importy a inicializace
# health bar zvírasznění powerupů!
import pygame
import sys
import random
import math

from strela import Strela,Raketa
from letadlo import Letadlo,Powerup
from nepritel import Nepritel_zem,Nepritel_vzduch
from Shop import Shop    


pygame.font.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 48)
barva =0
delay_do_konce=1
text_color = (0, 0, 0)

obrazek_y=0
obrazek_x=620
bomba_y = 0
firerate = 0


# Inicializace proměnných
angle_kanon = 180
pohyb_pozadí = 0
rozdil_pozadi = 1920
výška, šířka = 1080, 1920
hrac_x = šířka * 1 / 5
hrac_y = výška / 2

zivoty = 6
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


# Inicializace Pygame
obrazovka = pygame.display.set_mode((šířka, výška))
pygame.display.set_caption("zkouška")
pozadi_barva = (20, 150, 255)
loading_screen = pygame.image.load("loading_screen.png")
obrazovka.blit(loading_screen,(0,0))

pygame.display.flip()


# Načtení obrázků
 #___________________________________________________________________________________________________________________________________________________________________________________________________________________
raketa_image11 = pygame.image.load('Raketa11.png')
raketa_image12 = pygame.image.load('Raketa12.png')


atom = pygame.image.load('atom_výbuch.png')
pozadí = pygame.image.load("pozadí.png")
Pohyblive_pozadi = pygame.image.load("Pozadí_pohyblivé.png")
bomba_image = pygame.image.load("bomba.png")
kanon13 = pygame.image.load("kanon_1l3.png")
kanon23 = pygame.image.load("kanon_2l3.png")
kanon33 = pygame.image.load("kanon_3l3.png")
kanon43 = pygame.image.load("kanon_4l3.png")

kanon_destroyed = pygame.image.load("kanon_destroyed.png")

strela_image = pygame.image.load("strela.png")
strela_image2 = pygame.image.load("strela2.png")

vybuch_image = pygame.image.load("výbuch_strely.png")

beam3l3 = pygame.image.load("beam.png")
vybuch = pygame.image.load("výbuch.png")

Lobby_image = pygame.image.load("Lobby.png")
wintext = pygame.image.load("win_text.png")

Button_leave = pygame.image.load("Button_back.png")

bar =pygame.image.load("bar.png")
health_bar =pygame.image.load("health_bar.png")
bar_raketa = pygame.image.load("Raketa.png")
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

raketa21 = pygame.image.load("Raketa21.png")
raketa22 = pygame.image.load("Raketa22.png")

raketa31 = pygame.image.load("Raketa31.png")
raketa32 = pygame.image.load("Raketa32.png")

raketa_shop1=pygame.image.load("Raketa_shop.png")
raketa_shop2=pygame.image.load("Raketa3_shop.png")
raketa_shop3=pygame.image.load("Shop_Shark.png")

button_raketa1 =pygame.image.load("Button_shop_raketa1.png")
button_raketa2 =pygame.image.load("Button_shop_raketa3.png")
button_raketa3 =pygame.image.load("Button_Shark.png")

bomber11 =pygame.image.load("bomber12.png")
bomber12 =pygame.image.load("bomber22.png")

powerup_image = pygame.image.load("powerup.png")
shield = pygame.image.load("štít.png")
enemy_base = pygame.image.load("enemy_base.png")
xskóre = pygame.image.load("2xskóre.png")
firerate_boom1 = pygame.image.load("firerate_boom1.png")
firerate_boom2 = pygame.image.load("firerate_boom2.png")
health_power_up = pygame.image.load("health_power_up.png")
health_bar2 = pygame.image.load("health_bar2.png")
health_bar2x = -1000
health_bar2y = 0
 #___________________________________________________________________________________________________________________________________________________________________________________________________________________



fockerfox_animace=[fockerfox13,fockerfox23,fockerfox33]
myg_animace=[myg13 ,myg23,myg33]
f_animace=[f13,f23,f33]

Raketa1=[raketa_image11,raketa_image12,raketa_image12]
Raketa3=[raketa21,raketa22,raketa22]
Raketa2=[raketa31,raketa32,raketa32]

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
    
    "raketa1":raketa_shop1,
    "raketa2":raketa_shop2,
    "raketa3":raketa_shop3,

    "raketa11":Raketa1,
    "raketa22":Raketa2,
    "raketa33":Raketa3,
    
    "myg_button":myg_button,
    "f_button":fbutton,
    "fockerfox_button":fockerfox_button,
    
    "r_b_1":button_raketa1,
    "r_b_2":button_raketa2,
    "r_b_3":button_raketa3,

    
    "pozice_buttonu1":pozice1,
    "pozice_buttonu2":pozice2,
    "pozice_buttonu3":pozice3,
    

    }




nep_vz_x =500 
nep_vz_y =500
 
Lobby = True
Infinite_mode = False 
shop = False 
play=False


#y Vytvoření instancí tříd
letadlo = Letadlo(hrac_x, hrac_y, šířka, výška, 6, uhel, smrt, 0, 0, vystrel, angle_kanon)
nepritel = Nepritel_zem(rychlost_pozadi, poloha_x, poloha_y, šířka, výška, vystrel, zivoty_nepritel, obrazovka, zivoty)
Obchod = Shop(main_buttony,shop_image)
vznepritel1 = Nepritel_vzduch(600,500,30,bomber11,bomber12)
vznepritel2 = Nepritel_vzduch(300,500,30,bomber11,bomber12)
powerup = Powerup(powerup_image)

while True:
    gained_money=letadlo.skore/10
    Obchod.peníze+=gained_money
    
    while Lobby:
       
        text = f" money: {Obchod.peníze} "
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(500, 50))
        
        for udalost in pygame.event.get():
            
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if udalost.type == pygame.MOUSEBUTTONDOWN:
                
               if pozice_play.collidepoint(udalost.pos):  # Kontrola, zda kliknutí bylo na obrázku tlačítka
                   Lobby = False
                   play=True
                   letadlo.reset(nepritel,vznepritel1,vznepritel2,Obchod.zivoty)
                   pohyb_pozadí=0
                   mise= random.randint(1,2)
                   base_x = 3000
                   bomba = 0
                   bomba_y =0  
                   delay_do_konce=1
                   health_bar2x = -1000
               if pozice_shop.collidepoint(udalost.pos):  # Kontrola, zda kliknutí bylo na obrázku tlačítka
                    Lobby = False
                    shop = True
                    letadlo.reset(nepritel,vznepritel1,vznepritel2,Obchod.zivoty)
                    pohyb_pozadí=0
            
               if pozice_infinity.collidepoint(udalost.pos):  # Kontrola, zda kliknutí bylo na obrázku tlačítka
                    Lobby = False
                    Infinite_mode = True
                    letadlo.reset(nepritel,vznepritel1,vznepritel2,nepritel.zivoty)
                    pohyb_pozadí=0
                    base_x = 3000
                    bomba = 0
                    delay_do_konce=1
                    health_bar2x = -1000
        
        
                   
        umisteni_pozadi1 = pohyb_pozadí % rozdil_pozadi
        umisteni_pozadi2 = (pohyb_pozadí % rozdil_pozadi) - rozdil_pozadi
        plane_lobby_pozice = 724,850
        
        
        
        
         # Vypočítej ofset od středu obrázku k pravému hornímu rohu
        
        
        
        
        # Poté vyplníme pozadí

        obrazovka.fill(pozadi_barva)
        obrazovka.blit(pozadí,(0,558))
        
        obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi1, výška - 100))
        obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi2, výška - 100))
        
        # Vykreslíme ostatní obrázky (např. pozadí Lobby)
        obrazovka.blit(Lobby_image, (-20, 0))
        # Nejprve vykreslíme tlačítka
        obrazovka.blit(button_play, pozice_play)
        obrazovka.blit(button_shop, pozice_shop)
        obrazovka.blit(button_infinity, pozice_infinity)
        obrazovka.blit( Obchod.animace(fockerfox_animace,f_animace,myg_animace,1), plane_lobby_pozice)
        obrazovka.blit(text_surface, text_rect)

        # Aktualizace obrazovky
        pygame.display.flip()
        
        # Nastavení FPS
        clock.tick(60)
        
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
    while play:
        text = f" SKÓRE: {letadlo.skore}                            :{letadlo.pocet_raket} "
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(300, 110))
        
        
        
        for i in range(vystrel):
            strela_x = letadlo.x + 17
            strela_y = letadlo.y + 17
            zasazeni = False
            strela = Strela(strela_x, strela_y, letadlo.uhel, zasazeni,strela_image,25,1)
            
            if powerup.co_padlo == 2:
                   
                     
                    strela = 0
                    strela = Strela(strela_x, strela_y, letadlo.uhel, zasazeni,strela_image2,25,5)
            vystreleni.append(strela)
        vystrel = 0 
          
        #
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
            
        if powerup.odpočet >0 and powerup.zivoty !=0:
            
            nepritel.zivoty  =powerup.zivoty
        
        if nepritel.zivoty >= 1:
                

            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                letadlo.pohyb_dolu(Obchod.obratnost)
        
            letadlo.pohyb_jiným_směrem()
            
            if firerate > 0:  # Delay mezi střelami
                firerate -= 1
                
            if firerate_rakety > 0:  # Delay mezi raketami
                firerate_rakety -= 1
                
             
            if keys[pygame.K_SPACE] and firerate == 0:
                firerate = Obchod.firerate * powerup.firerate  # Nastavení hodnoty delay
                vystrel = 1

                
            raketa_vystrelena = 0
            
            if keys[pygame.K_LALT] and firerate_rakety == 0 and letadlo.pocet_raket>0:
                firerate_rakety = 100  # Nastavení hodnoty delay
                raketa_vystrelena = 1
                letadlo.pocet_raket-=1
            
            if keys[pygame.K_UP]:
                letadlo.pohyb_nahoru(Obchod.obratnost)
            nepritel.rychlost_pozadi =Obchod.rychlost #očítání pohybu pod úhlem
            
               
            nepritel.rychlost_pozadi =-nepritel.rychlost_pozadi * math.sin(math.radians(letadlo.uhel-90))#90je zde k pootočení osy
                           
        else:
            letadlo.znic_se(Lobby,Infinite_mode)
            if  letadlo.znic_se(Lobby,Infinite_mode):
                Lobby = True
                play = False 
                vystreleni=[]   
        if letadlo.smrt == False:  # Kontrola jestli letadlo žije
            nepritel.pohyb_kanonu()
            pohyb_pozadí -= nepritel.rychlost_pozadi
            umisteni_pozadi1 = pohyb_pozadí % rozdil_pozadi
            umisteni_pozadi2 = (pohyb_pozadí % rozdil_pozadi) - rozdil_pozadi
        
        
        obrazovka.fill(pozadi_barva)
        obrazovka.blit(pozadí,(0,558))
        obrazovka.blit(bar,(abs(pohyb_pozadí)/25,50))
        obrazovka.blit(health_bar2,(health_bar2x,health_bar2y))
        obrazovka.blit(health_bar,(nepritel.zivoty*100-1920,0))
        if nepritel.zivoty*100-1920 < health_bar2x:
            health_bar2x-=3
        
        obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi1, výška - 100))
        obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi2, výška - 100))
        
        if mise ==1 and pohyb_pozadí > -38400:#rozlišení misí
            nepritel.nabíjení(obrazovka, kanon13, kanon23, kanon33 , kanon43, beam3l3,kanon_destroyed)
            zaměření_na=nepritel
                
            if nepritel.zivoty_self <= 0 and nepritel.pricti ==True:
                letadlo.skore+=1000 * powerup.bonus_ke_skore
                nepritel.pricti = False

        elif pohyb_pozadí < -38000:
            base_x-=nepritel.rychlost_pozadi
            obrazovka.blit(enemy_base,(base_x,0))
            if vystrel == 1 and bomba == 0 and pohyb_pozadí <-41000  :
                bomba = 1
                bomba_x= letadlo.x -nepritel.rychlost_pozadi
                bomba_y= letadlo.y -5
            if bomba ==1:
                bomba_x-=nepritel.rychlost_pozadi-4
                bomba_y+= 5

                obrazovka.blit(bomba_image, (bomba_x, bomba_y))

       
    
        else:    #mise 2 
            vznepritel1.odpocet_do_vystrelu(vystrel)
            vznepritel2.odpocet_do_vystrelu(vystrel)

            vznepritel1.aiming(letadlo.y,letadlo.x)
        
        
             
            
    
            if vznepritel1.vystrel  == 1:
                zasazeni = False
                strela = Strela(vznepritel1.poloha_x-5, vznepritel1.poloha_y+110, vznepritel1.uhel_strely + random.randint(-10,10), zasazeni,strela_image,10,1)
                vystreleni.append(strela) 

            vznepritel1.pohyb(nepritel.rychlost_pozadi)
            vznepritel1.zjev_se(obrazovka)
            vznepritel1.znic_se()
            
            vznepritel2.aiming(letadlo.y,letadlo.x)

            if vznepritel2.vystrel  == 1:
                zasazeni = False
                strela = Strela(vznepritel2.poloha_x-5, vznepritel2.poloha_y+110, vznepritel2.uhel_strely+ random.randint(-5,5), zasazeni,strela_image,10,1)
                vystreleni.append(strela) 
            
            vznepritel2.pohyb(nepritel.rychlost_pozadi)
            vznepritel2.zjev_se(obrazovka)
            vznepritel2.znic_se()
            
            if vznepritel1.zivoty_self > 0:
                pricteni2 =True
            if vznepritel2.zivoty_self > 0:
                pricteni3 =True

        
            if vznepritel1.zivoty_self < 0 and pricteni2 ==True:
                letadlo.skore+=1000 * powerup.bonus_ke_skore
                pricteni2 =False
            if vznepritel2.zivoty_self < 0 and pricteni3 ==True:
                letadlo.skore+=1000 * powerup.bonus_ke_skore
                pricteni3 =False

            if vznepritel1.poloha_x < vznepritel2.poloha_x:
                zaměření_na = vznepritel1
            else:
                zaměření_na = vznepritel2

        otočená_stíhačka = pygame.transform.rotate(Obchod.animace(fockerfox_animace,f_animace,myg_animace,1), letadlo.uhel)
        
        rect = otočená_stíhačka.get_rect(center=(letadlo.x, letadlo.y))
        for strela in vystreleni:
            strela.just_spawned-=1
            if strela.zasazeni == False and strela.just_spawned<0 :
                strela.zasah(nepritel,200,200,3,rect)
            
                strela.zasah(nepritel,150,100,2,rect)
                
                strela.zasah(vznepritel1,173,578,1,rect)
                strela.zasah(vznepritel2,173,578,1,rect)

            strela.draw(obrazovka, strela.vzhled, vybuch_image,vybuch)    
            strela.move(nepritel.rychlost_pozadi)
            strela.draw(obrazovka, strela.vzhled, vybuch_image,vybuch)
            
        for raketa in raketa_vystrel:
            
            if raketa.zasazeni == False:
                
                
                raketa.zasah(vznepritel1,150,578,1)
                
                raketa.zasah(vznepritel2,150,578,1) 
                raketa.zasah(nepritel,150,100,2)
               
            raketa.navádění(zaměření_na,obrazovka,Obchod.animace(Raketa1,Raketa2,Raketa3,2),výška,nepritel.rychlost_pozadi,Obchod.presnost)
            raketa.draw(obrazovka, Obchod.animace(Raketa1,Raketa2,Raketa3,2), vybuch_image,vybuch, nepritel.rychlost_pozadi)
        
        if bomba_y > 900:
             letadlo.uhel = 0
             obrazovka.fill((barva,barva,barva))
             if barva<255:
                barva+=3
                  

             if obrazek_y<620:
                obrazek_y+=5
                y_pos = výška - obrazek_y   
             delay_do_konce+=1      
             atom1=pygame.transform.scale(atom,(obrazek_x,obrazek_y))
             obrazovka.blit(atom1, (540, y_pos))
             obrazovka.blit(wintext, (491, 110))

             if delay_do_konce == 300:
                 play = False
                 Lobby = True
        else:
    
    
                            
    
    
        
            powerup.touch(letadlo,shield,obrazovka,rect,nepritel.zivoty,xskóre,health_power_up,firerate_boom1,firerate_boom2)
            powerup.pohyb(nepritel.rychlost_pozadi)
            powerup.spawn(obrazovka,1000)
            
            obrazovka.blit(otočená_stíhačka, rect.topleft)
            obrazovka.blit(text_surface, text_rect)
            obrazovka.blit(bar_raketa, (350,95))
        
        
        letadlo.neutíkej()
        pygame.display.flip()
        clock.tick(60)
         #___________________________________________________________________________________________________________________________________________________________________________________________________________________
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
    
            
        
        
        

        #___________________________________________________________________________________________________________________________________________________________________________________________________________________ 
    while Infinite_mode:
        mise = 1
        text = f" SKÓRE: {letadlo.skore}                            :{letadlo.pocet_raket} "
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(300, 110))
        
        
        
        for i in range(vystrel):
            strela_x = letadlo.x + 17
            strela_y = letadlo.y + 17
            zasazeni = False
            strela = Strela(strela_x, strela_y, letadlo.uhel, zasazeni,strela_image,25,1)
            
            if powerup.co_padlo == 2:
                   
                     
                    strela = 0
                    strela = Strela(strela_x, strela_y, letadlo.uhel, zasazeni,strela_image2,25,5)
            vystreleni.append(strela)
        vystrel = 0 
          
        #
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
            
        if powerup.odpočet >0 and powerup.zivoty !=0:
            
            nepritel.zivoty  =powerup.zivoty
        
        if nepritel.zivoty >= 1:
                

            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                letadlo.pohyb_dolu(Obchod.obratnost)
        
            letadlo.pohyb_jiným_směrem()
            
            if firerate > 0:  # Delay mezi střelami
                firerate -= 1
                
            if firerate_rakety > 0:  # Delay mezi raketami
                firerate_rakety -= 1
                
             
            if keys[pygame.K_SPACE] and firerate == 0:
                firerate = Obchod.firerate * powerup.firerate  # Nastavení hodnoty delay
                vystrel = 1

                
            raketa_vystrelena = 0
            
            if keys[pygame.K_LALT] and firerate_rakety == 0 and letadlo.pocet_raket>0:
                firerate_rakety = 100  # Nastavení hodnoty delay
                raketa_vystrelena = 1
                letadlo.pocet_raket-=1
            
            if keys[pygame.K_UP]:
                letadlo.pohyb_nahoru(Obchod.obratnost)
            nepritel.rychlost_pozadi =Obchod.rychlost #očítání pohybu pod úhlem
            
               
            nepritel.rychlost_pozadi =-nepritel.rychlost_pozadi * math.sin(math.radians(letadlo.uhel-90))#90je zde k pootočení osy
                           
        else:
            letadlo.znic_se(Lobby,Infinite_mode)
            if  letadlo.znic_se(Lobby,Infinite_mode):
                Lobby = True
                play = False 
                vystreleni=[]   
        if letadlo.smrt == False:  # Kontrola jestli letadlo žije
            nepritel.pohyb_kanonu()
            pohyb_pozadí -= nepritel.rychlost_pozadi
            umisteni_pozadi1 = pohyb_pozadí % rozdil_pozadi
            umisteni_pozadi2 = (pohyb_pozadí % rozdil_pozadi) - rozdil_pozadi
        
        
        obrazovka.fill(pozadi_barva)
        obrazovka.blit(pozadí,(0,558))
        
        obrazovka.blit(health_bar2,(health_bar2x,health_bar2y))
        obrazovka.blit(health_bar,(nepritel.zivoty*100-1920,0))
        if nepritel.zivoty*100-1920 < health_bar2x:
            health_bar2x-=3
        
        obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi1, výška - 100))
        obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi2, výška - 100))
       
        nepritel.nabíjení(obrazovka, kanon13, kanon23, kanon33 , kanon43, beam3l3,kanon_destroyed)
        zaměření_na=nepritel
            
        if nepritel.zivoty_self <= 0 and nepritel.pricti ==True:
            letadlo.skore+=1000 * powerup.bonus_ke_skore
            nepritel.pricti = False

        

        otočená_stíhačka = pygame.transform.rotate(Obchod.animace(fockerfox_animace,f_animace,myg_animace,1), letadlo.uhel)
        
        rect = otočená_stíhačka.get_rect(center=(letadlo.x, letadlo.y))
        for strela in vystreleni:
            strela.just_spawned-=1
            if strela.zasazeni == False and strela.just_spawned<0 :
                strela.zasah(nepritel,200,200,3,rect)
            
                strela.zasah(nepritel,150,100,2,rect)
                
                strela.zasah(vznepritel1,173,578,1,rect)
                strela.zasah(vznepritel2,173,578,1,rect)

            strela.draw(obrazovka, strela.vzhled, vybuch_image,vybuch)    
            strela.move(nepritel.rychlost_pozadi)
            strela.draw(obrazovka, strela.vzhled, vybuch_image,vybuch)
            
        for raketa in raketa_vystrel:
            
            if raketa.zasazeni == False:
                
                
                raketa.zasah(vznepritel1,150,578,1)
                
                raketa.zasah(vznepritel2,150,578,1) 
                raketa.zasah(nepritel,150,100,2)
               
            raketa.navádění(zaměření_na,obrazovka,Obchod.animace(Raketa1,Raketa2,Raketa3,2),výška,nepritel.rychlost_pozadi,Obchod.presnost)
            raketa.draw(obrazovka, Obchod.animace(Raketa1,Raketa2,Raketa3,2), vybuch_image,vybuch, nepritel.rychlost_pozadi)
        
        if bomba_y > 900:
             letadlo.uhel = 0
             obrazovka.fill((barva,barva,barva))
             if barva<255:
                barva+=3
                  

             if obrazek_y<620:
                obrazek_y+=5
                y_pos = výška - obrazek_y   
             delay_do_konce+=1      
             atom1=pygame.transform.scale(atom,(obrazek_x,obrazek_y))
             obrazovka.blit(atom1, (540, y_pos))
             obrazovka.blit(wintext, (491, 110))

             if delay_do_konce == 300:
                 Infinite_mode = False
                 Lobby = True
        else:
    
    
                            
    
    
        
            powerup.touch(letadlo,shield,obrazovka,rect,nepritel.zivoty,xskóre,health_power_up,firerate_boom1,firerate_boom2)
            powerup.pohyb(nepritel.rychlost_pozadi)
            powerup.spawn(obrazovka,1000)
            
            obrazovka.blit(otočená_stíhačka, rect.topleft)
            obrazovka.blit(text_surface, text_rect)
            obrazovka.blit(bar_raketa, (350,95))
        
        
        letadlo.neutíkej()
        pygame.display.flip()
        clock.tick(60)

        
