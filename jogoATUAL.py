import pygame
import random
from personagemATUAL import Personagema
from obstaculoATUAL import Obstaculoa

pygame.init()

#Constrindo a tela
tela = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Freeway")
tela.fill((80,120,200))

FUNDO = pygame.image.load("imagens_akuma/fundo.jpg")
FUNDO = pygame.transform.scale(FUNDO,(1000,500))

#Criando mais personagens
jogador1 = Personagema("imagens_akuma/Luffy.png",80,50,300,450)



frutas = [Obstaculoa("imagens_akuma/fruta_amarela.png",100,50,random.randint(5, 10),0),
               Obstaculoa("imagens_akuma/fruta_abacaxi.jpg",100,50,random.randint(5, 10),0),
               Obstaculoa("imagens_akuma/fruta_azul.webp",100,50,random.randint(5, 10),0),
               Obstaculoa("imagens_akuma/fruta_prata.webp",100,50,random.randint(5, 10),0),
               Obstaculoa("imagens_akuma/fruta_roxa.png",100,50,random.randint(5, 10),0)]

#Configurando a fonte
fonte = pygame.font.SysFont("Castellar",14)

#Carregando som de dor
som_dor = pygame.mixer.Sound("som/som_dor.mp3")
som_vaca = pygame.mixer.Sound("som/som_vaca.mp3")

#musica de fundo
pygame.mixer.music.load("som/musica_fundo.mp3")

# Defina a repetição do som de fundo
pygame.mixer.music.set_endevent(pygame.USEREVENT)

# Inicie a reprodução do som de fundo
pygame.mixer.music.play()

#Criando um relogio para controlar o FPS
clock = pygame.time.Clock()




rodando = True
while rodando:
    #Tratando eventos
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("Você clicou!!")
        if evento.type == pygame.QUIT:
            rodando = False

    tela.blit(FUNDO,(0,0))

    #Desenhando as imagens
    jogador1.movimentar_via_controle(pygame.K_RIGHT,pygame.K_LEFT)
    jogador1.desenhar(tela)

    

    for fruta in frutas:
        fruta.movimenta()
        fruta.desenhar(tela)

        if jogador1.mascara.overlap(fruta.mascara,(fruta.pos_x-jogador1.pos_x , fruta.pos_y-jogador1.pos_y)):
            texto_pontuacao_vaca = texto_pontuacao_vaca + 1
            som_vaca.play()
        
            


    


        
    texto_pontuacao_vaca = fonte.render(f"Pontuação: {jogador1.pontuacao}",True,(255,0,0))
    tela.blit(texto_pontuacao_vaca,(0,10))

    

    #Atualizando a tela
    pygame.display.update()

    #Regulando o FPS
    clock.tick(60)

























