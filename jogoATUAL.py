import pygame
import random
from personagem import Personagem
from obstaculoANTIGO import Obstaculo

pygame.init()

#Constrindo a tela
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Freeway")
tela.fill((80,120,200))

FUNDO = pygame.image.load("imagens/estrada.png")
FUNDO = pygame.transform.scale(FUNDO,(800,500))

#Criando mais personagens
jogador1 = Personagem("imagens/vaca.png",80,50,300,450)
jogador2 = Personagem("imagens/hamster.png",50,50,450,450)

lista_carro = [Obstaculo("imagens_akuma/fruta_amarela.png",100,50,random.randint(5, 10),0),
               Obstaculo("imagens_akuma/fruta_abacaxi.jpg",100,50,random.randint(5, 10),0),
               Obstaculo("imagens_akuma/fruta_azul.webp",100,50,random.randint(5, 10),0),
               Obstaculo("imagens_akuma/fruta_prata.webp",100,50,random.randint(5, 10),0),
               Obstaculo("imagens_akuma/fruta_roxa.png",100,50,random.randint(5, 10),0)]

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
    jogador1.movimentar_via_controle(pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT)
    jogador1.desenhar(tela)
    jogador2.movimentar_via_controle(pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a)
    jogador2.desenhar(tela)
    

    for carro in lista_carro:
        carro.movimenta()
        carro.desenhar(tela)

        if jogador1.mascara.overlap(carro.mascara,(carro.pos_x-jogador1.pos_x , carro.pos_y-jogador1.pos_y)):
            jogador1.pos_x = 300
            jogador1.pos_y = 450
            jogador1.pontuacao -= 1
            som_vaca.play()
            

        if jogador2.mascara.overlap(carro.mascara,(carro.pos_x-jogador2.pos_x , carro.pos_y-jogador2.pos_y)):
            jogador2.pos_x = 450
            jogador2.pos_y = 450
            jogador2.pontuacao -= 1
            som_dor.play()

    if jogador1.pos_y <= 10:
        jogador1.pos_x = 300
        jogador1.pos_y = 450
        jogador1.pontuacao += 1

    if jogador2.pos_y <= 10:
        jogador2.pos_x = 300
        jogador2.pos_y = 450
        jogador2.pontuacao += 1
        
    texto_pontuacao_vaca = fonte.render(f"Pontuação da VACA: {jogador1.pontuacao}",True,(255,0,0))
    tela.blit(texto_pontuacao_vaca,(0,10))

    texto_pontuacao_hamster= fonte.render(f"Pontuação da HAMSTER: {jogador2.pontuacao}",True,(255,0,0))
    tela.blit(texto_pontuacao_hamster,(0,24))

    #Atualizando a tela
    pygame.display.update()

    #Regulando o FPS
    clock.tick(60)

























