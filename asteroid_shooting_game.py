#Joshua Hinojosa
#Mr.Davis
#3/7/17
#Adv. Comp. Programming
#Astroid Shootin'
#v1.1

'''
This is an graphic space shooter game made with pygame, similar to a classic arcade shooter.
The main objective of the game is to get as many points as you can by destroying the oncoming asteroids.
For each asteroid you destroy, you gain 100 points and for every asteroid that gets passed you, you lose 100.
When you destroy 14 asteroids a bonus asteroid spawns and is worth 1000 points. To move the space ship left or
right, you use the left and right arrow keys on keyboard. To make the space ship shoot lasers, you use the spacebar.
Each player starts with 3 lives. If the player loses all of their lives, a gameover is triggered and if their score
is high enough, it is recorded onto the top 10 high score leaderboard. The player is then ask if they want play again.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>'''

import pygame, sys, random, time
from pygame.locals import *
pygame.init()

class Entity(pygame.sprite.Sprite):
    """Inherited by any object in the game."""

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # This makes a rectangle around the entity, used for anything
        # from collision to moving around.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


class Asteroid(Entity):
    """
    The Asteroid!  Moves around the screen.
    """

    def __init__(self, x, y, width, height):
        super(Asteroid, self).__init__(x, y, width, height)


        self.image = asteroidIMg

        self.y_direction = 4
        # Positive = down, negative = up
        # Current speed.
        self.speed = 5

    def update(self):
        # Moves the Asteroid
        self.rect.y+=3
class Bonus_Asteroid(Entity):
    """
    The Asteroid!  Moves around the screen.
    """

    def __init__(self, x, y, width, height):
        super(Bonus_Asteroid, self).__init__(x, y, width, height)

        self.image = bonus_asteroid

        self.y_direction = 5
        # Positive = down, negative = up
        # Current speed.
        self.speed = 8

    def update(self):
        # Moves the Asteroid
        self.rect.y+=7
class Spaceship(Entity):
    """
    Player controlled or AI controlled, main interaction with
    the game
    """

    def __init__(self, x, y, width, height):
        super(Spaceship, self).__init__(x, y, width, height)

        self.image = spaceshipImg

class Player(Spaceship):
    """The player controlled Paddle"""

    def __init__(self, x, y, width, height):
        super(Player, self).__init__(x, y, width, height)

        # How many pixels the Player Paddle should move on a given frame.
        self.x_change = 0
        # How many pixels the paddle should move each frame a key is pressed.
        self.x_dist = 6

    def MoveKeyDown(self, key):
        """Responds to a key-down event and moves accordingly"""
        if (key == pygame.K_LEFT):
            self.x_change += -self.x_dist
        elif (key == pygame.K_RIGHT):
            self.x_change += self.x_dist
        elif (key == pygame.K_SPACE):
            # Fires a laser bullet if the user presses the spacebar
            laser_sound.play()
            bullet = Bullet(player.rect.x+8, player.rect.y-22, 60, 70)
            # Set the laser bullet so it is where the player is
            # Add the laser bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.append(bullet)

    def MoveKeyUp(self, key):
        """Responds to a key-up event and stops movement accordingly"""
        if (key == pygame.K_LEFT):
            self.x_change += self.x_dist
        elif (key == pygame.K_RIGHT):
            self.x_change += -self.x_dist

    def update(self):
        """
        Moves the spaceship while ensuring it stays in bounds
        """
        # Moves it relative to its current location.
        self.rect.move_ip(self.x_change, 0)

        # If the spaceship moves off the screen, put it back on.
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > window_width - self.width:
            self.rect.x = window_width - self.width

class Bullet(Entity):
    """ This class represents the bullet . """
    def __init__(self,x, y, width, height):
        super(Bullet, self).__init__(x, y, width, height)


        self.image = laserbulletImg

        self.y_direction = 5
        # Positive = down, negative = up
        # Current speed.
        self.speed = 5
    def update(self):
        # Move the Asteroid!
        #self.rect.move_ip(self.speed * self.x_direction)
        self.rect.y-=18
