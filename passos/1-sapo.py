import pygame

pygame.init()
tela = pygame.display.set_mode((600, 400))
relogio = pygame.time.Clock()
T = 40
inicio = pygame.Rect(7 * T, 9 * T, T, T)
sapo = inicio.copy()
setas = {
    pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0),
    pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1),
}

def desenhar_sapo(s):
    corpo = s.inflate(-6, -6)
    pygame.draw.rect(tela, "chartreuse", corpo, 0, 12)
    for lado in (-9, 9):
        olho = (s.centerx + lado, s.top + 10)
        pygame.draw.circle(tela, "white", olho, 6)
        pygame.draw.circle(tela, "black", olho, 3)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key in setas:
                dx, dy = setas[evento.key]
                novo = sapo.move(dx * T, dy * T)
                if tela.get_rect().contains(novo):
                    sapo = novo

    tela.fill("dimgray")
    tela.fill("royalblue", (0, T, 600, 3 * T))
    for y in (0, 4, 9):
        tela.fill("forestgreen", (0, y * T, 600, T))
    desenhar_sapo(sapo)
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
