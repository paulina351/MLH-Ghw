import pygame
import random
import time

class Game:

    def __init__(self):
        # init pygame
        pygame.init()
        # score
        self.score = 0 
        # set the window
        self.window = pygame.display.set_mode((500, 500))
        # font 
        self.font = pygame.font.SysFont("consolas", 20)
        # important colors
        self.blue = pygame.Color(0, 0, 255)
        self.green = pygame.Color(149, 212, 122)
        self.red = pygame.Color(255, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.black = pygame.Color(0, 0, 0)
        self.pink = pygame.Color(246, 143, 160)
        self.aqua = pygame.Color(0, 176, 178)
        # snake speed
        self.speed = 15
        # head
        self.head = [100, 50]
        self.snake_blocks = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.dir = "RIGHT"
        self.next_dir = self.dir
        # fruit
        self.eaten = False
        # initial fruit position
        self.fruit_pos = (random.randrange(1, (500//10)) * 10, random.randrange(1, (400//10)) * 10)

    def show_score(self):
        """
        Function that shows the score of a player
        """ 
        score_surface = self.font.render(f"Score {self.score}", True, self.block)
        # create rect
        score_rect = score_surface.get_rect()
        # displace score
        self.window.blit(score_surface, score_rect)

    def spawn_fruit(self):
        """
        Function that takes care of the spawning of the fruit.
        """
        # choose random position
        self.fruit_pos = (random.randrange(1, (500//10) * 10), random.randrange(1, (400//10)) * 10)
        pygame.draw.rect(self.window, self.blue, pygame.Rect(self.fruit_pos[0], self.fruit_pos[1], 10, 10))

    def keyboard(self, key):
        """
        Function that takes care of the keyboard dynamics
        """
        if key == pygame.K_UP:
            self.next_dir = "UP"
        if key == pygame.K_DOWN:
            self.next_dir = "DOWN"
        if key == pygame.K_LEFT:
            self.next_dir = "LEFT"
        if key == pygame.K_RIGHT:
            self.next_dir = "RIGHT"

        # make sure it doesn't collide with itself weirdly
        if self.next_dir == "UP" and self.dir != "DOWN":
            self.dir = "UP"
        if self.next_dir == "DOWN" and self.dir != "UP":
            self.dir = "DOWN"
        if self.next_dir == "LEFT" and self.dir != "RIGHT":
            self.dir = "LEFT"
        if self.next_dir == "RIGHT" and self.dir != "LEFT":
            self.dir = "RIGHT"

    def snake_mech(self):
        """
        Function that takes care of the snake's mech
        Since the size of each of the snake's body part is 10x10
        we'll have to add by tens 
        """
        # draw first fruit
        pygame.draw.rect(self.window, self.pink, pygame.Rect(self.fruit_pos[0], self.fruit_pos[1], 10, 10))
        # increment by ten the move
        self.snake_blocks.insert(0, list(self.head))
        # increment if snake ate
        if self.head[0] == self.fruit_pos[0] and self.head[1] == self.fruit_pos[1]:
            self.score += 10
            self.eaten = True
        else:
            self.snake_blocks.pop()

        for pos in self.snake_blocks:
            pygame.draw.rect(self.window, self.aqua, pygame.Rect(pos[0], pos[1], 10, 10))

        # move the snake
        if self.dir == "UP":
            self.head[1] -= 10
        if self.dir == "DOWN":
            self.head[1] += 10
        if self.dir == "LEFT":
            self.head[0] -= 10
        if self.dir == "RIGHT":
            self.head[0] += 10

        # check if snake is in bound
        if self.head[0] < 0 or self.head[0] > 500 - 10:
            self.game_over()
        if self.head[1] < 0 or self.head[1] > 400 - 10:
            self.game_over()

        # check if we lost :(
        for block in self.snake_blocks[1:]:
            if self.head[0] == block[0] and self.head[1] == block[1]:
                self.game_over()

    def game_over(self):
        """
        Function that takes care of losing.
        """
        # create text
        game_over_surface = self.font.render("YOU LOST :(", True, self.red)
        # create rectangle to hold text
        game_over_rect = game_over_surface.get_rect()
        # set position of text
        game_over_rect.midtop = (500/2, 400/2)
        # write in screen
        self.window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        # after two seconds quit game
        time.sleep(2)
        # quit
        pygame.quit()

    def start(self):
        """
        Function that takes care of the game :D
        """
        pygame.display.set_caption("Snake Game :D")
        # fps control
        fps = pygame.time.Clock()

        while True:
            self.window.fill(self.green)
            # display score
            self.show_score()
            # check for event
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.keyboard(event.key)

            # snake move
            self.snake_mech()

            # check if fruit eaten
            if self.eaten:
                self.spawn_fruit()
                self.eaten = False

            # refresh
            pygame.display.update()
            fps.tick(self.speed)

if __name__ == "__main__":
    game = Game
    game.start()

