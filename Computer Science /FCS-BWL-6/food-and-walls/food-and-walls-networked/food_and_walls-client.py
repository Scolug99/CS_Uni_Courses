# Inspired by https://github.com/us/Turtle-Game

import turtle
import math
import random
import time
import socket

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 480

# Create the player game element as a global variable
player = turtle.Turtle()

# Create the player's score count as a global variable
score = 0

def random_x_coordinate():
    return random.randint(-SCREEN_WIDTH/2,SCREEN_WIDTH/2)
    
def random_y_coordinate():
    return random.randint(-SCREEN_HEIGHT/2,SCREEN_HEIGHT/2)
    
def turn_left():
    player.setheading(180)

def turn_right():
    player.setheading(0)

def turn_up():
    player.setheading(90)

def turn_down():
    player.setheading(270)

def detect_collision(game_element_1, game_element_2):
    # Calculate cartesian distance between the given game elements. Signal a collision if the distance is lower than 20
    d = math.sqrt(math.pow(game_element_1.xcor() - game_element_2.xcor(), 2) + math.pow(game_element_1.ycor() - game_element_2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False
        
def enforce_infinite_screen():
    # Make game elements move to ("reappear at") the opposite side of the screen when they are about to leave the screen. If the game_element leaves the screen, just move it "back" by SCREEN_WIDTH (at the sides) or SCREEN_HEIGHT (at the top and bottom)
    if (player.xcor() > (SCREEN_WIDTH / 2)) or (player.xcor() < -(SCREEN_WIDTH / 2)):
        player.backward(SCREEN_WIDTH)
	
    if (player.ycor() > (SCREEN_HEIGHT / 2)) or (player.ycor() < -(SCREEN_HEIGHT / 2)):
        player.backward(SCREEN_HEIGHT)
    
def main():
    # score will be modified, so we need to declare it as global
    global score
    
    # Set initial game speed (i.e., how many pixels the player moves per tick)
    speed = 1
    
    # Get player name
    player_name = input("Enter your name: ")
        
    # Wait a few seconds before starting the game
    time.sleep(3)
    
    
    ## Setup game elements (using the turtle library for graphics)

    # Setup a black window
    window = turtle.Screen()
    window.bgcolor("black")
    window.setup(SCREEN_WIDTH + 10, SCREEN_HEIGHT + 10)
    window.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.tracer(2)
    
    # Create player
    player.color("cyan")
    player.shape("triangle")
    player.penup()

    # Create num_walls walls at random locations
    num_walls = 10
    walls = []

    for wall_index in range(num_walls):
        # Create a new Turtle game object for each wall
        walls.append(wall_index)
        walls[wall_index] = turtle.Turtle()
        walls[wall_index].shape("square")
        walls[wall_index].color("yellow3")
        walls[wall_index].penup()
        walls[wall_index].speed(0)
        walls[wall_index].setposition(random_x_coordinate(),random_y_coordinate())

    # Create food at a random location
    food = turtle.Turtle()
    food.penup()
    food.shape("square")
    food.color("blue")
    food.setposition(random_x_coordinate(), random_y_coordinate())

    # Setup event handlers (i.e., when the user presses the "Left" arrow key, then the function turn_left() shall be called). This is easy thanks to the turtle library
    turtle.listen()
    turtle.onkey(turn_left, "Left")
    turtle.onkey(turn_up, "Up")
    turtle.onkey(turn_down, "Down")
    turtle.onkey(turn_right, "Right")
  
    server_IP = "130.82.171.2" # "130.82.171.2" 
    serverAddressPort = (server_IP, 5678)
    myClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    bufferSize = 1024

    # Execute main game loop "forever"
    while True:
        
        # Move player's ship forward
        player.forward(speed)
        
        # Test "collisions" of the player's ship with window borders
        enforce_infinite_screen()
                            
        # Detect collision of the player's ship with food            
        if detect_collision(player, food):
            # If there is a collision, increase speed and score
            score += 10
            speed += 0.5
                        
            # Move food to new random position
            food.setposition(random_x_coordinate(),random_y_coordinate())
            
            print("+10 Points :-)")
                    
        # Detect collisions of the player's ship with all walls
        for wall_index in range(num_walls):
            if detect_collision(player, walls[wall_index]):
                print("Game Over! Your score: ", score)
                
                # TODO Send score message to server. Format: "Score <playername> score"
				# Example: "Score simon 110"
                messageToSend = "Score " + player_name + " " + str(score)
                print("Sending:", messageToSend)
				
                bytesToSend = str.encode(messageToSend)
                myClientSocket.sendto(bytesToSend, serverAddressPort)                
                
				# Exit the game
                window.bye()
                exit()                
        
        # Uncomment the following line for debugging output
        # print("Player coordinates:", player.xcor(), player.ycor())
        
        # Wait for 10 milliseconds, then loop again
        time.sleep(0.01)

if __name__ == '__main__':
    main()
