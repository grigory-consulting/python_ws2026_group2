import random
import msvcrt # for windows capture keys from keyboard
import time 
import os 


WIDTH = 40
HEIGHT = 24 

class SnakeGame:
    def __init__(self):
        self.direction = (1,0) # (-1,0) -> left, (0,-1) -> up, (0,1) -> down 
        self.delay = 0.15 # initial delay   
        self.snake = [
            (WIDTH/2, HEIGHT/2), # 10, 6 -> 
            ]
        self.apple = self.new_apple() 
        self.points = 0 # integer
        self.game_over = False # boolean

    def clear_screen(self):
        os.system("cls")

    def new_apple(self): # will return new point 
        while True:
            apple = (random.randint(0, WIDTH -1), random.randint(0,HEIGHT - 1))
            if apple not in self.snake:
                return apple 
    
    def draw(self):
        self.clear_screen()
        print("+" + "-"*WIDTH + "+") # upper boundary of the board
        for y in range(HEIGHT):
            print("|", end="")  
            for x in range(WIDTH):
                if (x,y) == self.apple:
                    print("*", end="") 
                elif (x,y) == self.snake[0]:
                    print("@", end="")
                elif (x,y) in self.snake:
                    print("o", end="")
                else:
                    print(" ", end = "")
            print("|")
        print("+" + "-"*WIDTH + "+") # lower boundary of the board
    
    def update(self):
        head_x, head_y = self.snake[0] # snake head
        new_x = (head_x + self.direction[0]) % WIDTH 
        new_y = (head_y + self.direction[1]) % HEIGHT

        new_head = (new_x,new_y)
        if new_head in self.snake:
            self.game_over = True
            return # end the function here
        
        self.snake.insert(0,new_head)

        if new_head == self.apple:
            self.points +=1
            self.apple = self.new_apple()
            if self.points % 5 == 0: # every 5 points we increase the speed
                self.delay -= 0.01

        else:
            self.snake.pop() # remove last element
    
    def input(self):
        if msvcrt.kbhit():
            key = msvcrt.getch().decode().lower()
            if key == "q":
                self.game_over = True
            elif key == "w" and self.direction != (0,1):
                self.direction = (0,-1)
            elif key == "a" and self.direction != (1,0):
                self.direction = (-1,0)
            elif key == "d" and self.direction != (-1, 0):
                self.direction = (1,0)
            elif key == "s" and self.direction != (0,-1):
                self.direction = (0,1)

    
    def run(self):
        print("SNAKE GAME")
        while not self.game_over:
            self.draw()
            time.sleep(self.delay)
            self.input()
            self.update()
        
game = SnakeGame()
game.run()

"""
******************
*           o    *
*         @oo    *
*                *
*   +            *     
*                *
*                *
*                *
******************
"""
# apple = (4,4)
# snake = [(10,2), (11,2), (12,2), (12,1)]