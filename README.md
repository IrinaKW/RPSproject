Rock Paper Scissors Project
Documentation Guideline
Computer Vision Rock Paper Scissors is a project that uses Teachable Machine to train the model to distinct between 3 states or nothing.

Milestone 1
Google Teachable-Machine https://teachablemachine.withgoogle.com/ has been used to capture over 25 images of each state, followed by the trained model. Model has been dowloaded as h5 file. 


Milestone 2
All the required libraries:
    import cv2
    from keras.models import load_model
    import numpy as np
    import pandas as pd
    import time


Milestone 3
The program is using three functions as separate files
    comp_choice is the function that create a random choice of rock, paper or scissors.
    
    player_choice is the function that utilises the model, created in Milestone 1 step.
    The functon required the video input of the player captured by the build-in camera, that later is used to return the player choice.
    If the camera cannot recognise the choice, it asks the player to repeat the camera capturing process. 
    
    outcome is the function that produces the game outcome based on the previous input, computer and player.

    game is the key file with the function main that is being played while the player is interested to continue.
    The function displays the picture of the choices selected by player and computer.

Milestone 4



Conclusions
Model can be further used to training/rediction purposes or as a part of the game building process.
