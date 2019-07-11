#!/usr/bin/env python3
# Yazeed M. Al`Fadani`s Rock, Paper, Scissor Project
# For Udacity`s Connect Into to Programming course
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:  # Parent Player Template
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    
        

    def learn(self, my_move , their_move):
        pass

class RandomPlayer(Player): # Random Player Behavior Template
    def move(self):
        return random.choice(moves)

class ReflectPlayer(Player): # First Play is Always a Rock
    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def move(self):
        if self.their_move is None:
            play = moves[0]               
        else:
            play = self.their_move             
            return (play)  

    def learn(self, my_move, their_move):
        self.their_move = their_move

class CyclePlayer(Player): 
    def __init__(self):
        Player.__init__(self)
        self.my_move = None

    def move(self):
            play = None
            if self.my_move is None:
                play = Player.move(self)
            else:
                index = moves.index(self.my_move) + 1
                if index >= len(moves):
                    index = 0
                play = moves[index]
            self.my_move = play
            return play   

class HumanPlayer(Player): # Human Player Actions
    def move(self):
        action = input('rock, paper, scissors? >')
        while action not in moves:
            action = input('Sorry try again. >')
        return(action)

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game: # Game Engine!
    def __init__(self, p1, p2):
        self.p1 = HumanPlayer()
        self.p2 = CyclePlayer()
    
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}")
        print(f"John played {move2}")
        if beats(move1, move2):
            print ("Victory!")
            print(f"Score: You: {move1}  John: {move2}\n\n")
            self.p1.score += 1
            return 1
        elif beats(move2, move1):
            print ("John Wins You Lose!")
            print(f"Score: You: {move1}  John: {move2}\n\n")
            self.p2.score += 1
            return 2
        else:
            print ("Draw!!")
            print(f"Score: You: {move1}  John: {move2}\n\n")
            return 0

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print('You won!')
        elif self.p1.score < self.p2.score:
            print('John Won!')
        else:
            print('The game was a tie!')
        print('The final score is: ' + str(self.p1.score) + ' TO ' +
              str(self.p2.score))
        print("Game over!")


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
