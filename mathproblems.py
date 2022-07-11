import random

import time

def addition(firstNumber, secondNumber):
    trueAnswer = firstNumber + secondNumber

    return trueAnswer

def subtraction(firstNumber, secondNumber):
    trueAnswer = firstNumber - secondNumber

    return trueAnswer

def multiplication(firstNumber, secondNumber):
    trueAnswer = firstNumber * secondNumber

    return trueAnswer

def division(firstNumber, secondNumber):
    trueAnswer = firstNumber/secondNumber

    return trueAnswer


def playingGame():

    firstNumber = random.randint(0, 12)

    secondNumber = random.randint(0,12)

    numOfPoints = 0


    print("---------------------------------")

    if(questionType == 'A'):
        print(firstNumber, "+", secondNumber)
    elif(questionType == 'S'):
        print(firstNumber, "-", secondNumber)
    elif(questionType == 'M'):
        print(firstNumber, "*", secondNumber)
    else:
        print(firstNumber, "/", secondNumber)

    userAnswer = float(input("--> "))

    if(questionType == 'A'):
        trueAnswer = addition(firstNumber, secondNumber)
    elif(questionType == 'S'):
        trueAnswer = subtraction(firstNumber, secondNumber)
    elif(questionType == 'M'):
        trueAnswer = multiplication(firstNumber, secondNumber)
    else:
        trueAnswer = division(firstNumber, secondNumber)

    print("This is the true answer:", trueAnswer)

    if(userAnswer == trueAnswer):
        numOfPoints = numOfPoints + 1
    
    return numOfPoints




print("Welcome to the math problems Website")

questionType = input("Addition (A)/ Subtraction (S)/ Multiplication (M)/ Division (D)")


# if(gameMode == 1):

numberOfQuestions = int(input("How many questions do you want to answer?"))

    #Random number generator

i = 0

myPoints = 0

for i in range(numberOfQuestions):

    totalPoints = playingGame()

    print("This is the total Points", totalPoints)

    myPoints += totalPoints

    i = i + 1

print("You got a total of", myPoints, "questions right!")
    #Implement time?


# -- TIMING MODE --


# else:

#     def countdown(t):
        
#         while t:
#             mins, secs = divmod(t, 60)
#             timer = 'TIME: {:02d}:{:02d}'.format(mins, secs)
#             print(timer, end="\r")
#             time.sleep(1)
#             t -= 1

#         numOfPoints = playingGame()
        

#         print('Fire in the hole!!')
#         print("You got", numOfPoints, "points")
    
    
#     # input time in seconds
#     t = int(input("Please input whether you would like to set timer to 30 seconds (30), or a minute (60)"))

#     if(t == 30):
#         countdown(30)
#     else:
#         countdown(60)
    
#     # function call
#     countdown(int(t))