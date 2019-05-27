'''
Goal : Creating a hangman game to improve my programming logic

Task : 2 users to play a game where one user inputs a word and the other has to
        guess the word before he is hung

'''
import re
import turtle
##Makes sure user input is inputted correctly
##and catches errors if any arise

def drawHangman(counter):
  
  def drawNoose():
    turtle.speed(10)
    turtle.color("Black")
    turtle.forward(120)
    turtle.forward(-60)
    turtle.left(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    
  def drawHead():
    turtle.circle(15)
    turtle.circle(15, 180) # draw a semicircle
    turtle.right(90)
    
  def drawArms():
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(20)
    turtle.forward(-40)
    turtle.forward(20)
    turtle.right(90)
    
  def drawTorso():
    turtle.forward(30)
    
  def drawLegs():
    turtle.left(45)
    turtle.forward(30)
    turtle.forward(-30)
    turtle.right(90)
    turtle.forward(30)
    turtle.forward(-30)
    turtle.left(45)
    
  if counter==0:
    drawNoose()
  elif counter==1:
    drawNoose()
    drawHead()
  elif counter==2:
    drawArms()
  elif counter==3:
    drawTorso()
  elif counter==4:
    drawLegs()
  elif counter==5:
      print('You have DIED')

def start():
    
    one = 0
    while one < 1:
        try:
            ask = input('Player 1, what is the secret word?  ')
            if len(ask) > 0 and ask.isalpha():
                ask1 = ask.lower()
                one = 1
            else:
                raise TypeError
        
        except TypeError:
            print('Only input letters')
        except EOFError:
            print('You have to input something')

    len_1 = len(ask1)
    ## Contains length of word to check if user guessed correctly

    no_of_tries = 0
    ## Incremented to 11 for hanging
    guessed_letters = []
    mistakes = 0
    guessed_letters_correct = []
    ## Length of answers which are right

    while mistakes < 5:
        len_2 = len(guessed_letters_correct)
        try:
            if len_1 == len_2:
                print('Player 2 wins')
                break

            ask2 = input('Player 2, guess your letter')
            ask2 = ask2.lower()
            if ask2 in guessed_letters:
                print('You already guessed this letter')
                print(ask2)
                
            
            elif len(ask2)==1 and ask2.isalpha():
                guessed_letters.append(ask2)
                no_of_tries +=1
                if ask2 in ask1:
                    guessed_letters_correct.append(ask2)
                    print('Correct')
                    print(guessed_letters_correct)
                else:
                    mistakes +=1
                    drawHangman(mistakes)
                    print('Incorrect')
                    print(guessed_letters)
                    continue
            else:
                raise TypeError
            
        except TypeError:
            print('Letters only please')
            continue
        except EOFError:
            print('You have to input something')
            continue


    if len_1 != len_2:
        print('Player 1 wins')

    print(guessed_letters)
    print(guessed_letters_correct)
    


start()
