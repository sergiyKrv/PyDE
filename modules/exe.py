import pygame

def handle_sprite_click(screen, x, y, width, height, color):
    """
    Малює спрайт і перевіряє, чи був клік у межах спрайта.
    
    screen: об'єкт Pygame Surface, на якому малюється спрайт.
    x, y: координати верхнього лівого кута спрайта.
    width, height: розміри спрайта.
    color: колір спрайта у форматі (R, G, B).
    """
    sprite_surface = pygame.Surface((width, height))
    sprite_surface.fill(color)
    sprite_rect = pygame.Rect(x, y, width, height)
    screen.blit(sprite_surface, (x, y))
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Ліва кнопка миші
            if sprite_rect.collidepoint(event.pos):  # Перевірка, чи в межах спрайта
                print("Спрайт натиснуто!")