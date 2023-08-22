import pygame
import os
import random

pygame.init()

#  VARIABILI
larghezzafinestra = 840
altezzafinestra = 640
grandezzafigurine = 128
colonne = 5
righe = 4
spaziosinistra = (larghezzafinestra - ((grandezzafigurine + 10) * colonne)) // 2
saziodestra = spaziosinistra
spaziosopra = (altezzafinestra - ((grandezzafigurine + 10) * righe)) // 2
spaziosotto = spaziosopra
bianco = (255, 255, 255)
nero = (0, 0, 0)
verde = (0, 255, 0)
ntentativi = 0
haivinto = pygame.font.SysFont("Bell MT", 200)
s1 = None
s2 = None

# CREAZIONE FINESTRA
schermo = pygame.display.set_mode((larghezzafinestra, altezzafinestra))
pygame.display.set_caption("Memory")
figure = pygame.image.load("figure/Anzani.jpg")
pygame.display.set_icon(figure)

# LISTA CON TUTTE LE IMMAGINI
figurine = []
for item in os.listdir('figure/'):
    figurine.append(item.split('.')[0])
copiafigurine = figurine.copy()
figurine.extend(copiafigurine)
copiafigurine.clear()
random.shuffle(figurine)

# CARICARE LE IMMAGINI IN PYTHON
fotomemory = []
fotomemoryrect = []
nascoste = []
for item in figurine:
    immagine = pygame.image.load(f'figure/{item}.jpg')
    immagine = pygame.transform.scale(immagine, (grandezzafigurine, grandezzafigurine))
    fotomemory.append(immagine)
    immaginerect = immagine.get_rect()
    fotomemoryrect.append(immaginerect)

for i in range(len(fotomemoryrect)):
    fotomemoryrect[i][0] = spaziosinistra + ((grandezzafigurine + 10) * (i % colonne))
    fotomemoryrect[i][1] = spaziosopra + ((grandezzafigurine + 10) * (i % righe))
    nascoste.append(False)

print(figurine)
print(fotomemory)
print(fotomemoryrect)
print(nascoste)

# SFONDO
sfondo = pygame.image.load('sfondo.jpg')
sfondo = pygame.transform.scale(sfondo, (larghezzafinestra, altezzafinestra))
sfondorect = sfondo.get_rect()

gioco = True
while gioco:
    # CARICAMENTO IMMAGINE DI SFONDO
    schermo.blit(sfondo, sfondorect)

    # INPUT
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for i in fotomemoryrect:
                if i.collidepoint(evento.pos):
                    if nascoste[fotomemoryrect.index(i)] != True:
                        if s1 != None:
                            s2 = fotomemoryrect.index(i)
                            nascoste[s2] = True
                        else:
                            s1 = fotomemoryrect.index(i)
                            nascoste[s1] = True

    for i in range(len(figurine)):
        if nascoste[i] == True:
            schermo.blit(fotomemory[i], fotomemoryrect[i])
        else:
            pygame.draw.rect(schermo, bianco, (fotomemoryrect[i][0], fotomemoryrect[i][1], grandezzafigurine, grandezzafigurine))
    pygame.display.update()

    if s1 != None and s2 != None:
        ntentaivi = ntentativi + 1
        if figurine[s1] == figurine[s2]:
            s1, s2 = None, None
        else:
            pygame.time.wait(1000)
            nascoste[s1] = False
            nascoste[s2] = False
            s1, s2 = None, None

    vittoria = 1
    for number in range(len(nascoste)):
        vittoria *= nascoste[number]

    if vittoria == 1:
        schermo.fill(nero)
        scritta = haivinto.render("HAI VINTO!", True, verde)
        schermo.blit(scritta, (35, 200))
        pygame.display.flip()
        pygame.time.wait(3000)
        
        gioco = False

    pygame.display.update()

pygame.quit()