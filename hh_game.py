import random
import pygame

# the Hobo class manages the properties of the player character 

class Hobo():
    def __init__(self):
        img = pygame.image.load('hobo.png').convert()
        self.image = img
        self.rect = self.image.get_rect()
        self.movex = 0
        self.movey = 0
        self.health = 5

    def update(self):
        if ((self.rect.y + self.movey) > 500):
            pass
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

    def control(self,x,y):
        self.movex += x
        self.movey += y


    def draw(self,screen):
        screen.blit(self.image,self.rect)

class SceneBase:
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)


def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

          
            
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
            
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update(filtered_events,pressed_keys)
        active_scene.Render(screen)
        
        active_scene = active_scene.next
        
        pygame.display.flip()
        clock.tick(fps)

class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.number_of_tracks = 2
        self.train_duration = 5
        self.inter_train_distance = 10
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER): # WHEN ENTER PRESSED, CHANGE THE SCENE TO THE GAME
                self.SwitchToScene(GameScene(self.number_of_tracks,self.train_duration,self.inter_train_distance))
    
    def Update(self,events,pressed_keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                # EVENT HANDLERS FOR TRACK NUMBER SELECTORS
                if (pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 150):
                    if (pygame.mouse.get_pos()[1] > 125 and pygame.mouse.get_pos()[1] < 175):
                        self.number_of_tracks = 2
                if (pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[0] < 300):
                    if (pygame.mouse.get_pos()[1] > 125 and pygame.mouse.get_pos()[1] < 175):
                        self.number_of_tracks = 3
                if (pygame.mouse.get_pos()[0] > 350 and pygame.mouse.get_pos()[0] < 450):
                    if (pygame.mouse.get_pos()[1] > 125 and pygame.mouse.get_pos()[1] < 175):
                        self.number_of_tracks = 4

                # EVENT HANDLERS FOR TRAIN DURATION SELECTORS
                if (pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 150):
                    if (pygame.mouse.get_pos()[1] > 225 and pygame.mouse.get_pos()[1] < 275):
                        self.train_duration = 5
                if (pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[0] < 300):
                    if (pygame.mouse.get_pos()[1] > 225 and pygame.mouse.get_pos()[1] < 275):
                        self.train_duration = 15
                if (pygame.mouse.get_pos()[0] > 350 and pygame.mouse.get_pos()[0] < 450):
                    if (pygame.mouse.get_pos()[1] > 225 and pygame.mouse.get_pos()[1] < 275):
                        self.train_duration = 25

                # EVENT HANDLERS FOR INTER-TRAIN DISTANCE SELECTORS
                if (pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 150):
                    if (pygame.mouse.get_pos()[1] > 325 and pygame.mouse.get_pos()[1] < 375):
                        self.inter_train_distance = 10
                if (pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[0] < 300):
                    if (pygame.mouse.get_pos()[1] > 325 and pygame.mouse.get_pos()[1] < 375):
                        self.inter_train_distance = 20
                if (pygame.mouse.get_pos()[0] > 350 and pygame.mouse.get_pos()[0] < 450):
                    if (pygame.mouse.get_pos()[1] > 325 and pygame.mouse.get_pos()[1] < 375):
                        self.inter_train_distance = 30


    
    def Render(self, screen):
        screen.fill((38, 173, 142))
        playfont = pygame.font.SysFont(None,20)
        font = pygame.font.SysFont(None, 64)
        font2 = pygame.font.SysFont(None, 30)

        title = playfont.render('*PRESS ENTER TO PLAY*',True, (255,0,0))
        screen.blit(title, (170, 400))

        title = playfont.render('*controls are 1-2-3-4 to change tracks*',True, (255,0,0))
        screen.blit(title, (135, 440))

        title = font.render('The Hogwarts',True, (255,0,0))
        screen.blit(title, (98, 8))

        title = font.render('HOBO',True, (255,0,0))
        screen.blit(title, (185, 52))

        tr = font2.render('Number of Tracks:',True, (255,0,0))
        screen.blit(tr, (165, 100))

        pygame.draw.rect(screen, (0,255,0),(50,125,100,50))
        pygame.draw.rect(screen, (0,255,0),(200,125,100,50))
        pygame.draw.rect(screen, (0,255,0),(350,125,100,50))

        if (self.number_of_tracks ==2):
            pygame.draw.rect(screen, (0,0,255),(50,125,100,50))
        if (self.number_of_tracks ==3):
            pygame.draw.rect(screen, (0,0,255),(200,125,100,50))
        if (self.number_of_tracks ==4):
            pygame.draw.rect(screen, (0,0,255),(350,125,100,50))
        
        tr = font2.render('2',True, (255,0,0))
        screen.blit(tr, (92, 140))
        tr = font2.render('3',True, (255,0,0))
        screen.blit(tr, (242, 140))
        tr = font2.render('4',True, (255,0,0))
        screen.blit(tr, (392, 140))


        td = font2.render('Train Duration',True, (255,0,0))
        screen.blit(td, (179, 200))

        pygame.draw.rect(screen, (0,255,0),(50,225,100,50))
        pygame.draw.rect(screen, (0,255,0),(200,225,100,50))
        pygame.draw.rect(screen, (0,255,0),(350,225,100,50))

        if (self.train_duration ==5):
            pygame.draw.rect(screen, (0,0,255),(50,225,100,50))
        if (self.train_duration ==15):
            pygame.draw.rect(screen, (0,0,255),(200,225,100,50))
        if (self.train_duration ==25):
            pygame.draw.rect(screen, (0,0,255),(350,225,100,50))

        tr = font2.render('5',True, (255,0,0))
        screen.blit(tr, (92, 240))
        tr = font2.render('15',True, (255,0,0))
        screen.blit(tr, (235, 240))
        tr = font2.render('25',True, (255,0,0))
        screen.blit(tr, (385, 240))

        trd = font2.render('Inter-train Distance',True, (255,0,0))
        screen.blit(trd, (155, 300))

        pygame.draw.rect(screen, (0,255,0),(50,325,100,50))
        pygame.draw.rect(screen, (0,255,0),(200,325,100,50))
        pygame.draw.rect(screen, (0,255,0),(350,325,100,50))

        if (self.inter_train_distance ==10):
            pygame.draw.rect(screen, (0,0,255),(50,325,100,50))
        if (self.inter_train_distance ==20):
            pygame.draw.rect(screen, (0,0,255),(200,325,100,50))
        if (self.inter_train_distance ==30):
            pygame.draw.rect(screen, (0,0,255),(350,325,100,50))

        tr = font2.render('10',True, (255,0,0))
        screen.blit(tr, (85, 340))
        tr = font2.render('20',True, (255,0,0))
        screen.blit(tr, (235, 340))
        tr = font2.render('30',True, (255,0,0))
        screen.blit(tr, (385, 340))

        img = pygame.image.load('hobo.png').convert()
        screen.blit(img, (80,463))
        screen.blit(img, (230,463))
        screen.blit(img, (380,463))

        #self.SwitchToScene(GameScene())

# display the users score and tell them to exit the game
class GameOverScene(SceneBase):
    def __init__(self,score):
        SceneBase.__init__(self)
        self.score = score
    
    def ProcessInput(self,events,pressed_keys):
        pass

    def Update(self,events,pressed_keys):
        pass
    
    def Render(self, screen):
        screen.fill((0,0,0))
        font = pygame.font.SysFont(None, 24)
        txt = font.render('GAME OVER, YOU SCORED: '+str(self.score),True, (0,0,255))
        txt2 = font.render('PRESS ESCAPE TO CLOSE AND THEN RUN AGAIN',True,(0,0,255))
        screen.blit(txt, (125, 250))
        screen.blit(txt2, (50, 300))


class GameScene(SceneBase):
    def __init__(self,number_of_tracks,train_duration,inter_train_distance):
        SceneBase.__init__(self)
        self.number_of_tracks = number_of_tracks
        self.train_duration = train_duration
        self.inter_train_distance = inter_train_distance
        self.hobo = Hobo()
        self.hobo.rect.x = 250
        self.hobo.rect.y = 200
        self.seconds = pygame.time.get_ticks()
        self.danger = False
        self.trainOn = 5
        self.trainOnNext = random.randrange(1,self.number_of_tracks+1)
        self.hit = False
        self.wait_count = 0
        self.train_count = 1
        self.danger = False
        self.lieChance = random.randrange(1,3)


    
    def ProcessInput(self, events, pressed_keys):
        pass
        
    def Update(self,events,pressed_keys):
        # control the movement, player uses the 1-4 keys to switch tracks.
        for event in events:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_KP1 or event.key ==pygame.K_1):
                    self.hit = False
                    self.hobo.rect.y = 100

                if (event.key == pygame.K_KP2 or event.key == pygame.K_2):
                    self.hit = False
                    self.hobo.rect.y = 200

                if (event.key == pygame.K_KP3 or event.key ==pygame.K_3):
                    if (self.number_of_tracks == 2):
                        pass
                    else:
                        self.hit = False
                        self.hobo.rect.y = 300

                if (event.key == pygame.K_KP4 or event.key ==pygame.K_4):
                    if (self.number_of_tracks == 3 or self.number_of_tracks == 2):
                        pass
                    else:
                        self.hit = False
                        self.hobo.rect.y = 400

        # if the hobo's health drops to 0, go to the game over screen
        if (self.hobo.health < 1):
            self.SwitchToScene(GameOverScene(self.seconds))

    
    def Render(self, screen):
        font = pygame.font.SysFont(None, 24)
        time = (pygame.time.get_ticks() - self.seconds) /1000
        screen.fill((38,0,0))

        # draw the train tracks
        img = pygame.image.load('track.png').convert()
        track = img.get_rect(center = (250,118))
        track2 = img.get_rect(center = (250,218))


        screen.blit(img,track)
        screen.blit(img,track2)
        if (self.number_of_tracks == 3):
            track3 = img.get_rect(center = (250,318))
            screen.blit(img,track3)
        elif (self.number_of_tracks == 4):
            track3 = img.get_rect(center = (250,318))
            track4 = img.get_rect(center = (250,418))
            screen.blit(img,track3)
            screen.blit(img,track4)

        # collision detection for each track, check if train is on the track that you are trying to go to and reposition after a hit.
        if (self.hobo.rect.y / 100 == self.trainOn): # if hit at 100, go to 200
            self.hobo.health -= 1
            self.hobo.rect.y = 200
            self.hit = True

        if (self.hobo.rect.y / 100 == self.trainOn): # if hit at 200, go to 100
            self.hobo.health -= 1
            self.hobo.rect.y = 100
            self.hit = True
        
        if (self.hobo.rect.y / 100 == self.trainOn): # if hit at 300, go to 200
            self.hobo.health -= 1
            self.hobo.rect.y = 200
            self.hit = True

        if (self.hobo.rect.y / 100 == self.trainOn): # if hit at 400, go to 300
            self.hobo.health -= 1
            self.hobo.rect.y = 300
            self.hit = True

        
        # TRAIN ARRIVE CONDITION
        if (int(time) == self.inter_train_distance+(self.train_duration + self.inter_train_distance)*self.wait_count):
            self.trainOn = self.trainOnNext
            self.trainOnNext = random.randrange(1,self.number_of_tracks+1)
            self.danger = True
            self.wait_count += 1

        if (self.danger == True and self.hit == True): # if you are hit and the trains are still running
            txt = font.render('HIT!',True, (255, 254, 142))  # alert the player that they have been hit
            screen.blit(txt, (250, 0))

            if (self.trainOn == 1): #draw the trains on the track where they got hit, and remove them when they leave the tunnel.
                train = pygame.image.load('train.png').convert()
                trainRect = img.get_rect(center = (250,118))
                screen.blit(train,trainRect)

            if (self.trainOn == 2):
                train = pygame.image.load('train.png').convert()
                trainRect = img.get_rect(center = (250,218))
                screen.blit(train,trainRect)

            if (self.trainOn == 3):
                train = pygame.image.load('train.png').convert()
                trainRect = img.get_rect(center = (250,318))
                screen.blit(train,trainRect)

            if (self.trainOn == 4):
                train = pygame.image.load('train.png').convert()
                trainRect = img.get_rect(center = (250,418))
                screen.blit(train,trainRect)
            
            self.lieChance = random.randrange(1,3) # ready up another possible lie for next round...
            


        if (self.danger == False):
            self.hit=False
            if (self.lieChance == 2): # the hobos tell the truth somtimes...
                txt = font.render('hint: next train may be at L'+str(self.trainOnNext)+'...',True, (255, 254, 142))
                screen.blit(txt, (150, 0))
            
            if (self.lieChance == 1): # and other times they lie....
                if (self.trainOnNext == 1):
                    txt = font.render('hint: next train may be at L'+(str(self.trainOnNext+1))+'...',True, (255, 254, 142))
                    screen.blit(txt, (150, 0))
                else:
                    txt = font.render('hint: next train may be at L'+(str(self.trainOnNext-1))+'...',True, (255, 254, 142))
                    screen.blit(txt, (150, 0))

        # TRAIN LEAVE CONDITION
        if (int(time) == (self.inter_train_distance+self.train_duration)*self.train_count):
            self.danger = False
            self.trainOn = 0
            self.train_count += 1

        # draw the player character and update position on each render
        screen.blit(self.hobo.image, self.hobo.rect)
        self.hobo.update()

        # draw the health and time indicators
        health_indicator = font.render('health: '+str(self.hobo.health),True, (0,0,255))
        time_indicator = font.render('time: '+str(int(time)),True, (0,0,255),)
        screen.blit(health_indicator, (0, 0))
        screen.blit(time_indicator,(400,0))

run_game(500, 500, 60, TitleScene())