import pygame

mouse_color = (0, 255, 0)

def get_position():
    """Отримує координати курсора миші."""
    return pygame.mouse.get_pos()

def simply_cursor(screen, width, height):
    """Малює спрайт у вигляді прямокутника в координатах миші."""
    x, y = get_position()  # Отримує координати миші
    sprite_surface = pygame.Surface((width, height))  # Створює поверхню
    sprite_surface.fill(mouse_color)  # Заповнює її кольором
    screen.blit(sprite_surface, (x, y))  # Малює на екрані
