import pygame, sys, random

# -----Dificuldade-----
# Facil          ->  10
# Normal         ->  15
# Difícil        ->  30
# Impossível     ->  50
dificuldade = 10

# Janela
janela_x = 720
janela_y = 480

pygame.init()

# Iniciar Snake Game Final
pygame.display.set_caption('Snake Game Final')
janela = pygame.display.set_mode((janela_x, janela_y))


# Cores RGB
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
cinza = pygame.Color(25, 25, 25)



# FPS
fps_controller = pygame.time.Clock()


# Variáveis
cobra_pos = [100, 60]
cobra_corpo = [[100, 60], [100-20, 60], [100-(2*20), 60]]

comida_pos = [random.randrange(1, (janela_x//20)) * 20, random.randrange(1, (janela_y//20)) * 20]

direção = 'RIGHT'
trocar = direção

score = 0
font1 = pygame.font.SysFont('arial', 20, True, True) #fonte | tamanho | Negrito ou não | Italico ou não
font2 = pygame.font.SysFont('arial', 50, True, True)

# Game Over
def game_over():
    global morreu
    game_over = font2.render('Game over!', True, red)
    game_over_rect = game_over.get_rect()
    game_over_rect = (janela_x/3.2, janela_y/4)
    janela.fill(black)
    janela.blit(game_over, game_over_rect)
    text_format2 = font1.render('Press R to restart', True, red)
    janela.blit(text_format2, (janela_x/2.6, janela_y/2))
    pygame.display.flip()
    morreu = True
    
    
def reiniciar():
    global score, cobra_corpo, cobra_pos, comida_pos, direção, trocar, morreu
    score = 0
    cobra_corpo = [[100, 60], [100-20, 60], [100-(2*20), 60]]
    cobra_pos = [100, 60]
    comida_pos = [random.randrange(1, (janela_x//20)) * 20, random.randrange(1, (janela_y//20)) * 20]
    direção = 'RIGHT'
    trocar = direção
    morreu = False


morreu = False
# Início
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Quando uma tecla for pressionada
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                trocar = 'UP'
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                trocar = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                trocar = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                trocar = 'RIGHT'


    # Cobra não ir direção contraria da sua direção principal
    if trocar == 'UP' and direção != 'DOWN':
        direção = 'UP'
    if trocar == 'DOWN' and direção != 'UP':
        direção = 'DOWN'
    if trocar == 'LEFT' and direção != 'RIGHT':
        direção = 'LEFT'
    if trocar == 'RIGHT' and direção != 'LEFT':
        direção = 'RIGHT'

    # Movimento
    if direção == 'UP':
        cobra_pos[1] -= 20
    if direção == 'DOWN':
        cobra_pos[1] += 20
    if direção == 'LEFT':
        cobra_pos[0] -= 20
    if direção == 'RIGHT':
        cobra_pos[0] += 20
    # Score
    msg = f'Score: {score}'
    text_format = font1.render(msg, True, (255, 255, 255))

    # Comer maçã
    cobra_corpo.insert(0, list(cobra_pos))
    if cobra_pos[0] == comida_pos[0] and cobra_pos[1] == comida_pos[1]:
        score += 1
        comida_pos = [random.randrange(1, (janela_x//20)) * 20, random.randrange(1, (janela_y//20)) * 20]
    else:
        cobra_corpo.pop()

    janela.fill(black)
    for pos in cobra_corpo:
        pygame.draw.rect(janela, green, pygame.Rect(pos[0], pos[1], 20, 20))

    # Comida
    pygame.draw.rect(janela, red, pygame.Rect(comida_pos[0], comida_pos[1], 20, 20))

    # Game over
    # Borda
    if cobra_pos[0] < 0 or cobra_pos[0] > janela_x - 20:
        game_over()
    if cobra_pos[1] < 0 or cobra_pos[1] > janela_y - 20:
        game_over()
    # Tocar proprio corpo
    for block in cobra_corpo[1:]:
        if cobra_pos[0] == block[0] and cobra_pos[1] == block[1]:
            game_over()

    while morreu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reiniciar()

    # Linhas
    for x in range(0, janela_x, 20): # linhas horizontais
        pygame.draw.line(janela, cinza, (x, 0), (x, janela_y))
    for y in range(0, janela_y, 20): # Linhas verticais
        pygame.draw.line(janela, cinza, (0, y), (janela_x, y))


    janela.blit(text_format, (600, 10))
    pygame.display.update()
    fps_controller.tick(dificuldade)
