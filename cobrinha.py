import pygame
import time
import random

# Inicializando o pygame
pygame.init()

# Definindo as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)

# Definindo as dimensões da tela
largura = 800
altura = 600

# Criando a tela do jogo
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo Snake')

# Definindo o relógio
relogio = pygame.time.Clock()

# Definindo o tamanho do bloco e a velocidade da cobra
tamanho_bloco = 20
velocidade = 15

# Função para exibir a pontuação
def mostrar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont(None, 35)
    texto = fonte.render("Pontuação: " + str(pontuacao), True, preto)
    tela.blit(texto, [0, 0])

# Função principal do jogo
def jogo():
    fim_jogo = False
    fim_jogo_perdeu = False

    x1 = largura / 2
    y1 = altura / 2

    x1_mudanca = 0
    y1_mudanca = 0

    corpo_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0

    while not fim_jogo:

        while fim_jogo_perdeu:
            tela.fill(branco)
            fonte = pygame.font.SysFont(None, 50)
            mensagem = fonte.render("Você perdeu! Pressione Q-Quit ou C-Continuar", True, vermelho)
            tela.blit(mensagem, [largura / 6, altura / 3])
            mostrar_pontuacao(comprimento_cobra - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_jogo = True
                        fim_jogo_perdeu = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_mudanca = -tamanho_bloco
                    y1_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_mudanca = tamanho_bloco
                    y1_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y1_mudanca = -tamanho_bloco
                    x1_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y1_mudanca = tamanho_bloco
                    x1_mudanca = 0

        if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
            fim_jogo_perdeu = True
        x1 += x1_mudanca
        y1 += y1_mudanca
        tela.fill(branco)
        pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        cabeca_cobra = []
        cabeca_cobra.append(x1)
        cabeca_cobra.append(y1)
        corpo_cobra.append(cabeca_cobra)
        if len(corpo_cobra) > comprimento_cobra:
            del corpo_cobra[0]

        for segmento in corpo_cobra[:-1]:
            if segmento == cabeca_cobra:
                fim_jogo_perdeu = True

        for segmento in corpo_cobra:
            pygame.draw.rect(tela, preto, [segmento[0], segmento[1], tamanho_bloco, tamanho_bloco])

        mostrar_pontuacao(comprimento_cobra - 1)
        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
            comprimento_cobra += 1

        relogio.tick(velocidade)

    pygame.quit()
    quit()

jogo()
