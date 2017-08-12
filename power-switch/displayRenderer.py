import pygame


class DisplayRenderer:
    """class to render generated number to the screen"""

    def __init__(self, debug_log=dict()):
        """constructor
        :param debug_log: dictionary to write log entries into
        """
        self.debug_log = debug_log
        self.debug_log['display'] = ""
        self.full_screen = False
        self.display_buffer = None
        self.small_font = None
        self.display_width = 0
        self.display_height = 0

    def open(self, full_screen=False):
        """initializes the screen and render objects
        :param full_screen: True to use full screen, False to use window
        :param render_zero: True to render the number 0, False to render blank on 0
        """
        self.full_screen = full_screen
        if self.full_screen:
            self.display_buffer = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.display_buffer = pygame.display.set_mode((1024, 768))
        self.display_width = self.display_buffer.get_width()
        self.display_height = self.display_buffer.get_height()
        self.small_font = pygame.font.Font('freesansbold.ttf', 11)
        self.display_buffer.fill((0, 0, 0))

    def render_menu(self, menu_page=list()):
        """renders a single menu screen
        :param menu_page: the menu screen to render as a list of strings
        """
        for line in range(len(menu_page)):
            display_text = self.small_font.render(menu_page[line], True, (255, 255, 255), (0, 0, 0))
            display_rect = display_text.get_rect()
            display_rect = display_rect.move(0, 11 * line)
            self.display_buffer.blit(display_text, display_rect)

    def update(self):
        """updates the screen with the current buffer and clears the buffer"""
        pygame.display.update()
        self.display_buffer.fill((0, 0, 0))
