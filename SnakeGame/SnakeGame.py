import random


WIDTH = 20
HEIGHT = 12 

class SnakeGame:
    def __init__(self):
        self.direction = (1,0) # (-1,0) -> left, (0,-1) -> up, (0,1) -> down 
        self.speed = 0.3 # later  
        self.snake = [
            (WIDTH/2, HEIGHT/2), # 10, 6 -> 
            ]
        self.apple = self.new_apple() 
        self.points = 0 # integer
        self.game_over = False # boolean

    def new_apple(self): # will return new point 
        while True:
            apple = (random.randint(0, WIDTH -1), random.randint(0,HEIGHT - 1))
            if apple not in self.snake:
                return apple 
    
    def draw(self):
        print("SNAKE GAME")
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
        else:
            self.apple.pop() # remove last element


    
    def run(self):
        self.draw()
        
        
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