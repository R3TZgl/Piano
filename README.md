# Piano

## Projeto Escolar de Extensão

O projeto a seguir está sendo desenvolvido em horários externos ao horário do ensino médio e vem com o objetivo de aprofundar mais os conhecimentos sobre Python e a biblioteca Pygame. 

## Detalhes do Jogo

Este jogo funciona de forma semelhante a um piano, com 7 teclas e cada uma com suas devidas notas.

### Imagem

![Teclado](https://pt.dreamstime.com/imagem-de-stock-piano-colorido-arco-%C3%ADris-image13157551)

## Base do código

> Foi usado a linguagem Python junto com a biblioteca pygame.

~~~~python

while True:
    tela.fill((25,25,25))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, vermelho, (25, 25, l_tecla, a_tecla))

    comand = pygame.key.get_pressed()
    if comand[pygame.K_z]:
        pygame.draw.rect(tela, branco, (25, 25, l_tecla, a_tecla))
        pygame.draw.rect(tela, preto, (25, 25, l_tecla, a_tecla),2)
        som("Notas/do.wav")

    pygame.display.update()
~~~~

[Código Completo do Jogo](piano.py)

No momento é isto.
Até a próxima!