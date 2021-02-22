import math
import random

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()


# this is the cod for the main screen
# create the screen
screen = pygame.display.set_mode((800, 600))

# background
img = 'C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/background.png'
background = pygame.image.load(img)

# background sound
mixer.music.load("C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/background music.mp3")
mixer.music.play(-1)

# caption and icon
pygame.display.set_caption("Main Screen")
icon = pygame.image.load("C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/alien aicon.png")
pygame.display.set_icon(icon)

# defining a font
bigfont = pygame.font.SysFont('Corbel', 80)

# rendering a text written in
# this font
one_text = bigfont.render('To The Game', True, (255, 255, 255))
two_text = bigfont.render('Lead Bourd', True, (255, 255, 255))

#choose wich screen
wich_bourd = "null"


run = True
while run:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if the mouse is clicked on the
            # button the game is terminated
            # mouse[0]= x cordinats
            # mouse[1]= y cordinats
            if 30 <= mouse[0] <= 450 and 100 <= mouse[1] <= 250:
                wich_bourd = "choose_hoe_many_players"
                run = False
            if 30 <= mouse[0] <= 450 and 350 <= mouse[1] <= 500:
                wich_bourd = "lead_bourd"
                run = False

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # this is for the button for one player
    # if mouse is hovered on a button it
    # changes to lighter shade
    if 30 <= mouse[0] <= 370 and 250 <= mouse[1] <= 400:
        # screen = where to put the button (when the mouse flot on the button)
        # (0,0,0) the color of the button (when the mouse flot on the button)
        # 30 the width for the button change (when the mouse flot on the button)
        # 100, the height for the button change (when the mouse flot on the button)
        # 420, 150 the size of the button (when the mouse flot on the button)
        pygame.draw.rect(screen, (0, 0, 0), [30, 100, 420, 150])
    else:
        # screen = where to put the button
        # (0,0,0) the color of the button
        # 30 the width for the button
        # 100 the height for the button
        # 420, 150 the size of the button
        pygame.draw.rect(screen, (0, 0, 0), [30, 100, 420, 150])

    # this is for the button for two players
    # if mouse is hovered on a button it
    # changes to lighter shade
    if 400 <= mouse[0] <= 700 and 250 <= mouse[1] <= 400:
        # screen = where to put the button (when the mouse flot on the button)
        # (0,0,0) the color of the button (when the mouse flot on the button)
        # 30 the width for the button change (when the mouse flot on the button)
        # 350, the height for the button change (when the mouse flot on the button)
        # 420, 150 the size of the button (when the mouse flot on the button)
        pygame.draw.rect(screen, (0, 0, 0), [30, 350, 420, 150])
    else:
        # screen = where to put the button
        # (0,0,0) the color of the button
        # 30 the width for the button
        # 350 the height for the button
        # 420, 150 the size of the button
        pygame.draw.rect(screen, (0, 0, 0), [30, 350, 420, 150])

    # superimposing the text onto our button
    # the first is for x place  for the text
    # the scoend is for y place for the text
    screen.blit(one_text, (30, 140))
    screen.blit(two_text, (55, 380))

    # updates the frames of the game
    pygame.display.update()





# this is the cod for the choose how many players screen
if(wich_bourd == "choose_hoe_many_players"):

    # create the screen
    screen = pygame.display.set_mode((800, 600))

    # background
    img = 'C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/background.png'
    background = pygame.image.load(img)

    # caption and icon
    pygame.display.set_caption("Choose How Many Players Screen")
    icon = pygame.image.load("C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/alien aicon.png")
    pygame.display.set_icon(icon)

    # stores the width of the
    # screen into a variable
    width = screen.get_width()

    # stores the height of the
    # screen into a variable
    height = screen.get_height()

    # defining a font
    bigfont = pygame.font.SysFont('Corbel', 80)

    # rendering a text written in
    # this font
    one_text = bigfont.render('one player', True, (255, 255, 255))
    two_text = bigfont.render('two players', True, (255, 255, 255))

    how_many_players = 0

    run = True
    while run:

        # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))
        # Background Image
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the
                # button the game is terminated
                # mouse[0]= x cordinats
                # mouse[1]= y cordinats
                if 30 <= mouse[0] <= 370 and 250 <= mouse[1] <= 400:
                    how_many_players = 1
                    run = False
                if 400 <= mouse[0] <= 760 and 250 <= mouse[1] <= 400:
                    how_many_players = 2
                    run = False

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        # this is for the button for one player
        # if mouse is hovered on a button it
        # changes to lighter shade
        if 30 <= mouse[0] <= 370 and 250 <= mouse[1] <= 400:
            # screen = where to put the button (when the mouse flot on the button)
            # (0,0,0) the color of the button (when the mouse flot on the button)
            # [60 the width for the button change (when the mouse flot on the button)
            # 250, the height for the button change (when the mouse flot on the button)
            # 300, 150 the size of the button (when the mouse flot on the button)
            pygame.draw.rect(screen, (0, 0, 0), [30, 250, 340, 150])
        else:
            # screen = where to put the button
            # (0,0,0) the color of the button
            # 60 the width for the button
            # 250 the height for the button
            # 340, 150 the size of the button
            pygame.draw.rect(screen, (0, 0, 0), [30, 250, 340, 150])

        # this is for the button for two players
        # if mouse is hovered on a button it
        # changes to lighter shade
        if 400 <= mouse[0] <= 700 and 250 <= mouse[1] <= 400:
            # screen = where to put the button (when the mouse flot on the button)
            # (0,0,0) the color of the button (when the mouse flot on the button)
            # [60 the width for the button change (when the mouse flot on the button)
            # 250, the height for the button change (when the mouse flot on the button)
            # 300, 150 the size of the button (when the mouse flot on the button)
            pygame.draw.rect(screen, (0, 0, 0), [400, 250, 365, 150])
        else:
            # screen = where to put the button
            # (0,0,0) the color of the button
            # 60 the width for the button
            # 250 the height for the button
            # 340, 150 the size of the button
            pygame.draw.rect(screen, (0, 0, 0), [400, 250, 365, 150])

        # superimposing the text onto our button
        # the first is for x place  for the text
        # the scoend is for y place for the text
        screen.blit(one_text, (30, 280))
        screen.blit(two_text, (400, 280))

        # updates the frames of the game
        pygame.display.update()





