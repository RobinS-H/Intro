import pygame
from frame import Frame

pygame.init()
pygame.font.init()

class Puzzle:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.FPS = pygame.time.Clock()
        self.is_arranged = False
        self.font = pygame.font.SysFont("Courier New", 33)
        self.background_color = (0, 0, 0)
        self.message_color = (255, 255, 255)
    
    def _draw(self, frame):
        frame.draw(self.screen)
        pygame.display.update()

    def _instruction(self):
        instructions = self.font.render("Använd piltangenterna", True, self.message_color)
        screen.blit(instructions,(5,460))

    def main(self, frame_size):
        self.screen.fill("white")
        frame = Frame(frame_size)
        self._instruction()
        game = Game()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if not self.is_arranged:
                        if game.arrow_key_clicked(event):
                            frame.handle_click(event)
                if game.is_game_over(frame):
                    self.is_arranged = True
                    game.message
            self._draw(frame)
            self.FPS.tick(30)
        pygame.quit()

if __name__ == "__main__":
    window_size = (450, 500)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Slide puzzle")
    game = Puzzle(screen)
    game.main(window_size[0])


    