from pygame import *

window = display.set_mode((700, 500))
display.set_caption("pig_pong")
king_fon = transform.scale(image.load("fon_pinpong.jpg"),(700,500))
cloc = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

    def update_right(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed

player_1 = Player("r_1.png", 670, 150, 1, 30, 150)
player_2 = Player("r_2.png", 10, 150, 1, 30, 150)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(king_fon,(0,0))

    player_1.update_left()
    player_2.update_right()

    player_1.reset()
    player_2.reset()

    cloc.tick()
    display.update()