# **********************************************
# Author: Zayaan Bhanwadia & Percy Zhao
# Date: June 15, 2022
# Program Name: The Math WIZ
# Description: Welcome to The Math WIZ, a game to help young kids learn simple math and have fun!
# *********************************************

# importing modules
import pygame
import random
import math
from pygame.color import THECOLORS
from pygame import mixer

# declaring game/review variables
stage = int(0)
kills = int(0)
vanquishes = int(0)
spares = int(0)
stage = int(0)
monsters = int(0)
lives = int()
correct = bool()
enemies = []

# declaring other variables
percent_score = int()
questions = int(0)
correct_answers = int(0)
test_taken = bool()

# initalize Pygame, display screen, and setting clock
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1020, 640))
pygame.display.set_caption('The Math WIZ')

# setting music
mixer.init()

# loading game/review images
heart = pygame.image.load('Images/heart.png')
heart = pygame.transform.scale(heart, (50, 50))

wizard = pygame.image.load('Images/wizard.png')
wizard = pygame.transform.scale(wizard, (200, 200))
screen.blit(wizard, (50, 300))

zombie = pygame.image.load('Images/zombie.png')
zombie = pygame.transform.scale(zombie, (150, 200))

fireball = pygame.image.load('Images/fireball.png')
fireball = pygame.transform.scale(fireball, (200, 100))

explode = pygame.image.load('Images/explode.png')
explode = pygame.transform.scale(explode, (200, 150))

shield = pygame.image.load('Images/shield.png')
shield = pygame.transform.scale(shield, (300, 300))

ice = pygame.image.load('Images/ice.png')
ice = pygame.transform.scale(ice, (200, 200))
ice = pygame.transform.rotate(ice, 90)

ghost = pygame.image.load('Images/ghost.png')
ghost = pygame.transform.scale(ghost, (200, 200))

skeleton = pygame.image.load('Images/skeleton.png')
skeleton = pygame.transform.scale(skeleton, (200, 200))

spider = pygame.image.load('Images/spider.png')
spider = pygame.transform.scale(spider, (200, 200))

slime = pygame.image.load('Images/slime.png')
slime = pygame.transform.scale(slime, (200, 150))
slime = pygame.transform.flip(slime, True, False)

boss = pygame.image.load('Images/hydra.png')
boss = pygame.transform.scale(boss, (350, 200))

spare = pygame.image.load('Images/spare.png')
spare = pygame.transform.scale(spare, (200, 200))

watch = pygame.image.load('Images/watch.png')
watch = pygame.transform.scale(watch, (75, 75))


# first font text function
def text(msg, colour, size, x, y):
    fonts = pygame.font.Font('Texts/Ancient Medium.ttf', size)
    text = fonts.render(msg, True, colour)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

# font for the game
def text_review(msg, colour, size, x, y):
    fonts = pygame.font.Font('Texts/times-new-roman.ttf', size)
    text = fonts.render(msg, True, colour)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

# defining a text function for lesson with a different font
def lessonsText(msg, colour, size, x, y):
    fonts = pygame.font.Font('Texts/TaiHeritagePro-Regular.ttf', size)
    text = fonts.render(msg, True, colour)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)
    
