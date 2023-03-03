# File created by: Braeden Webb
# Edit for github

# import libraries
from time import sleep
from random import randint

# delays code
from time import sleep
# generates random result in rock, paper, scissors
from random import randint
# a game library for use with python
import pygame as pg
# os is a library that lets you manage file
import os

# stores where work is being done in game folder
game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 300
HEIGHT = 300
FPS = 30

# define colors (RGB) through tuples and integers
# tuples are immutable - cannot change once created
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initializes Pygame
pg.init()
# initializes Sound
pg.mixer.init()

# Sets ups screen to certain widtch & height
screen = pg.display.set_mode((WIDTH, HEIGHT))
# Sets window name
pg.display.set_caption(("Rock, Paper, Scissors"))
# Class ticks clock at frames per second
clock = pg.time.Clock()

# Takes images from folders and sets them to variables
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
# win/lose/tie images
win_image = pg.image.load(os.path.join(game_folder, 'win.png')).convert()
lose_image = pg.image.load(os.path.join(game_folder, 'lose.png')).convert()
tie_image = pg.image.load(os.path.join(game_folder, 'tie.png')).convert()
# user images
user_rock_image = pg.image.load(os.path.join(game_folder, 'user_rock.png')).convert()
user_paper_image = pg.image.load(os.path.join(game_folder, 'user_paper.png')).convert()
user_scissors_image = pg.image.load(os.path.join(game_folder, 'user_scissors.png')).convert()
# cpu images
cpu_rock_image = pg.image.load(os.path.join(game_folder, 'cpu_rock.png')).convert()
cpu_paper_image = pg.image.load(os.path.join(game_folder, 'cpu_paper.png')).convert()
cpu_scissors_image = pg.image.load(os.path.join(game_folder, 'cpu_scissors.png')).convert()

# Set Image Transparency
rock_image.set_colorkey(BLACK)
paper_image.set_colorkey(BLACK)
scissors_image.set_colorkey(BLACK)
win_image.set_colorkey(BLACK)
lose_image.set_colorkey(BLACK)
tie_image.set_colorkey(BLACK)
user_rock_image.set_colorkey(BLACK)
user_paper_image.set_colorkey(BLACK)
user_scissors_image.set_colorkey(BLACK)
cpu_rock_image.set_colorkey(BLACK)
cpu_paper_image.set_colorkey(BLACK)
cpu_scissors_image.set_colorkey(BLACK)

# Does not store pixels but instead where they are and how many they are in dimensions
# Allows for those values to changed and adjusted
rock_image_rect = rock_image.get_rect()
paper_image_rect = paper_image.get_rect()
scissors_image_rect = scissors_image.get_rect()
win_image_rect = win_image.get_rect()
lose_image_rect = lose_image.get_rect()
tie_image_rect = lose_image.get_rect()
user_rock_image_rect = rock_image.get_rect()
user_paper_image_rect = paper_image.get_rect()
user_scissors_image_rect = scissors_image.get_rect()
cpu_rock_image_rect = rock_image.get_rect()
cpu_paper_image_rect = paper_image.get_rect()
cpu_scissors_image_rect = scissors_image.get_rect()

# Sets image coordinates
rock_image_rect.x = 0
rock_image_rect.y = 50
paper_image_rect.x = 100
paper_image_rect.y = 50
scissors_image_rect.x = 200
scissors_image_rect.y = 50
user_rock_image_rect.x = 0
user_rock_image_rect.y = 50
user_paper_image_rect.x = 100
user_paper_image_rect.y = 50
user_scissors_image_rect.x = 200
user_scissors_image_rect.y = 50
cpu_rock_image_rect.x = 0
cpu_rock_image_rect.y = 150
cpu_paper_image_rect.x = 100
cpu_paper_image_rect.y = 150
cpu_scissors_image_rect.x = 200
cpu_scissors_image_rect.y = 150
# win/lose/tie
win_image_rect.x = 50
win_image_rect.y = 125
lose_image_rect.x = 50
lose_image_rect.y = 125
tie_image_rect.x = 50
tie_image_rect.y = 125


