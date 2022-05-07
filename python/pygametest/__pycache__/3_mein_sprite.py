import pygame


pygame.init()

screen_width = 480
screen_heiht = 640
screen = pygame.display.set_mode((screen_width, screen_heiht))
pygame.display.set_caption("Nado Game")

backgorund = pygame.image.load("C:/github/codingstudy/python/pygametest/backgorund.png")

charter = pygame.image.load("C:\github\codingstudy\python\pygametest\charter.png")
charter_size = charter.get_rect().size
charter_width = charter_size[0]
charter_height = charter_size[1]
charter_x_pos = (screen_width / 2) - (charter_width / 2)
charter_y_pos = screen_heiht - charter_height




running = True  # 게임이 진행 중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.blit(backgorund, (0, 0))

    screen.blit(charter, (charter_x_pos, charter_y_pos))

    pygame.display.update()

pygame.quit()