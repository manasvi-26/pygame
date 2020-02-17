import pygame

WHITE = (255, 255, 255)

#fixed_obstacle
class fixed_obstacle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.width=width
        self.height=height
        self.color = color


        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

        self.rect = self.image.get_rect()

#moving_obstacle
class moving_obstacle(pygame.sprite.Sprite):

    def __init__(self,color,width,height,speed):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.width=width
        self.height=height
        self.color = color
        self.speed = speed


        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

        self.rect = self.image.get_rect()

    def move(self, speed):
        self.rect.x += self.speed * speed / 20

    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
