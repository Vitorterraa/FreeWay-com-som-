import pygame
import random

class Obstaculo:

    def __init__(self,arquivo_imagem,largura_imagem,altura_imagem,x_inicial,y_inicial):
        self.imagem = pygame.image.load(arquivo_imagem)

        self.largura = largura_imagem
        self.altura = altura_imagem

        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))

        self.pos_x = x_inicial
        self.pos_y = y_inicial

        self.velocidade = random.randint(1, 20)

        self.mascara = pygame.mask.from_surface(self.imagem)
    

    def movimenta(self):
        self.pos_x = self.pos_x - self.velocidade
        if self.pos_x < -200:
            self.pos_x = 850
            self.velocidade = random.randint(10, 30)

    def desenhar(self, tela):
        tela.blit(self.imagem,(self.pos_x,self.pos_y))        