#the cod for the lead bourd
if(wich_bourd == "lead_bourd"):

    # create the screen
    screen = pygame.display.set_mode((800, 600))

    # background
    img = 'C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/background.png'
    background = pygame.image.load(img)

    # caption and icon
    pygame.display.set_caption("Lead Bourd Screen")
    icon = pygame.image.load("C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/alien aicon.png")
    pygame.display.set_icon(icon)

    # lead bourd text
    leadbourd_font = pygame.font.Font('freesansbold.ttf', 70)


    def lead_bourd_text():
        leadbourd_text = leadbourd_font.render("Lead Bourd", True, (0, 128, 0))
        screen.blit(leadbourd_text, (200, 0))


    run = True
    while run:

        # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))
        # Background Image
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        lead_bourd_text()

        pygame.display.update()





# the cod for the game
# this is the cod for the game screen
screen = pygame.display.set_mode((800, 600))

# background
img = 'C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/background.png'
background = pygame.image.load(img)

# caption and icon
pygame.display.set_caption("Space Game")
icon = pygame.image.load("C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/alien aicon.png")
pygame.display.set_icon(icon)

# Player1
player1Img = pygame.image.load('C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/spaceship.png')
player1X = 160
player1Y = 480
player1X_change = 0

# Player2
player2Img = pygame.image.load('C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/spaceship2.png')
player2X = 580
player2Y = 480
player2X_change = 0

# coin
coinImg = pygame.image.load('C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/xp.png')
coinX = random.randint(0, 735)
coinY = 70
coinY_change = 2
time_for_coin = 0
time_to_start_coin = random.randint(500, 800)

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 11

