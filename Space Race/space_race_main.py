import pygame
import math
import random


class Border:
    def __init__(self,window):
        self.window = window
        self.height = 400
        self.height_change = 2
        
    
    def draw(self):
        self.rectangle = pygame.Rect(400,300,10,self.height)
        pygame.draw.rect(self.window,(255,255,255),self.rectangle)



class Asteroid:
    def __init__(self,window):
        self.window = window
        self.image = pygame.image.load("/Users/dunura/Desktop/Programming/Python_work/Space Race/meteorite.png")
        self.x = random.randint(0,800)
        self.y = random.randint(0,550)
        self.x_change = -3
    
    def draw(self):
        self.window.blit(self.image,(self.x,self.y))
        self.x += self.x_change
        


class Ship:
    def __init__(self, window):
        self.window = window

        self.image = pygame.image.load("/Users/dunura/Desktop/Programming/Python_work/Space Race/space-shuttle.png")

        self.x = 136
        self.y = 620

        self.direction = "still"

        self.y_change = 0
    
    def draw(self):
        self.window.blit(self.image,(self.x,self.y))
        
        self.y+=self.y_change




class Game:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((800,700))
        self.background = (0,0,0)


        # SHIP INSTANCES 
        self.ship1 = Ship(self.window)
        self.ship2 = Ship(self.window)

        self.ship2.x = 600  # x cooridnate of RIGHT SHIP


        # SCORE
        self.score1 = 0
        self.score2 = 0

        # ASTEROID INSTANCES
        self.asteroids = []

        NUM_OF_ASTEROIDS = 30

        for i in range(NUM_OF_ASTEROIDS):
            i = Asteroid(self.window)
            self.asteroids.append(i)
    

        # BORDER INSTANCE

        self.border = Border(self.window)


    @staticmethod
    def isCollision(x1,y1,x2,y2):
        distance = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
        return distance
    
    def displayScore(self):
        font = pygame.font.SysFont("impact", 100)
        line1 = font.render(f"{self.score1}",True,(255,255,255))
        line2 = font. render(f"{self.score2}",True,(255,255,255))

        self.window.blit(line1,(50,50))
        self.window.blit(line2,(690,50))

    
    def get_winner(self,score1,score2):

        if score1 > score2:
            winner = "PLAYER 1"
        
        if score2 > score1:
            winner = "PLAYER 2"
        
        if score1 == score2:
            winner = "TIE"
        
        return winner
    

    def gameOver(self):
        self.window.fill((0,0,0))
        WINNER = self.get_winner(self.score1,self.score2)
        font = pygame.font.SysFont("impact",60)
        line2 = font.render("Press 'RETURN' to play again",True,(255,255,255))

        if WINNER == "TIE":
            line1 = font.render(f"TIE!",True,(255,255,255))
            self.window.blit(line1,(360,280))
            self.window.blit(line2,(75,370))
            

        
        else:
            line1 = font.render(f"{WINNER} WON!",True,(255,255,255))
            self.window.blit(line1,(225,280))
            self.window.blit(line2,(75,370))
        

        


    

        


    def play(self):
        self.window.fill(self.background)
        self.ship1.draw()
        self.ship2.draw()
        self.displayScore()
        self.border.draw()
        
        
        
        # ASTEROID MECHANICS
        for asteroid in self.asteroids:
            asteroid.draw()
            if asteroid.x <= 0:
                asteroid.x = 800
                asteroid.y = random.randint(0,550)
            

            # CHECK COLLISION BETWEEN ASTEROID AND SHIPS
            if self.isCollision(asteroid.x,asteroid.y,self.ship1.x,self.ship1.y) <= 36:
                self.ship1.y = 620
            
            if self.isCollision(asteroid.x,asteroid.y,self.ship2.x, self.ship2.y) <= 36:
                self.ship2.y = 620




        # SHIP MECHANICS
        if self.ship1.y >= 620:
            self.ship1.y = 620
        
        if self.ship2.y >= 620:
            self.ship2.y = 620
        
        if self.ship1.y <= 0:
            self.ship1.y = 620
            self.score1+=1

        
        if self.ship2.y <= 0:
            self.ship2.y = 620
            self.score2 +=1


        if self.border.height <= 0:
            raise "Game Over"
            

        self.border.height-=0.06
        


    


    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    
                    if event.key == pygame.K_w:
                        self.ship1.y_change = -4
                    

                    if event.key == pygame.K_s:
                        self.ship1.y_change = 4
                    
                    if event.key == pygame.K_UP:
                        self.ship2.y_change = -4
                    
                    if event.key == pygame.K_DOWN:
                        self.ship2.y_change = 4
                    
                    if event.key == pygame.K_RETURN:
                        if pause == True:
                            self.ship1.y = 620
                            self.ship2.y = 620
                            self.border.height = 400
                            self.score1 = 0
                            self.score2 =0
                            pause = False

                    

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        self.ship1.y_change = 0
                    
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.ship2.y_change = 0
                    
                    
                    


                    






            try:
                self.play()
            
            except:

                self.gameOver()
                pause = True
            
            pygame.display.update()
        






if __name__ == "__main__":
    game = Game()
    game.run()