import pickle
import random

import pygame
import math

from pygame import font

from NeuralNetwork import NeuralNetwork
import numpy as np

class Bar:
    def __init__(self):
        self.length = 120
        self.height = 16
        self.bar_x = (Game.width-self.length)/2
        self.bar_y = Game.height-self.height
        self.center_x = (Game.width/2)
        self.center_y = Game.height-(self.height/2)
        self.radius = 15
        self.ball_x = self.center_x
        self.ball_y = self.bar_x+(self.length)/2-(2*self.radius)
        self.ball_center_x = random.randrange(15,Game.width-15)
        self.ball_center_y = random.randrange(Game.height)
        self.ball_vel_x = 10
        self.ball_vel_y = 10
        self.bar_vel = 0
        self.score = 0
        self.fitness = 0
        self.distance = 0
        self.brain = NeuralNetwork(9,4,2)
    def showBar(self,x,y):
        pygame.draw.rect(Game.gameDisplay,Game.black,[x,y,self.length,self.height])

    def showBall(self,x,y):
        pygame.draw.circle(Game.gameDisplay,Game.gray,(int(x),int(y)),self.radius)

    def predict(self):
        # Quadrant I
        if self.ball_center_x > self.center_x:
            dis1 = self.calculateDistance((self.ball_center_x),(self.ball_center_y+self.radius))
        else:
            dis1 = -1
        dis1/= 1000

        if self.ball_center_x < self.center_x:
            dis2 = self.calculateDistance((self.ball_center_x),(self.ball_center_y+self.radius))
        else:
            dis2 = -1
        dis2/= 1000

        if self.ball_center_x == self.center_x:
            dis3 = self.calculateDistance((self.ball_center_x),(self.ball_center_y+self.radius))
        else:
            dis3 = -1
        dis3/=1000

        vel_x = self.ball_vel_x
        vel_x/=1000

        vel_y = self.ball_vel_y
        vel_y /= 1000

        dis_wall1 = self.bar_x
        dis_wall2 = (Game.width) -(self.bar_x)

        dis_ball1 = math.sqrt((self.ball_center_x-self.bar_x)**2+(self.ball_center_y+self.radius-(Game.height-self.height))**2)
        dis_ball2 = math.sqrt((self.ball_center_x-(self.bar_x+self.length))**2+(self.ball_center_y+self.radius-(Game.height-self.height))**2)

        dis_wall1/=Game.width
        dis_wall2/=Game.width
        dis_ball1/=1000
        dis_ball2/=1000

        inputs = [dis1,dis2,dis3,dis_wall1,dis_wall2,dis_ball1,dis_ball2,vel_x,vel_y]
        inputs = np.array(inputs)
        inputs = np.reshape(inputs,(9,1))
        output = self.brain.feedforward(inputs)
        if output[0]>output[1]:
            self.moveRight()
        else:
            self.moveLeft()


    def moveLeft(self):
        if self.bar_x != 0:
            self.bar_x -= 10
            self.center_x -= 10
            self.distance += 1
    def moveRight(self):
        if self.bar_x != (Game.width - self.length):
            self.bar_x += 10
            self.center_x += 10
            self.distance += 1

    def updateVelocity(self):
        self.ball_center_x += self.ball_vel_x
        self.ball_center_y += self.ball_vel_y

    def isColliding(self):
        if (self.ball_center_y + self.radius) >= (Game.height - self.height):
            if self.ball_center_x >= self.bar_x and self.ball_center_x <= (
                    self.bar_x + self.length):
                return True
    def isCollidingSide(self):
        if self.ball_center_x >= Game.width or self.ball_center_x - self.radius <= 0:
            return True

    def isCollidingAbove(self):
        if self.ball_center_y <= 0:
            return True
    def calculateDistance(self,x,y):
        return math.sqrt((self.center_x-x)**2+(self.center_y-y)**2)