# Sets variable, running, to True
running = True

###### Preparation ######

print("Let's play:")

# Defines choices
choices = ["rock", "paper", "scissors"]

for i in choices:
    print(i)

# Computer randomly decides
def cpu_randchoice():
    choice = choices[randint(0,2)]
    print("computer randomly decides..." + choice)
    return choice
# allows user to choose something

player_choice = "nothing"
cpu_choice = "cpu_nothing"

###### Primary Game Loop ######
while running:
    clock.tick(FPS)

    # event is anytime the user does something with the computer
    for event in pg.event.get():
        # If this event occurs, running set to False
        if event.type == pg.QUIT:
            running = False
        # Sets event when mouse button is released
        if event.type == pg.MOUSEBUTTONUP:
            # Gets their individual coordinates of x and y value and prints them
            # Tuple 0 = x
            print(pg.mouse.get_pos()[0])
            # Tuple 1 = y
            print(pg.mouse.get_pos()[1])
            
            # Creates variable for mouse position
            mouse_coords = pg.mouse.get_pos()

            # rock check
            if rock_image_rect.collidepoint(mouse_coords):
                print("user clicked on rock")
                player_choice = "rock"
                cpu_choice = cpu_randchoice()
            # paper check
            elif paper_image_rect.collidepoint(mouse_coords):
                print("user clicked on paper")
                player_choice = "paper"
                cpu_choice = cpu_randchoice()
            # scissor check
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("user clicked on scissors")
                player_choice = "scissors"
                cpu_choice = cpu_randchoice()
            # if nothing is chosen
            else:
                print("user clicked on nothing")
                cpu_choice = cpu_randchoice()
            # returns true or false 
            # print(rock_image_rect.collidepoint(mouse_coords))
            # print(paper_image_rect.collidepoint(mouse_coords))
            # print(scissors_image_rect.collidepoint(mouse_coords))

    ###### input ######
    # HCU - Human Computer Interaction
    # keyboard, mouse, controller, vr headset

    ###### update ######

    ###### draw ######
    
    screen.fill(BLACK)
    screen.blit(rock_image, rock_image_rect)
    screen.blit(paper_image, paper_image_rect)
    screen.blit(scissors_image, scissors_image_rect)

    # draw user choice

    if player_choice == "rock":
        screen.fill(BLACK)
        screen.blit(user_rock_image, user_rock_image_rect)
        
    if player_choice == "paper":
        screen.fill(BLACK)
        screen.blit(user_paper_image, user_paper_image_rect)

    if player_choice == "scissors":
        screen.fill(BLACK)
        screen.blit(user_scissors_image, user_scissors_image_rect)

    # draw computer choice

    if cpu_choice == "rock":
        screen.blit(cpu_rock_image, cpu_rock_image_rect)
        break

    if cpu_choice == "paper":
        screen.blit(cpu_paper_image, cpu_paper_image_rect)
        break

    if cpu_choice == "scissors":
        screen.blit(cpu_scissors_image, cpu_scissors_image_rect)
        break

    pg.display.flip()

    # Comparison
    
    # Tie
    if player_choice == cpu_choice:
        screen.blit(tie_image, tie_image_rect)
    
    # Win
    elif player_choice == "rock" and cpu_choice == "scissors":
        screen.blit(win_image, win_image_rect)
    elif player_choice == "paper" and cpu_choice == "rock":
        screen.blit(win_image, win_image_rect)
    elif player_choice == "scissors" and cpu_choice == "paper":
        screen.blit(win_image, win_image_rect)

    # Lose
    elif player_choice == "scissors" and cpu_choice == "rock":
        screen.blit(lose_image, lose_image_rect)
    elif player_choice == "rock" and cpu_choice == "paper":
        screen.blit(lose_image, lose_image_rect)
    elif player_choice == "paper" and cpu_choice == "scissors":
        screen.blit(lose_image, lose_image_rect)
    

    # # If anything but rock, paper, or scissors is chosen by user
    # else:
    #     print("error")
    
pg.quit()