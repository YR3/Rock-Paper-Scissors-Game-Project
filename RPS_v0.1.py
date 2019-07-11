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

    def learn_name(self, name):
        self.name = input("Your Name Please?\n".title())
        

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player): # Random Player Behavior Template
    def move(self):
        return random.choice(moves)

class Jack(RandomPlayer): # Computer Player 1
    pass        

class John(RandomPlayer): # Computer Player 2
    pass

class HumanPlayer(Player): # Human Player Actions
    def move(self):
        action = input('rock, paper, scissors? >')
        while action != 'rock'and action != 'paper'and action != 'scissors':
            print('Sorry try again.')
        return(action)
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f" " + input('Your Name Please?\n') + ":" + f" {move1}  John: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print(self.p1.name + ' won!')
        elif self.p1.score < self.p2.score:
            print(self.p2.name + ' won!')
        else:
            print('The game was a tie!')
        print('The final score is: ' + str(self.p1.score) + ' TO ' +
              str(self.p2.score))
        print("Game over!")


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