for i in range(num_of_enemies):
    enemyImg.append(
        pygame.image.load('C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/alien.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 250))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet for player 1
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bullet1Img = pygame.image.load('C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/bullet.png')
bullet1X = 0
bullet1Y = 480
bullet1X_change = 0
bullet1Y_change = 35
bullet1_state = "ready"

# Bullet for player 2
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bullet2Img = pygame.image.load('C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/bullet.png')
bullet2X = 0
bullet2Y = 480
bullet2X_change = 0
bullet2Y_change = 35
bullet2_state = "ready"

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 335
textY = 10

# game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score:" + " " + str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player1(x, y):
    screen.blit(player1Img, (x, y))


def fire_bullet1(x, y):
    global bullet1_state
    bullet1_state = "fire"
    screen.blit(bullet1Img, (x + 20, y + 10))


def isCollision1(enemyX, enemyY, bullet1X, bullet1Y):
    distance = math.sqrt((math.pow(enemyX - bullet1X, 2)) + (math.pow(enemyY - bullet1Y, 2)))
    if (distance < 27):
        return True
    else:
        return False


def player2(x, y):
    screen.blit(player2Img, (x, y))


def fire_bullet2(x, y):
    global bullet2_state
    bullet2_state = "fire"
    screen.blit(bullet2Img, (x + 20, y + 10))


def isCollision2(enemyX, enemyY, bullet2X, bullet2Y):
    distance = math.sqrt((math.pow(enemyX - bullet2X, 2)) + (math.pow(enemyY - bullet2Y, 2)))
    if (distance < 27):
        return True
    else:
        return False


def coin(x, y):
    screen.blit(coinImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# the tnai if there is going to be 1 or 2 players
if (how_many_players != 2):
    player2X = 1200

# game loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

        # if keystroke is pressed check whether its right or left for player1
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                player1X_change = -5
            if (event.key == pygame.K_RIGHT):
                player1X_change = 5
            if (event.key == pygame.K_SPACE):
                if (bullet1_state == "ready"):
                    bullet1_Sound = mixer.Sound(
                        "C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/gun sound.mp3")
                    bullet1_Sound.play()
                    # Get the current x cordinate of the spaceship
                    bullet1X = player1X
                    fire_bullet1(bullet1X, bullet1Y)
            if (how_many_players == 2):
                # if keystroke is pressed check whether its right or left for player2
                if (event.key == pygame.K_d):
                    player2X_change = 5
                if (event.key == pygame.K_a):
                    player2X_change = -5
                if (event.key == pygame.K_f):
                    if (bullet2_state == "ready"):
                        bullet2_Sound = mixer.Sound(
                            "C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/gun sound.mp3")
                        bullet2_Sound.play()
                        # Get the current x cordinate of the spaceship
                        bullet2X = player2X
                        fire_bullet2(bullet2X, bullet2Y)

        # make shur that if you dont press any button the space sip dont move
        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                player1X_change = 0

        # make shur that if you dont press any button the space sip dont move
        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_a or event.key == pygame.K_d):
                player2X_change = 0

    # chacking for bounderies of player1 so it doesn't go out of bounds
    player1X += player1X_change
    if (player1X <= 0):
        player1X = 0
    elif (player1X >= 736):
        player1X = 736

    if (how_many_players == 2):
        # chacking for bounderies of player2 so it doesn't go out of bounds
        player2X += player2X_change
        if (player2X <= 0):
            player2X = 0
        elif (player2X >= 736):
            player2X = 736

    # enemy movement
    for i in range(num_of_enemies):
        # game over
        if (enemyY[i] > 440):
            for j in range(num_of_enemies):
                enemyY[j] = 2000
                time_for_coin = 1000

            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if (enemyX[i] <= 0):
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif (enemyX[i] >= 736):
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]

        # Collision player1
        collision1 = isCollision1(enemyX[i], enemyY[i], bullet1X, bullet1Y)
        if collision1:
            explosion_Sound = mixer.Sound(
                "C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/explosion sound.mp3")
            explosion_Sound.play()
            bullet1Y = 480
            bullet1_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

        # Collision player2
        collision2 = isCollision2(enemyX[i], enemyY[i], bullet2X, bullet2Y)
        if collision2:
            explosion_Sound = mixer.Sound(
                "C:/Users/עמית/PycharmProjects/pythonProject3/Submission_tasks/may game/explosion sound.mp3")
            explosion_Sound.play()
            bullet2Y = 480
            bullet2_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet1 Movement
    if (bullet1Y <= 0):
        bullet1Y = 480
        bullet1_state = "ready"

    if (bullet1_state == "fire"):
        fire_bullet1(bullet1X, bullet1Y)
        bullet1Y -= bullet1Y_change

    # Bullet2 Movement
    if (bullet2Y <= 0):
        bullet2Y = 480
        bullet2_state = "ready"

    if (bullet2_state == "fire"):
        fire_bullet2(bullet2X, bullet2Y)
        bullet2Y -= bullet1Y_change

    # this ifs make the coin to fall down and the player1 to catch him
    if (time_for_coin == time_to_start_coin):
        coinY += coinY_change
        if (abs(coinX - player1X) <= 25) and (abs(coinY - player1Y) <= 25):
            score_value = score_value + 1
            time_for_coin = 0
            coinX = 900
            coinY = 70
        elif (coinY == 600):
            time_for_coin = 0
            coinX = 900
            coinY = 70
    elif (time_for_coin == time_to_start_coin - 1):
        coinX = random.randint(0, 735)
        time_for_coin = time_for_coin + 1
    else:
        coinX = 900
        time_for_coin = time_for_coin + 1

    # this ifs make the coin to fall down and the player2 to catch him
    if (time_for_coin == time_to_start_coin):
        coinY += coinY_change
        if (abs(coinX - player2X) <= 25) and (abs(coinY - player2Y) <= 25):
            score_value = score_value + 1
            time_for_coin = 0
            coinX = 900
            coinY = 70
        elif (coinY == 600):
            time_for_coin = 0
            coinX = 900
            coinY = 70
    elif (time_for_coin == time_to_start_coin - 1):
        coinX = random.randint(0, 735)
        time_for_coin = time_for_coin + 1
    else:
        coinX = 900
        time_for_coin = time_for_coin + 1

    player1(player1X, player1Y)
    player2(player2X, player2Y)
    show_score(textX, textY)
    coin(coinX, coinY)

    pygame.display.update()