class Game():
    width = 900
    height = 600
    black = (0,0,0)
    gray = (70,70,70)
    gameDisplay = pygame.display.set_mode((width, height))
    population = 200
    generation = 1
    bars = []
    savedBars = []
    highscore = []
    score = []
    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.bar = Bar()
        self.gameLoop()

    def gameLoop(self):
        gameExit = False
        font = pygame.font.SysFont(None,25)
        for i in range(Game.population):
            self.bars.append(Bar())
        while not gameExit:

            msg = 'Gen : ' + str(self.generation)
            screen_text = font.render(msg,True,(0,0,0))
            self.gameDisplay.blit(screen_text,[10,10])
            for bar in self.bars:
                bar.predict()
                bar.updateVelocity()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            print('true')
                            self.showBest()
                if bar.isColliding():
                    bar.ball_vel_y = -bar.ball_vel_y
                    bar.score+=10
                if bar.bar_x == 0 or bar.bar_x == Game.width-bar.length:
                    bar.score -=1
                if len(self.highscore)>0:
                    if bar.score >= max(self.highscore):
                        self.bestBar = bar.brain.serialize()
                        self.highscore.append(bar.score)
                if bar.isCollidingSide():
                    bar.ball_vel_x = -bar.ball_vel_x
                if bar.isCollidingAbove():
                    bar.ball_vel_y = -bar.ball_vel_y
                if bar.ball_center_y > Game.height:
                    self.savedBars.append(bar)
                    self.score.append(bar.score)
                    self.bars.remove(bar)
                    if len(self.bars) == 0:
                        self.generation +=1
                        self.highscore.append(max(self.score))
                        self.score = []
                        ga = GA(self)
                        ga.nextGen()

                bar.showBar(bar.bar_x,bar.bar_y)
                bar.showBall(bar.ball_center_x,bar.ball_center_y)
            pygame.display.update()
            self.gameDisplay.fill((135,206,250))
            self.clock.tick(60)
        pygame.quit()
        quit()

    def showBest(self):
        self.gameDisplay.fill((135,206,250))
        bar = Bar()
        bar.brain = pickle.loads(self.bestBar)
        gameExit = False
        while not gameExit:
            bar.predict()
            bar.updateVelocity()
            if bar.isColliding():
                bar.ball_vel_y = -bar.ball_vel_y
                bar.score += 1
            if bar.isCollidingSide():
                bar.ball_vel_x = -bar.ball_vel_x
            if bar.isCollidingAbove():
                bar.ball_vel_y = -bar.ball_vel_y
            if bar.ball_center_y > Game.height:
                return
            pygame.display.update()
            self.gameDisplay.fill((135,206,250))
            self.clock.tick(30)
        pygame.quit()
        quit()


class GA(Game):
    def __init__(self,game):
        self.game = game

    def nextGen(self):
        self.calculateFitness()
        for i in range(len(self.savedBars)):
            self.game.bars.append(self.pickOne())
        self.game.savedBars = []
        self.savedBars = []

    def calculateFitness(self):
        sum = 0
        self.savedBars = self.game.savedBars
        for i in range(len(self.savedBars)):
            self.savedBars[i].fitness = (self.savedBars[i].score)**2 + (pow(2,self.savedBars[i].distance))
            sum+= self.savedBars[i].fitness

        for i in range(len(self.savedBars)):
            self.savedBars[i].fitness/= sum


    def pickOne(self):
        r = random.uniform(0,1)
        index = 0
        while r>0:
            r = r-self.savedBars[index].fitness
            index+=1
        index-=1

        r2 = random.uniform(0,1)
        index2 = 0
        while r2>0:
            r2 = r2-self.savedBars[index2].fitness
            index2 +=1
        index2-=1

        child = Bar()
        bar = self.savedBars[index]
        bar2 = self.savedBars[index2]
        child.brain.in_hidden1_weights = bar.brain.crossover(bar.brain.in_hidden1_weights,bar2.brain.in_hidden1_weights)
        child.brain.in_hidden1_biases = bar.brain.crossover(bar.brain.in_hidden1_biases,bar2.brain.in_hidden1_biases)
        child.brain.hidden1_output_weights = bar.brain.crossover(bar.brain.hidden1_output_weights,bar2.brain.hidden1_output_weights)
        child.brain.hidden1_output_biases = bar.brain.crossover(bar.brain.hidden1_output_biases,bar2.brain.hidden1_output_biases)

        child.brain.mutate(child.brain.in_hidden1_weights,0.3)
        child.brain.mutate(child.brain.in_hidden1_biases,0.3)
        child.brain.mutate(child.brain.hidden1_output_weights,0.3)
        child.brain.mutate(child.brain.hidden1_output_biases,0.3)

        return child


if __name__ == '__main__':
    game = Game()