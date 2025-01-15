import pygame
import modules.mouse as mouse
import modules.exe as exe

# Ініціалізація Pygame
pygame.init()
pygame.mouse.set_visible(False)
# Налаштування екрану
BG = (52, 107, 235)  # Колір фону
screen = pygame.display.set_mode((0, 0), pygame.HWSURFACE)  # Розмір вікна
pygame.display.set_caption('PyDE')  # Назва вікна

running = True  # Статус 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # Очищення екрану
    screen.fill(BG)
    # Мишка
    mouse.simply_cursor(screen, 10, 20)  # Розмір спрайта (10x20 пікселів)
    # Оновлення екрану
    pygame.display.flip()

pygame.quit()
