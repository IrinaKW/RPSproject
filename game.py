#%%

#libraries and functions
import os
import time
from time import sleep
import cv2 
from keras.models import load_model
import numpy as np
import pandas as pd

from comp_choice import comp_choice
from player_choice import player_choice
from outcome import outcome
from countdown import countdown

#Welcome part
os.system("cls")
print("==========================================================")
print('Hello there and Welcome to the Rock, Paper, Scissors game!')
print("==========================================================")
print("\nYou have 5 attempts to win.")
print('\n\nPlease enter your name', end='\r')
player=input('\nPlease type in your name  ').upper()
print(f"\n{player}, after the countdown of 5 seconds")
print("please hold your hand as rock, paper or scissors shape in front of the camera")
print("\n")

def main():
    game_options=['ROCK', 'PAPER','SCISSORS']
    images = {'ROCK':'rock.png', 'PAPER':'paper.png','SCISSORS':'scissors.png'}
    countdown(5)

    #Computer random choice
    comp_go=comp_choice(game_options)
    comp_im=images[comp_go]

    #Player visual choice
    player_go=player_choice()
    while player_go=='NONE':
        print('\nTRY AGAIN and show your choice to the camera')
        player_go=player_choice()

    player_im=images[player_go]

    #game outputs
    print(f"\nYou played played {player_go}")
    print('..........')
    print(f"\nComputer played {comp_go}")

    time.sleep(1)

    #show visual results
    font = cv2.FONT_HERSHEY_SIMPLEX
    img1 = cv2.imread(player_im)
    cv2.putText(img1, 
        'PLAYER', 
        (10, 10), 
        font, 1, 
        (255, 255, 255), 
        2, 
        cv2.LINE_4)
    img2 = cv2.imread(comp_im)
    cv2.putText(img2, 
        'COMPUTER', 
        (10, 10), 
        font, 1, 
        (255, 255, 255), 
        2, 
        cv2.LINE_4)
    Hori = np.concatenate((img1, img2), axis=1)
    cv2.imshow('THE GAME', Hori)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

    #results 
    res=outcome(player_go, comp_go)
    if res=='try':
        print('Try Again!\n')
    elif res=='c':
        print('You Lost this time\n')
        return ('c')
    else:
        print('You Won this time!\n')
        return('p')

#OUTCOME after 5 repetitions
p=0
c=0
t=0
while t<5:
    print(f"You have {5-t} tries")
    print(f"Current score is: \nYOU {p}: COMPUTER {c} ")
    k=main()
    t=t+1
    if k=='c': c=c+1
    elif k=='p': p=p+1
    os.system("cls") 

if p==c:
    print(f"\nIt is a DRAW: {p}:{c}")
elif p<c:
    print(f"\nYou Lost the Game: {p}:{c}\n Better Luck Next Time!")
else:
    print(f"\nYou WON the Game: {p}:{c}\n")
    img1 = cv2.imread('win.png')
    cv2.imshow('results', img1)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()
 # %%