def playagain():
    global background
    font2 = pygame.font.SysFont("monospace", 18)
    font3 = pygame.font.SysFont("monospace", 32)
    #         R    G    B
    WHITE = (255, 255, 255)
    while True:  # display loop
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_y:
                    menu()
                elif event.key == K_n:
                    pygame.quit()
                    sys.exit()
        playagaintxt= font3.render("Play again? y/n ", 1, WHITE)
        instructionstxt= font2.render("<Press 'y' for yes and 'n' for no>", 1, WHITE)
        screen.blit(playagaintxt, (80, 350))
        screen.blit(instructionstxt, (50, 650))
        clock.tick(60)
        pygame.display.flip()
def showscores():    #function that displays highscores
    global pscore, scoreslist
    try:
        font2 = pygame.font.SysFont("monospace", 28)
        font3 = pygame.font.SysFont("monospace", 24)
        #         R    G    B
        WHITE = (255, 255, 255)
        #gets highscores from highscore txt file
        infile = open("highscores.txt", "r")
        lines = infile.readlines()
        for line in lines:
            items = line.split()
            items = " ".join(items)
            if items in scoreslist:
                pass
            else:
                scoreslist.append(items)
        infile.close()
        if str(pscore) in scoreslist:
            pass
        else:
            scoreslist.append(str(pscore))
        scoreslist = sorted(scoreslist,key=int,reverse=True)
        player_place= scoreslist.index(str(pscore))+1
        outfile = open("highscores.txt", "w")       #writes updated highscores to highscores txt file
        for i in scoreslist[:10]:
            outfile.write("".join(i) + "\n")
        outfile.close()
        while True: #display loop
            screen.blit(background, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
            highscores_txt = font2.render("HIGH SCORES", 3, WHITE)  # displays "HIGH SCORE"
            border_txt = font2.render("___________", 3, WHITE)
            screen.blit(highscores_txt, (150, 135))  # displays player's high score
            screen.blit(border_txt, (150, 145))
            #displays all of the highscores
            hscore1=font3.render(scoreslist[9], 1, WHITE)
            hscore2=font3.render(scoreslist[8], 1, WHITE)
            hscore3=font3.render(scoreslist[7], 1, WHITE)
            hscore4=font3.render(scoreslist[6], 1, WHITE)
            hscore5=font3.render(scoreslist[5], 1, WHITE)
            hscore6=font3.render(scoreslist[4], 1, WHITE)
            hscore7=font3.render(scoreslist[3], 1, WHITE)
            hscore8=font3.render(scoreslist[2], 1, WHITE)
            hscore9=font3.render(scoreslist[1], 1, WHITE)
            hscore10=font3.render(scoreslist[0], 1, WHITE)
            pplace=font3.render("Player Place: " + str(player_place), 1, WHITE)
            screen.blit(hscore10, (150, 180))
            screen.blit(hscore9, (150, 210))
            screen.blit(hscore8, (150, 240))
            screen.blit(hscore7, (150, 270))
            screen.blit(hscore6, (150, 300))
            screen.blit(hscore5, (150, 330))
            screen.blit(hscore4, (150, 360))
            screen.blit(hscore3, (150, 390))
            screen.blit(hscore2, (150, 420))
            screen.blit(hscore1, (150, 450))
            screen.blit(pplace, (150, 480))
            pygame.display.flip()
            time.sleep(6)
            pagain=True
            if pagain==True:
                playagain()
            clock.tick(60)
    except FileNotFoundError: #if highscores txt file doesn't exist, then it creates one
        scoreslist=['7500','6500','5500','4500','3500','2500','1500','1000','500','0']
        outfile = open("highscores.txt", "a")  # writes updated highscores to highscores txt file
        for i in scoreslist:
            outfile.write("".join(i) + "\n")
        outfile.close()
        showscores()
def gameover(): #game over function
    global pscore, scoreslist
    scoreslist=[]
    font2 = pygame.font.SysFont("monospace", 28)
    pygame.mixer.music.load('game_over.wav')
    pygame.mixer.music.play(-1, 0)
    #         R    G    B
    WHITE = (255, 255, 255)
    while True: #display loop
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        gameover_txt= font2.render("GAME OVER", 3, WHITE)   # displays "GAME OVER"
        players_highscore_txt = font2.render("Player's Final Score: {0}".format(pscore), 3, WHITE)  # shows player's final score
        screen.blit(players_highscore_txt, (25, 350))  # displays player's high score
        screen.blit(gameover_txt, (175, 275))
        pygame.display.flip()
        clock.tick(60)
        time.sleep(5)       #runs the show high score function after 5 seconds
        gameover=True
        if gameover:
            showscores()
        clock.tick(60)
def check_screen(asteroids,bullets):    #checks if the asteroid goes off the screen
    global pscore, bonus
    for i in asteroids:
        if i.rect.y+60>=710:
            i.remove(all_sprites_list)
            asteroids.remove(i)
            if pscore==0:
                pscore+=0
            else:
             pscore-=100
    for i in bullets:
        if i.rect.y<=-10:
            i.remove(all_sprites_list)
            bullets.remove(i)

def check_hit(asteroids):#checks if the asteroid collides with player
    global plives
    for i in asteroids:
        if i.rect.colliderect(player.rect):
            asteroids.remove(i)
            i.remove(all_sprites_list)
            spaceship_explosion_sound.play()
            plives-=1
            screen.blit(background, (0, 0))
            time.sleep(.25)
            if plives==0:
                time.sleep(1)
                gameover()
def bullet_hit(asteroids,bullets):  #checks if player's lasers collide with asteroids
    global pscore, bonus, asteroid_counter
    for i in asteroids:
        for x in bullet_list:
            if i.rect.colliderect(x):  #if the player's lasers hit an asteroid, the player recieves 100 points and the asteroid and laser disappear
                i.remove(all_sprites_list)
                x.remove(all_sprites_list)
                explosion_sound.play()
                asteroids.remove(i)
                bullets.remove(x)
                if bonus==True: #if the player destroys the bonus asteroid, the player gets 1000
                    pscore+=1000
                    bonus=False
                    asteroid_counter=0
                else:
                    pscore+=100
                asteroid_counter+=1
pygame.init()
def main(): #main game function
    global screen,background, bullet_list, all_sprites_list, clock, player, window_height,\
        window_width, asteroidIMg, spaceshipImg, laserbulletImg, pscore, plives, laser_sound, \
        explosion_sound, spaceship_explosion_sound, bonus_asteroid, asteroid_counter, bonus
    spaceshipImg= pygame.image.load('Galaga_ship.png')
    spaceshipImg=pygame.transform.scale(spaceshipImg, (60, 60))
    laserbulletImg=pygame.image.load('laser_bullet.png')
    laserbulletImg=pygame.transform.scale(laserbulletImg, (60, 70))
    asteroidIMg=pygame.image.load('asteroid.png')
    asteroidIMg =pygame.transform.scale(asteroidIMg, (50, 50))
    bonus_asteroid=pygame.image.load('fire_asteroid.png')
    bonus_asteroid =pygame.transform.scale(bonus_asteroid, (50, 50))
    laser_sound = pygame.mixer.Sound('Laser Blasts.wav')
    explosion_sound = pygame.mixer.Sound('explosion.wav')
    spaceship_explosion_sound = pygame.mixer.Sound('spaceship_explode.wav')
    pygame.mixer.music.load('soft-techno-music.mp3')
    pygame.mixer.music.play(-1, 6.3)
    window_width = 500
    window_height = 700
    screen = pygame.display.set_mode((window_width, window_height))
    background= pygame.image.load('space_background.png')
    background= pygame.transform.scale(background, (500, 700))
    pygame.display.set_caption("Astroid Shootin'")
    asteroid_list = []
    bullet_list = []
    pscore=0        #starting player score
    plives=3       #number of lives the player starts with
    level_time=80
    create_astroid_time=level_time
    #         R    G    B
    WHITE = (255, 255, 255)
    font = pygame.font.SysFont("monospace", 20)     #sets the font for scoring titles
    clock = pygame.time.Clock()
    player = Player((window_width / 2)-30, 600, 60, 60)
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(player)
    # This represents an asteroid
    first_asteroid = Asteroid(random.randrange(window_width-60), 50, 50, 50)
    asteroid_list.append(first_asteroid)
    all_sprites_list.add(first_asteroid)
    asteroid_counter=0
    bonus=False
    while True: #main game loop
        screen.blit(background, (0, 0))
        bullet_hit(asteroid_list, bullet_list)  # Check if laser hits asteroid
        check_hit(asteroid_list)  # Check if player hit by asteroid
        check_screen(asteroid_list, bullet_list)  # Check if anything off screen
        if create_astroid_time <= 0:  # This creates asteroids after set amount of time
            if asteroid_counter == 14:  #if the player has destroyed 14 asteroids, then it spawns a bonus asteroid worth 1000 points
                x=Bonus_Asteroid(random.randrange(window_width-60), -10, 50, 50)
                bonus=True
                asteroid_counter = 0
            else:
                x = Asteroid(random.randrange(window_width-60), -10, 50, 50)
                bonus=False
            asteroid_list.append(x)
            all_sprites_list.add(x)
            level_time -= 1  # each time an asteroid is formed we make it shorter until next is made
            create_astroid_time = level_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
            elif event.type == pygame.KEYUP:
                player.MoveKeyUp(event.key)
        for ent in all_sprites_list:
            ent.update()

        player_scoretxt = font.render("Player Score: {0}".format(pscore), 1, WHITE)  # updates player's score
        player_livestxt = font.render("Lives: {0}".format(plives),1, WHITE)
        screen.blit(player_scoretxt, (25, 10))  # displays player's score
        screen.blit(player_livestxt, (300, 10))
        all_sprites_list.draw(screen)
        create_astroid_time-=1
        if create_astroid_time<=-10:
            create_astroid_time=40
        pygame.display.flip()
        clock.tick(60)
def menu():
    global scoreslist
    try:
        scoreslist=[]
        spaceshipImg= pygame.image.load('Galaga_ship.png')
        spaceshipImg=pygame.transform.scale(spaceshipImg, (60, 60))
        asteroidIMg=pygame.image.load('asteroid.png')
        asteroidIMg =pygame.transform.scale(asteroidIMg, (50, 50))
        background= pygame.image.load('space_background.png')
        background= pygame.transform.scale(background, (500, 700))
        window_width = 500
        window_height = 700
        screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Astroid Shootin'")
        #         R    G    B
        WHITE = (255, 255, 255)
        clock = pygame.time.Clock()
        # gets highscores from highscore txt file
        infile = open("highscores.txt", "r")
        lines = infile.readlines()
        for line in lines:
            items = line.split()
            items = " ".join(items)
            if items in scoreslist:
                pass
            else:
                scoreslist.append(items)
        infile.close()
        while True:
            screen.blit(background, (0, 0))
            screen.blit(spaceshipImg,(220, 575))
            screen.blit(asteroidIMg, (220, 300))
            font1 = pygame.font.SysFont("monospace", 18)
            font2 = pygame.font.SysFont("monospace", 42)
            menu_titletxt= font2.render("ASTEROID SHOOTIN'", 3, WHITE)
            instructions_txt= font1.render("<Press space to start game>", 1, WHITE)
            font3 = pygame.font.SysFont("monospace", 28)
            scoreslist = sorted(scoreslist, key=int, reverse=True)
            highscores_txt = font3.render("HIGH SCORE: " + str(scoreslist[0]) , 3, WHITE)  # displays "HIGH SCORE"
            # displays all of the highscores
            screen.blit(highscores_txt, (135, 450))
            screen.blit(menu_titletxt, (35, 150))
            screen.blit(instructions_txt, (100, 650))
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key== K_SPACE:
                        main()
                    else:
                        pass
            pygame.display.flip()
            clock.tick(60)
    except FileNotFoundError:  # if highscores txt file doesn't exist, then it creates one
        scoreslist = ['7500', '6500', '5500', '4500', '3500', '2500', '1500', '1000', '500', '0']
        outfile = open("highscores.txt", "a")  # writes updated highscores to highscores txt file
        for i in scoreslist:
            outfile.write("".join(i) + "\n")
        outfile.close()
        showscores()
menu()