# button function
def button(x, y, w, h, msg):
    mouse = pygame.mouse.get_pos()
    button_img = pygame.image.load('Images/main_menu_button.png')
    button_img = pygame.transform.scale(button_img, (w, h))
    screen.blit(button_img, (x, y))

    # returning True if button is pressed
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if pygame.mouse.get_pressed()[0] == 1:
            return True

    smallText = pygame.font.Font("Texts/Ancient Medium.ttf", 36)
    text = smallText.render(msg, True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (x + (w / 2), y + (h / 2))
    screen.blit(text, text_rect)

# title screen function
def title():
    mixer.music.load('Music/title.wav')
    mixer.music.play(-1)
    running = True
    background = pygame.image.load('Images/title_screen.jpg')
    background = pygame.transform.scale(background, (1020, 640))

    while running:
        screen.blit(background, (0, 0))
        text('Trials of the Math Wizard', 'white', 40, 510, 30)
        text('Press the spacebar to continue.', 'white', 28, 510, 550)
        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # moving onto main menu if user presses spacebar
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
                    main_menu()

# main menu function
def main_menu():
    # using variables
    global questions
    global correct_answers
    global kills
    global spares
    global vanquishes
    global stage
    global correct
    global lives
    global monsters

    # playing music
    mixer.music.load('Music/back_music.wav')
    mixer.music.set_volume(0.2)
    mixer.music.play(-1)

    # reset all game and quiz variables
    kills = 0
    spares = 0
    vanquishes = 0
    stage = 0
    lives = 0
    monsters = 0
    questions = 0
    correct_answers = 0

    # title screen background
    background = pygame.image.load('Images/main_menu.jpg')
    background = pygame.transform.scale(background, (1220, 640))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # displaying buttons
        learning = button(200, 200, 200, 50, 'Lesson')
        animation = button(600, 200, 200, 50, 'Animation')
        test = button(100, 400, 200, 50, 'Quiz')
        results = button(400, 400, 200, 50, 'Results')
        exit = button(700, 400, 200, 50, 'Exit')

        pygame.display.update()
        screen.blit(background, (-75, 0))
        clock.tick(60)

        # checking if buttons are pressed and taking the user to the button's destination
        if learning:
            running = False
            lesson()
        if animation:
            running = False
            review()
        if test:
            running = False
            quiz(questions)
        if results:
            running = False
            result()
        if exit:
            running = False
            sources()

# page 1 lesson function
def lesson():
    background = pygame.image.load('Images/lesson_background.jpg')
    background = pygame.transform.scale(background, (1020, 640))
    while True:

        screen.blit(background, (0, 0))
        clock.tick(60)

        # display lesson text on multiple lines
        lessonsText('Order of Operations (BEDMAS)', 'white', 44, 510, 40)
        lessonsText('B| brackets: Make sure to evaluate brackets first ().', 'white', 20, 510, 215)
        lessonsText('E| exponents: Evaluate exponents second (a^x).', 'white', 20, 510, 255)
        lessonsText('D| divison: Divide and multiply next in the order they appear.', 'white', 20,
                    510, 295)
        lessonsText('M| multiplication: Multiply and divide in the order they appear.', 'white',
                    20, 510, 335)
        lessonsText('A| addition: Add and subtract in the order they appear last.', 'white', 20,
                    510, 375)
        lessonsText('S| subtraction: Subtract and add in the order they appear last.', 'white', 20,
                    510, 415)

        nextLesson = button(485, 500, 90, 60, 'Next')
        pygame.display.update()

        # checking if button is pressed and take user to lesson page 2
        if nextLesson:
            next_lesson()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

# page 2 lesson function
def next_lesson():
    background = pygame.image.load('Images/lesson_background.jpg')
    background = pygame.transform.scale(background, (1020, 640))
    while True:

        screen.blit(background, (0, 0))
        clock.tick(60)

        # display lesson text on multiple lines
        lessonsText('Simple Linear Equations', 'white', 44, 510, 40)
        lessonsText('To solve isolate the variable by doing opposite operations to both sides.', 'white', 20,
                    510, 230)
        lessonsText('Eg. 2x - 5 = 15 --> 2x - 5 + 5 = 15 + 5 --> 2x/2 = 20/2 --> x = 10 ', 'white', 19, 510, 265)
        lessonsText('Opposite of + is -, opposite of * is / and vice versa for both.', 'white', 20, 510, 295)
        lessonsText('The opposite of an exponent is the same exponent as a root.', 'white', 20, 510, 335)
        lessonsText('If you have brackets, evaluate them then isolate the variable', 'white', 20, 510, 375)
        lessonsText('Remember BEDMAS!', 'white', 20, 510, 415)

        back = button(575, 560, 280, 60, 'Back')
        mainMenu = button(175, 560, 280, 60, 'Return to main menu')
        pygame.display.update()

        # checking if buttons are pressed and take the user to a certain page
        if mainMenu:
            main_menu()
        if back:
            lesson()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

# quiz question function
def question(x, y, w, h, msg, answer):
    # using global variables
    global questions
    global correct_answers

    background = pygame.image.load('Images/stars.jpg')
    background = pygame.transform.scale(background, (1020, 640))
    mouse = pygame.mouse.get_pos()
    button = pygame.image.load('Images/main_menu_button.png')
    button = pygame.transform.scale(button, (w, h))
    screen.blit(button, (x, y))

    # checking if button is pressed
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if pygame.mouse.get_pressed()[0] == 1:

            # checking if the button is the correct answer
            if answer == msg:
                questions += 1
                correct_answers += 1
                screen.blit(background, (0, 0))
                text('Correct!', 'white', 80, 510, 320)
                pygame.display.update()
                quiz(questions)
            else:
                questions += 1
                screen.blit(background, (0, 0))
                text('Incorrect!', 'white', 80, 510, 320)
                pygame.display.update()
                quiz(questions)

    smallText = pygame.font.Font("Texts/Ancient Medium.ttf", 36)
    font = smallText.render(msg, True, (255, 255, 255))
    text_rect = font.get_rect()
    text_rect.center = (x + (w / 2), y + (h / 2))
    screen.blit(font, text_rect)

# quiz page function
def quiz(x):
    # using global variables
    global questions
    global correct_answers
    global percent_score
    global test_taken

    # setting a delay and making test_taken True so results update
    test_taken = True
    pygame.time.delay(1000)

    background = pygame.image.load('Images/stars.jpg')
    background = pygame.transform.scale(background, (1020, 640))
    screen.blit(background, (0, 0))

    # displaying questions
    if x == 0:
        text('What is 7 - 2 * 3?', 'yellow', 40, 510, 30)
    if x == 1:
        text('What is (8+3) - 11', 'yellow', 40, 510, 30)
    if x == 2:
        text('If 5x + 3 = 23, what is x?', 'yellow', 40, 510, 30)
    if x == 3:
        text('What is 4 - 1 * 3^2', 'yellow', 40, 510, 30)
    if x == 4:
        text('If x = 3 - 5 * 3, what is x?', 'yellow', 40, 510, 30)
    if x == 5:
        text("You got " + str(correct_answers) + "/5", 'yellow', 60, 510, 320)

    running = True
    while running:
        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # displaying multiple choice answers
        if x == 0:
            question(200, 200, 200, 50, '15', '1')
            question(600, 200, 200, 50, '1', '1')
            question(200, 400, 200, 50, '7', '1')
            question(600, 400, 200, 50, '8', '1')
        if x == 1:
            question(200, 200, 200, 50, '7', '0')
            question(600, 200, 200, 50, '6', '0')
            question(200, 400, 200, 50, '0', '0')
            question(600, 400, 200, 50, '1', '0')
        if x == 2:
            question(200, 200, 200, 50, '0', '4')
            question(600, 200, 200, 50, '1', '4')
            question(200, 400, 200, 50, '7', '4')
            question(600, 400, 200, 50, '4', '4')
        if x == 3:
            question(200, 200, 200, 50, '27', '-5')
            question(600, 200, 200, 50, '-5', '-5')
            question(200, 400, 200, 50, '8', '-5')
            question(600, 400, 200, 50, '2', '-5')
        if x == 4:
            question(200, 200, 200, 50, '-12', '-12')
            question(600, 200, 200, 50, '-6', '-12')
            question(200, 400, 200, 50, '14', '-12')
            question(600, 400, 200, 50, '15', '-12')
        if x == 5:
            # resetting all variables and displaying results page
            questions = 0
            percent_score = correct_answers / 5 * 100
            correct_answers = 0
            running = False
            result()

# results page function
def result():
    global correct_answers
    global percent_score
    global test_taken

    running = True
    background = pygame.image.load('Images/stars.jpg')
    background = pygame.transform.scale(background, (1020, 640))
    screen.blit(background, (0, 0))

    while running:
        # display an appropriate message depending on if the user has taken the test
        if test_taken:
            text('Your score is ' + str(percent_score) + '%', 'white', 48, 510, 230)
            retake = button(550, 460, 280, 70, 'Retake test?')
        else:
            text('You must take the test.', 'white', 48, 510, 230)
            retake = button(550, 460, 280, 70, 'Go to test?')

        clock.tick(60)
        return_main = button(200, 460, 280, 70, 'Return to main menu')
        pygame.display.update()

        # checking if the user decided to reuturn to main menu or retake the quiz
        if retake:
            quiz(questions)
        if return_main:
            main_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

# sources function
def sources():
    background = pygame.image.load('Images/sources.jpg')
    background = pygame.transform.scale(background, (1020, 2000))
    mixer.music.load('Music/sources.mp3')
    mixer.music.play()
    yCord = int(0)
    screen.blit(background, (0, yCord))

    pygame.display.update()
    pygame.time.delay(1000)

    # scrolling down the page by decreasing y cordinate
    while yCord > -1500:
        pygame.display.update()
        screen.blit(background, (0, yCord))
        yCord -= 3
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    pygame.time.delay(1220)
    pygame.quit()
    quit()


# *********************Game/Animation*********************#
# game questions
def question_review(x, y, w, h, msg, answer):
    # using global variables
    global stage
    global correct

    mouse = pygame.mouse.get_pos()
    button = pygame.image.load('Images/main_menu_button.png')
    button = pygame.transform.scale(button, (w, h))
    background = pygame.image.load('Images/grassland.jpg')
    background = pygame.transform.scale(background, (1020, 640))
    screen.blit(button, (x, y))

    # checking if user clicked a button
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if pygame.mouse.get_pressed()[0] == 1:

            # checking if correct answer is pressed
            if answer == msg:
                stage += 1
                correct = True
                screen.blit(background, (0, 0))
                text('Correct!', 'white', 80, 510, 320)
                pygame.display.update()
                pygame.time.delay(500)
                review()
            else:
                stage += 1
                correct = False
                screen.blit(background, (0, 0))
                text('Incorrect!', 'white', 80, 510, 320)
                pygame.display.update()
                pygame.time.delay(500)
                review()

    smallText = pygame.font.Font("Texts/times-new-roman.ttf", 36)
    font = smallText.render(msg, True, (255, 255, 255))
    text_rect = font.get_rect()
    text_rect.center = (x + (w / 2), y + (h / 2))
    screen.blit(font, text_rect)

# boss questions
def question_boss(x, y, w, h, msg, answer):
    # using global variables
    global stage
    global correct

    mouse = pygame.mouse.get_pos()
    button = pygame.image.load('Images/main_menu_button.png')
    button = pygame.transform.scale(button, (w, h))
    screen.blit(button, (x, y))

    # checking if user picked an answer
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if pygame.mouse.get_pressed()[0] == 1:

            # checking if user picked the correct answer
            if answer == msg:
                stage += 1
                correct = True
                boss_fight()
            else:
                stage += 1
                correct = False
                boss_fight()

    smallText = pygame.font.Font("Texts/times-new-roman.ttf", 36)
    text = smallText.render(msg, True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (x + (w / 2), y + (h / 2))
    screen.blit(text, text_rect)

# minigame review
def review():
    # using global variables
    global kills, counter, font, fonts
    global spares
    global vanquishes
    global stage
    global correct
    global lives
    global attack
    global monsters

    background = pygame.image.load('Images/grassland.jpg')
    background = pygame.transform.scale(background, (1020, 640))
    font = pygame.font.Font('Texts/times-new-roman.ttf', 36)
    screen.blit(background, (0, 0))

    screen.blit(wizard, (50, 300))

    rect = fireball.get_rect()
    rect.x = 600
    rect.y = 300

    rect3 = ice.get_rect()
    rect3.x = 200
    rect3.y = 300

    spare = pygame.image.load('Images/spare.png')
    spare = pygame.transform.scale(spare, (200, 200))

    # making a list with all enemy types
    enemies.append(zombie)
    enemies.append(ghost)
    enemies.append(skeleton)
    enemies.append(spider)
    enemies.append(slime)
    monster = enemies[monsters]

    running = True
    timer = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.USEREVENT:
                if not timer:
                    counter -= 1
                    if counter > 0:
                        fonts = str(counter).rjust(3)
        # prologue
        if stage == 0:
            text_review('You are a legendary wizard in the land of Runeterra, a peaceful land filled with magic.',
                        'black', 28, 510, 30)
            text_review('One day, monsters invaded the land, attacking cities and towns.', 'black', 30, 510, 60)
            text_review("It's your job as the math wizard to defeat them and bring peace to the land.", 'black', 30,
                        510, 90)
            text_review("Answer math questions correctly to deflect attacks and counterstrike.", 'black', 30, 510, 120)
            ready = button(400, 320, 200, 50, 'Ready?')
            
            # start game when ready
            if ready:
                font = pygame.font.Font('Texts/times-new-roman.ttf', 36)
                mixer.music.load('Music/battle.wav')
                mixer.music.set_volume(0.1)
                mixer.music.play(-1)
                stage += 1
                lives = 3
                review()

        # displaying lives
        if lives > 0:
            if lives > 0:
                screen.blit(heart, (50, 50))

            if lives > 1:
                screen.blit(heart, (100, 50))

            if lives > 2:
                screen.blit(heart, (150, 50))

        # displaying death after all lives lost
        if monsters > 0 and lives == 0:
            running = False
            death()

        if stage == 1:
            if monsters == 0:
                if timer:
                    counter = 10
                    fonts = '10'.rjust(3)
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    timer = False
                screen.blit(background, (0, 0))
                screen.blit(watch, (890, 30))
                screen.blit(font.render(fonts, True, (0, 0, 0)), (900, 48))
                text('What is 15 + 2 / 4 * 2?', 'white', 40, 510, 30)
                question_review(200, 200, 200, 50, '14', '17')
                question_review(600, 200, 200, 50, '16', '16')
                question_review(200, 400, 200, 50, '3', '17')
                question_review(600, 400, 200, 50, '15', '17')
                screen.blit(monster, (800, 300))
                screen.blit(wizard, (50, 300))

                # update hearts
                if lives > 0:
                    if lives > 0:
                        screen.blit(heart, (50, 50))

                    if lives > 1:
                        screen.blit(heart, (100, 50))

                    if lives > 2:
                        screen.blit(heart, (150, 50))
                pygame.display.update()
                clock.tick(60)

                if counter == 0:
                    stage += 1
                    correct = False
                    review()

            # display monsters
            if monsters == 1:
                if timer:
                    counter = 10
                    fonts = '10'.rjust(3)
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    timer = False
                screen.blit(background, (0, 0))
                screen.blit(watch, (890, 30))
                screen.blit(font.render(fonts, True, (0, 0, 0)), (900, 48))
                text('What is (10/2) ^ 2?', 'white', 40, 510, 30)
                question_review(200, 200, 200, 50, '25', '25')
                question_review(600, 200, 200, 50, '11', '25')
                question_review(200, 400, 200, 50, '3', '25')
                question_review(600, 400, 200, 50, '10', '25')
                screen.blit(monster, (800, 300))
                screen.blit(wizard, (50, 300))

                # update hearts
                if lives > 0:
                    if lives > 0:
                        screen.blit(heart, (50, 50))

                    if lives > 1:
                        screen.blit(heart, (100, 50))

                    if lives > 2:
                        screen.blit(heart, (150, 50))
                pygame.display.update()
                clock.tick(60)

                if counter == 0:
                    stage += 1
                    correct = False
                    review()

            if monsters == 2:
                if timer:
                    counter = 10
                    fonts = '10'.rjust(3)
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    timer = False
                screen.blit(background, (0, 0))
                screen.blit(watch, (890, 30))
                screen.blit(font.render(fonts, True, (0, 0, 0)), (900, 48))
                text('If x + 3 * 2 = 5, what is x?', 'white', 40, 510, 30)
                question_review(200, 200, 200, 50, '7', '-1')
                question_review(600, 200, 200, 50, '9', '-1')
                question_review(200, 400, 200, 50, '2', '-1')
                question_review(600, 400, 200, 50, '-1', '-1')
                screen.blit(monster, (800, 300))
                screen.blit(wizard, (50, 300))

                # update lives
                if lives > 0:
                    if lives > 0:
                        screen.blit(heart, (50, 50))

                    if lives > 1:
                        screen.blit(heart, (100, 50))

                    if lives > 2:
                        screen.blit(heart, (150, 50))
                pygame.display.update()
                clock.tick(60)

                if counter == 0:
                    stage += 1
                    correct = False
                    review()

            if monsters == 3:
                if timer:
                    counter = 10
                    fonts = '10'.rjust(3)
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    timer = False
                screen.blit(background, (0, 0))
                screen.blit(watch, (890, 30))
                screen.blit(font.render(fonts, True, (0, 0, 0)), (900, 48))
                text('What is 11 x 3 - 6?', 'white', 40, 510, 30)
                question_review(200, 200, 200, 50, '41', '27')
                question_review(600, 200, 200, 50, '23', '27')
                question_review(200, 400, 200, 50, '27', '27')
                question_review(600, 400, 200, 50, '33', '27')
                screen.blit(monster, (800, 300))
                screen.blit(wizard, (50, 300))

                # update hearts
                if lives > 0:
                    if lives > 0:
                        screen.blit(heart, (50, 50))

                    if lives > 1:
                        screen.blit(heart, (100, 50))

                    if lives > 2:
                        screen.blit(heart, (150, 50))
                pygame.display.update()
                clock.tick(60)

                if counter == 0:
                    stage += 1
                    correct = False
                    review()

            if monsters == 4:
                if timer:
                    counter = 10
                    fonts = '10'.rjust(3)
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    timer = False
                screen.blit(background, (0, 0))
                screen.blit(watch, (890, 30))
                screen.blit(font.render(fonts, True, (0, 0, 0)), (900, 48))
                text('If 5x + 2 = 22, what is x?', 'white', 40, 510, 30)
                question_review(200, 200, 200, 50, '11', '4')
                question_review(600, 200, 200, 50, '4', '4')
                question_review(200, 400, 200, 50, '7', '4')
                question_review(600, 400, 200, 50, '3.5', '4')
                screen.blit(monster, (800, 300))
                screen.blit(wizard, (50, 300))

                # updating hearts
                if lives > 0:
                    if lives > 0:
                        screen.blit(heart, (50, 50))

                    if lives > 1:
                        screen.blit(heart, (100, 50))

                    if lives > 2:
                        screen.blit(heart, (150, 50))
                pygame.display.update()
                clock.tick(60)

                if counter == 0:
                    stage += 1
                    correct = False
                    review()

            if monsters == 5:
                running = False
                monsters = 0
                stage = 0
                boss_fight()

        if stage == 2:
            if not correct:
                if rect.x > 150:
                    rect.x -= 6
                    screen.blit(background, (0, 0))
                    screen.blit(wizard, (50, 300))
                    screen.blit(monster, (800, 300))
                    screen.blit(fireball, rect)
                else:
                    screen.blit(background, (0, 0))
                    screen.blit(wizard, (50, 300))
                    screen.blit(monster, (800, 300))
                    screen.blit(explode, (50, 300))
                    pygame.display.update()
                    pygame.time.wait(2000)
                    lives -= 1
                    stage = 1
                    monsters += 1
                    review()
            else:
                if rect.x > 270:
                    rect.x -= 6
                    screen.blit(background, (0, 0))
                    screen.blit(wizard, (50, 300))
                    screen.blit(monster, (800, 300))
                    screen.blit(shield, (20, 270))
                    screen.blit(fireball, rect)
                else:
                    screen.blit(background, (0, 0))
                    screen.blit(wizard, (50, 300))
                    screen.blit(monster, (800, 300))
                    vanquishes += 1
                    stage += 1
                    review()
        if stage == 3:
            screen.blit(background, (0, 0))
            screen.blit(wizard, (50, 300))
            screen.blit(monster, (800, 300))
            attack = button(250, 200, 200, 50, 'Attack')
            spare = button(550, 200, 200, 50, 'Spare')
            if attack or spare:
                stage += 1
                review()

        if stage == 4:
            if attack:
                if rect3.x < 700:
                    rect3.x += 6
                    screen.blit(background, (0, 0))
                    screen.blit(wizard, (50, 300))
                    screen.blit(monster, (800, 300))
                    screen.blit(ice, rect3)
                else:
                    stage = 1
                    monsters += 1
                    kills += 1
                    review()
            else:
                screen.blit(spare, (400, 30))
                screen.blit(monster, (800, 300))
                pygame.display.update()
                pygame.time.wait(2000)
                stage = 1
                monsters += 1
                spares += 1
                review()

        pygame.display.update()
        clock.tick(60)

# boss fight screen
def boss_fight():
    # using global variables
    global monsters
    global stage
    global kills, counter, font, fonts
    global spares
    global vanquishes
    global stage
    global correct
    global lives
    global attack

    # drawing background and sprites
    background = pygame.image.load('Images/grassland.jpg')
    background = pygame.transform.scale(background, (1020, 640))
    pygame.time.wait(120)    
    font = pygame.font.Font('Texts/times-new-roman.ttf', 36)
    screen.blit(background, (0, 0))

    screen.blit(wizard, (50, 300))

    rect = fireball.get_rect()
    rect.x = 600
    rect.y = 300

    rect3 = ice.get_rect()
    rect3.x = 200
    rect3.y = 300

    screen.blit(boss, (800, 300))
    spare = pygame.image.load('Images/spare.png')
    spare = pygame.transform.scale(spare, (200, 200))

    timer = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.USEREVENT:
                if not timer:
                    counter -= 1
                    if counter > 0:
                        fonts = str(counter).rjust(3)

        # displaying lives
        if lives > 0:
            if lives > 0:
                screen.blit(heart, (50, 50))

            if lives > 1:
                screen.blit(heart, (100, 50))

            if lives > 2:
                screen.blit(heart, (150, 50))

        # display death page if user loses all lives
        if monsters > 0 and lives == 0:
            running = False
            death()

        if stage == 0:
            mixer.music.load('Music/boss.mp3')
            mixer.music.play()
            text_review('The final boss approaches...', 'black', 28, 510, 30)
            text_review('Defend 3 attacks before fighting back!', 'black', 28, 510, 60)
            pygame.display.update()
            pygame.time.wait(3000)
            stage += 1
            boss_fight()

        # boss fight questions
        if stage == 1:
            if monsters == 0:
                if timer:
                    counter = 10
                    fonts = '10'.rjust(3)
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    timer = False
                screen.blit(background, (0, 0))
                screen.blit(watch, (890, 30))
                screen.blit(font.render(fonts, True, 'black'), (900, 48))
                text('If 4x - 6 = 22, what is x?', 'white', 40, 510, 30)
                question_boss(200, 200, 200, 50, '11', '7')
                question_boss(600, 200, 200, 50, '4', '7')
                question_boss(200, 400, 200, 50, '7', '7')
                question_boss(600, 400, 200, 50, '3.5', '7')
                screen.blit(boss, (800, 300))
                screen.blit(wizard, (50, 300))

                # update hearts
                if lives > 0:
                    if lives > 0:
                        screen.blit(heart, (50, 50))

                    if lives > 1:
                        screen.blit(heart, (100, 50))

                    if lives > 2:
                        screen.blit(heart, (150, 50))

                # starting boss fight
                if counter == 0:
                    stage += 1
                    correct = False
                    boss_fight()
                pygame.display.update()
                clock.tick(60)

            if monsters == 1:
                if timer:
                    counter = 10
                    fonts = '10'.rjust(3)
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    timer = False
                screen.blit(background, (0, 0))
                screen.blit(watch, (890, 30))
                screen.blit(font.render(fonts, True, (0, 0, 0)), (900, 48))
                text('If 2x - 2 = 22 * 0, what is x?', 'white', 40, 510, 30)
                question_boss(200, 200, 200, 50, '2', '1')
                question_boss(600, 200, 200, 50, '4', '1')
                question_boss(200, 400, 200, 50, '1', '1')
                question_boss(600, 400, 200, 50, '3.5', '1')
                screen.blit(boss, (800, 300))
                screen.blit(wizard, (50, 300))

                # update hearts
                if lives > 0:
                    if lives > 0:
                        screen.blit(heart, (50, 50))

                    if lives > 1:
                        screen.blit(heart, (100, 50))

                    if lives > 2:
                        screen.blit(heart, (150, 50))
                if counter == 0:
                    stage += 1
                    correct = False
                    boss_fight()
                pygame.display.update()
                clock.tick(60)

            if monsters == 2:
                if timer:
                    counter = 10
                    fonts = '10'.rjust(3)
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    timer = False
                screen.blit(background, (0, 0))
                screen.blit(watch, (890, 30))
                screen.blit(font.render(fonts, True, (0, 0, 0)), (900, 48))
                text('If x^2 = 16, what is x?', 'white', 40, 510, 30)
                question_boss(200, 200, 200, 50, '11', '4')
                question_boss(600, 200, 200, 50, '4', '4')
                question_boss(200, 400, 200, 50, '7', '4')
                question_boss(600, 400, 200, 50, '3.5', '4')
                screen.blit(boss, (800, 300))
                screen.blit(wizard, (50, 300))

                # updating hearts
                if lives > 0:
                    if lives > 0:
                        screen.blit(heart, (50, 50))

                    if lives > 1:
                        screen.blit(heart, (100, 50))

                    if lives > 2:
                        screen.blit(heart, (150, 50))
                if counter == 0:
                    stage += 1
                    correct = False
                    boss_fight()
                pygame.display.update()
                clock.tick(60)

        # boss attack and player shield animations
        if stage == 2:
            if not correct:
                if rect.x > 150:
                    rect.x -= 6
                    screen.blit(background, (0, 0))
                    screen.blit(wizard, (50, 300))
                    screen.blit(boss, (800, 300))
                    screen.blit(fireball, rect)
                else:
                    screen.blit(background, (0, 0))
                    screen.blit(wizard, (50, 300))
                    screen.blit(boss, (800, 300))
                    screen.blit(explode, (50, 300))
                    pygame.display.update()
                    pygame.time.wait(1200)
                    lives -= 1
                    if monsters != 2:
                        stage = 1
                        monsters += 1
                        boss_fight()
                    else:
                        stage = 3
                        boss_fight()
            else:
                if rect.x > 270:
                    rect.x -= 6
                    screen.blit(background, (0, 0))
                    screen.blit(wizard, (50, 300))
                    screen.blit(boss, (800, 300))
                    screen.blit(shield, (20, 270))
                    screen.blit(fireball, rect)
                else:
                    screen.blit(background, (0, 0))
                    screen.blit(wizard, (50, 300))
                    screen.blit(boss, (800, 300))
                    stage += 1
                    boss_fight()

        # boss attack or spare choice
        if stage == 3:
            if monsters != 2:
                stage = 1
                monsters += 1
                boss_fight()
            else:
                screen.blit(background, (0, 0))
                screen.blit(wizard, (50, 300))
                screen.blit(boss, (800, 300))
                attack = button(250, 200, 200, 50, 'Attack')
                spare = button(550, 200, 200, 50, 'Spare')
                if attack or spare:
                    stage += 1
                    boss_fight()

        # boss attack or spare animation
        if stage == 4:
            if attack:
                if rect3.x < 600:
                    rect3.x += 6
                    screen.blit(background, (0, 0))
                    screen.blit(wizard, (50, 300))
                    screen.blit(boss, (800, 300))
                    screen.blit(ice, rect3)
                else:
                    vanquishes += 1
                    kills += 1
                    ending()

            else:
                screen.blit(spare, (400, 30))
                screen.blit(boss, (800, 300))
                pygame.display.update()
                pygame.time.wait(3000)
                vanquishes += 1
                spares += 1
                ending()
        pygame.display.update()

# game ending screen
def ending():
    # using global variables
    global vanquishes
    global kills
    global spares

    background = pygame.image.load('Images/grassland.jpg')
    background = pygame.transform.scale(background, (1020, 640))
    screen.blit(background, (0, 0))

    # playing music depending on the ending (outside of while loop so music doesn't break)
    if vanquishes == kills:
        mixer.music.load('Music/hero.wav')
        mixer.music.play(-1)
    elif vanquishes == spares:
        mixer.music.load('Music/peace.wav')
        mixer.music.play(-1)
    else:
        mixer.music.load('Music/neutral.mp3')
        mixer.music.play(-1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # displaying a button that takes user to main menu
        mainMenu = button(360, 550, 300, 50, 'Return to main menu')
        if mainMenu:
            running = False
            main_menu()

        # checking if the user killed all the monsters they defeated
        if vanquishes == kills:
            text('Hero ending', 'black', 80, 510, 40)
            text_review('You defeated the monsters, and are hailed as the hero of the land.', 'black', 30, 510, 100)
            text_review('Essentially no monsters remain, you wiped most of them all out.', 'black', 30, 510, 140)
            text_review('Through your fame, you enjoy your new life to the fullest.', 'black', 30, 510, 180)
            text_review('That is until the monsters returned years later.', 'black', 30, 510, 220)
            text_review('It seems a heroes job is never quite over.', 'black', 30, 510, 260)
            text_review('Before going into battle once more, you think to yourself.', 'black', 30, 510, 300)
            text_review('Is all this fighting really needed?', 'white', 30, 510, 360)

        # checking if user spared all the monsters they defeated
        elif vanquishes == spares:
            text('Peaceful ending', 'Black', 80, 510, 40)
            text_review('Defying all expectations, you spared the lives of all monsters you defeated.', 'black', 30,
                        510, 100)
            text_review('Because of your outstanding kindness, the monster boss called off the attack.', 'black', 30,
                        510, 140)
            text_review("It seems that monsters and humans don't have to be enemies after all.", 'black', 30, 510, 180)
            text_review('Your efforts have earned lasting peace for generations to come.', 'black', 30, 510, 220)
            text_review('You will be remembered as the legendary wizard who brought peace to the land.', 'black', 30,
                        510, 260)

        # display neutral ending if both conditions above are not met
        else:
            text('Neutral', 'black', 80, 510, 40)
            text_review('You have successfully repelled the monster invasion.', 'black', 30, 510, 100)
            text_review('Many have survived the battle, and are trying to regroup.', 'black', 30, 510, 140)
            text_review('They will attack again soon, and you are not safe yet.', 'black', 30, 510, 180)
            text_review("It's time to take up your weapon again, and defend your home.", 'black', 30, 510, 220)

        pygame.display.update()

# death message screen
def death():
    # setting death screen music and images
    background = pygame.image.load('Images/steel.png')
    background = pygame.transform.scale(background, (1020, 640))
    blood = pygame.image.load('Images/blood.png')
    blood = pygame.transform.scale(blood, (1020, 320))
    screen.blit(background, (0, 0))
    screen.blit(blood, (0, 0))
    blood = pygame.transform.rotate(blood, 180)
    screen.blit(blood, (0, 300))
    mixer.music.load('Music/death.wav')
    mixer.music.play(-1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # displaying a button that takes user to main menu
        mainMenu = button(360, 510, 300, 50, 'Return to main menu')
        if mainMenu:
            running = False
            main_menu()

        text_review('You died.', 'white', 80, 510, 320)
        pygame.display.update()

# calling main game function
title()