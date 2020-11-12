import pygame
# from ball import Ball
from random import randint

pygame.mixer.pre_init(44100, -16, 1, 512) 
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)

pygame.mixer.music.load('sounds/bird.mp3')
pygame.mixer.music.play(-1)

s_catch = pygame.mixer.Sound('sounds/po.w64')

big_caht= pygame.mixer.Sound('sounds/ahr.w64')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
W, H = 1000,570

sc = pygame.display.set_mode((W, H))

clock = pygame.time.Clock()
FPS = 60


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, score, group,name):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.score = score
        self.name=name
        self.add(group)
        
    def update(self, *args):
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speed
        else:
            self.kill()









score = pygame.image.load('images/score_fon.png').convert_alpha()
f = pygame.font.SysFont('arial', 30)

telega = pygame.image.load('images/telega.png').convert_alpha()
telega = pygame.transform.scale(telega, (250, 150)).convert_alpha()

t_rect = telega.get_rect(centerx=W//2, bottom=H-5)

balls_data = (
              {'path': 'Thngs-1.png', 'score': 50,'name':'Thngs-1'},
              {'path': 'Thngs-2.png', 'score': 100,'name':'Thngs-2'},
              {'path': 'Thngs-3.png', 'score': 150,'name':'Thngs-3'},
              {'path': 'Thngs-7.png', 'score': 150,'name':'Thngs-7'},
              {'path': 'Thngs-13.png', 'score': 120,'name':'Thngs-13'},
              {'path': 'Thngs-17.png', 'score': 150,'name':'Thngs-17'},
              {'path': 'Thngs-19.png', 'score': 120,'name':'Thngs-19'},
              {'path': 'Thngs-26.png', 'score': 200,'name':'Thngs-26'},
            )
balls_surf1 = [pygame.image.load('images/'+data['path']).convert_alpha() for data in balls_data]

balls_surf=[]
for i in balls_surf1:
    picture = pygame.transform.scale(i, (75, 90)) 
    balls_surf.append(picture)



f1 = pygame.font.SysFont('serif', 48)
text1 = f1.render("World Мир", False,
                  (0, 180, 0))

def createBall(group):
    indx = randint(0, len(balls_surf)-1)
    x = randint(20, W-20)
    speed = randint(1, 4)

    return Ball(x, speed, balls_surf[indx], balls_data[indx]['score'], group, balls_data[indx]['name'])

game_score = 0


asd= pygame.draw.line(sc, BLACK, 
                 [10, 30], 
                 [290, 15], 3)

def collideBalls():
    global game_score
    for ball in balls:
        if t_rect.collidepoint(ball.rect.center):
            if ball.name=='Thngs-26':
                big_caht.play()
                game_score += ball.score
                ball.kill()
            s_catch.play()
            game_score += ball.score
            ball.kill()
        # if t_rect.collidepoint(ball.rect.center) != 1:
        #     game_score-=100




balls = pygame.sprite.Group()

bg = pygame.image.load('images/back1.jpg').convert()

speed = 10
createBall(balls)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)        

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        t_rect.x -= speed
        if t_rect.x < 0:
            t_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        t_rect.x += speed
        if t_rect.x > W-t_rect.width:
            t_rect.x = W-t_rect.width
    collideBalls()
    sc.blit(bg, (0, 0))
    sc.blit(score, (0, 0))
    sc_text = f.render(str(game_score), 1, (94, 138, 14))
    sc.blit(sc_text, (20, 10))

    balls.draw(sc)
    sc.blit(telega, t_rect)
    pygame.display.update()

    clock.tick(FPS)

    balls.update(H)