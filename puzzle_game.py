import pygame, random, math

#Initialize pygame
pygame.init()

FPS = 60
clock = pygame.time.Clock()

#Set display surface
w = 800
h = 800

red = (240,0,0)
black = (0,0,0)

font = pygame.font.Font('Blacknorthdemo.otf',32)


X = [(w//4,0), (w//4, h)]
Y = [h//4,h//2-h//4, h//2+h//4, h - h//4]

background_image = pygame.transform.scale(pygame.image.load("christmas_image.jpg"),(w,h))
background_rect = background_image.get_rect()

display_surface = pygame.display.set_mode((w,h))
pygame.display.set_caption("Christmas sliding game")

sliding_velocity = 10


class Game():
    def __init__(self):
        self.round_time = 0
        self.frame_count = 0

    def update(self):
        self.playField()
        self.frame_count += 1
        if self.frame_count == FPS:
            self.round_time += 1
            self.frame_count = 0
        
        
    def playField(self):
        #rozdělení do dílů
        pygame.draw.line(display_surface, red, (w//4,0), (w//4, h), 1)
        pygame.draw.line(display_surface, red, (w//2,0), (w//2, h), 1)
        pygame.draw.line(display_surface, red, (w - w//4,0), (w-w//4, h), 1)
        pygame.draw.line(display_surface, red, (0,h//4), (w,h//4), 1)
        pygame.draw.line(display_surface, red, (0, h//2), (w, h//2), 1)
        pygame.draw.line(display_surface, red, (0, h-h//4), (w, h - h//4), 1)

    
    def FirstPageText(self, main_text, mute_text):
        global running
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
      

        main_text = font.render(main_text, True, WHITE)
        main_rect = main_text.get_rect()
        main_rect.center = (w//2, h//2)

        mute_text = font.render(mute_text, True, WHITE)
        mute_rect = mute_text.get_rect()
        mute_rect.center = (w//2, h//2)

        
    


        display_surface.fill(BLACK)
        display_surface.blit(main_text, main_rect)
       # display_surface.blit(mute_text, mute_rect)
        pygame.display.update()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_paused = False

                if event.type == pygame.MOUSEBUTTONUP:
                    is_paused = False


                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    def roundTime(self):
        time_text = font.render("Round Time: " + str(self.round_time), True, red)
        time_rect = time_text.get_rect()
        time_rect.topright = (w//2, 5)
        display_surface.blit(time_text, time_rect)
        pygame.display.update()
    def draw(self):
        pass

class Images(pygame.sprite.Sprite):
    def __init__(self, num,x,y):
        super().__init__()
        #self.images = []
        self.num = num
        #self.index = index
        #for num in range(1,16):
        self.image = pygame.transform.scale(pygame.image.load(f"exp/{num}.jpg"),(200, 200))
        #self.index = 0
        #self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

class BlackPicture(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.picture = pygame.transform.scale(pygame.image.load("black.png"),(200,200))
        self.rect = self.picture.get_rect()
        self.rect.topleft = (x,y)
game = Game()
game.FirstPageText("hit ENTER or TOUCH THE SCREEN to start the game", "hit ENTER again to stop the clock")

im = []
for n in range(1,17):
    im.append(n)

random.shuffle(im)

image_group = pygame.sprite.Group()

image2 = Images(im[1],200,0)
image3 = Images(im[2],400,0)
image4 = Images(im[3],600,0)
image5 = Images(im[4], 0, 200)
image6 = Images(im[5], 200,200)
image7 = Images(im[6], 400, 200)
image8 = Images(im[7], 600, 200)
image9 = Images(im[8], 0, 400)
image10 = Images(im[9], 200, 400)
image11 = Images(im[10], 400, 400)
image12 = Images(im[11], 600, 400)
image13 = Images(im[12], 0, 600)
image14 = Images(im[13], 200,600)
image15 = Images(im[14], 400, 600)
image16 = Images(im[15], 600, 600)


image_group.add(image2, image3, image4, image5, image6,image7, image8, image9, image10, image11, image12, image13, image14, image15, image16)

black_group = pygame.sprite.Group()
black_image = BlackPicture(0,0)

running = True
while running:

    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in image_group if s.rect.collidepoint(pos)]
            if not clicked_sprites:
                pass
            else:
                a = clicked_sprites[0].rect.topleft
                b = black_image.rect.topleft
                black_image.rect.topleft = a
                clicked_sprites[0].rect.topleft = b
            

    display_surface.fill(black)

    image_group.draw(display_surface)
    image_group.update()

    black_group.draw(display_surface)
    black_group.update()

    game.playField()
    game.update()
   # game.roundTime()

    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()
     