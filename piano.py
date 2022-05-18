import pygame
from pygame.locals import *
from sys import exit
from musica import som
from time import sleep
    
pygame.init()


#Dimensões da Tela
l_tela = 750
a_tela = 550

#Tela
tela = pygame.display.set_mode((l_tela,a_tela))
pygame.display.set_caption('Borboletinha Verde')

#Dimensões das Teclas
l_tecla = 100
a_tecla = 500

#Cores
branco = (255,255,255)
vermelho = (255,0,0)
laranja = (255,140,0)
amarelo = (255,255,0)
verde = (0,255,0)
ciano = (0,255,255)
azul = (0,0,255)
violeta = (75,0,130)
cinza = (50,50,50)
preto = (0,0,0)



while True:
    tela.fill((25,25,25))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, vermelho, (25, 25, l_tecla, a_tecla))
    pygame.draw.rect(tela, laranja, (25 + l_tecla, 25, l_tecla, a_tecla))
    pygame.draw.rect(tela, amarelo, (25 + l_tecla * 2, 25, l_tecla, a_tecla))
    pygame.draw.rect(tela, verde, (25 + l_tecla * 3, 25, l_tecla, a_tecla))
    pygame.draw.rect(tela, ciano, (25 + l_tecla * 4, 25, l_tecla, a_tecla))
    pygame.draw.rect(tela, azul, (25 + l_tecla * 5, 25, l_tecla, a_tecla))
    pygame.draw.rect(tela, violeta, (25 + l_tecla * 6, 25, l_tecla, a_tecla))


    comand = pygame.key.get_pressed()
    if comand[pygame.K_z]:
        pygame.draw.rect(tela, branco, (25, 25, l_tecla, a_tecla))
        pygame.draw.rect(tela, preto, (25, 25, l_tecla, a_tecla),2)
        som("Notas/do.wav")
    
    if comand[pygame.K_x]:
        pygame.draw.rect(tela, branco, (25 + l_tecla, 25, l_tecla, a_tecla))
        pygame.draw.rect(tela, preto, (25 + l_tecla, 25, l_tecla, a_tecla),2)
        som("Notas/re.wav")
        
    if comand[pygame.K_c]:
        pygame.draw.rect(tela, branco, (25 + l_tecla * 2, 25, l_tecla, a_tecla))
        pygame.draw.rect(tela, preto, (25 + l_tecla * 2, 25, l_tecla, a_tecla),2)
        som("Notas/mi.wav")
    
    if comand[pygame.K_v]:
        pygame.draw.rect(tela, branco, (25 + l_tecla * 3, 25, l_tecla, a_tecla))
        pygame.draw.rect(tela, preto, (25 + l_tecla * 3, 25, l_tecla, a_tecla),2)
        som("Notas/fa.wav")
    
    if comand[pygame.K_b]:
        pygame.draw.rect(tela, branco, (25 + l_tecla * 4, 25, l_tecla, a_tecla))
        pygame.draw.rect(tela, preto, (25 + l_tecla * 4, 25, l_tecla, a_tecla),2)
        som("Notas/sol.wav")
    
    if comand[pygame.K_n]:
        pygame.draw.rect(tela, branco, (25 + l_tecla * 5, 25, l_tecla, a_tecla))
        pygame.draw.rect(tela, preto, (25 + l_tecla * 5, 25, l_tecla, a_tecla),2)
        som("Notas/la.wav")
    
    if comand[pygame.K_m]:
        pygame.draw.rect(tela, branco, (25 + l_tecla * 6, 25, l_tecla, a_tecla))
        pygame.draw.rect(tela, preto, (25 + l_tecla * 6, 25, l_tecla, a_tecla),2)
        som("Notas/si_fade.wav")

   

    pygame.display.update()
asdf
print('sim')
