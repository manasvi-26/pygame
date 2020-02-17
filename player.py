import pygame

WHITE = (255,255,255)

class Player(pygame.sprite.Sprite):
  
    def __init__(self,width, height, speed,x):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.width=width
        self.height=height
        self.speed = speed

        pygame.draw.rect(self.image, WHITE, [0, 0, self.width, self.height])
        
        self.image = pygame.image.load(x)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveUp(self,pixels):
        self.rect.y -= pixels

    def moveDown(self,pixels):
        self.rect.y += pixels

    def movbottom(self):
        self.rect.x = 500
        self.rect.y = 800
    
    