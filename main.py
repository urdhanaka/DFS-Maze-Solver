import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Solving Program")
wn.setup(1300,700)

start_x = 0
start_y = 0
end_x = 0
end_y = 0

# white turtle
class Maze(turtle.Turtle):
    def __init__(self) -> None:
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        
def setup_maze(grid):                          
    global start_x, start_y, end_x, end_y      
    for y in range(len(grid)):                 
        for x in range(len(grid[y])):          
            character = grid[y][x]             
            screen_x = -588 + (x * 24)         
            screen_y = 288 - (y * 24)          

            if character == "+":                   
                maze.goto(screen_x, screen_y)      
                maze.stamp()                       
                walls.append((screen_x, screen_y)) 

            if character == " ":                    
                path.append((screen_x, screen_y))   

            if character == "e":                    
                yellow.goto(screen_x, screen_y)     
                yellow.stamp()                      
                end_x, end_y = screen_x, screen_y   
                path.append((screen_x, screen_y))   

            if character == "s":                       
                start_x, start_y = screen_x, screen_y  
                red.goto(screen_x, screen_y)           

def search(x,y):
    frontier.append((x, y))                            
    solution[x, y] = x, y                              
    while len(frontier) > 0:                           
        time.sleep(0)                                  
        current = (x,y)                                

        if(x - 24, y) in path and (x - 24, y) not in visited:  
            cellleft = (x - 24, y)
            solution[cellleft] = x, y  
            blue.goto(cellleft)        
            blue.stamp()               
            frontier.append(cellleft)  

        if (x, y - 24) in path and (x, y - 24) 
            celldown = (x, y - 24)
            solution[celldown] = x, y  
            blue.goto(celldown)
            blue.stamp()
            frontier.append(celldown)

        if(x + 24, y) in path and (x + 24, y) not in visited:   
            cellright = (x + 24, y)
            solution[cellright] = x, y  
            blue.goto(cellright)
            blue.stamp()
            frontier.append(cellright)

        if(x, y + 24) in path and (x, y + 24) not in visited:  
            cellup = (x, y + 24)
            solution[cellup] = x, y  
            blue.goto(cellup)
            blue.stamp()
            frontier.append(cellup)

        x, y = frontier.pop()           
        visited.append(current)         
        green.goto(x,y)                 
        green.stamp()                   
        if (x,y) == (end_x, end_y):     
            yellow.stamp()              
        if (x,y) == (start_x, start_y): 
            red.stamp()                 

def backRoute(x, y):                       
    yellow.goto(x, y)                      
    yellow.stamp()
    while (x, y) != (start_x, start_y):    
        yellow.goto(solution[x, y])        
        yellow.stamp()                     
        x, y = solution[x, y]             
