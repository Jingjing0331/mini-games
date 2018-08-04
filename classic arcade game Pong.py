# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [300, 200]
ball_vel = [0, 0]
paddle1_pos = [[0, (HEIGHT - PAD_HEIGHT) / 2], [HALF_PAD_WIDTH, (HEIGHT - PAD_HEIGHT) / 2], 
               [HALF_PAD_WIDTH, (HEIGHT + PAD_HEIGHT) / 2], [0, (HEIGHT + PAD_HEIGHT) / 2]]
paddle2_pos = [[(WIDTH - PAD_WIDTH - 1), (HEIGHT - PAD_HEIGHT) / 2], [(WIDTH - 1), (HEIGHT - PAD_HEIGHT) / 2], 
               [(WIDTH - 1), (HEIGHT + PAD_HEIGHT) / 2], [(WIDTH - PAD_WIDTH - 1), (HEIGHT + PAD_HEIGHT) / 2]]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]
score1 = 0
score2 = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [300, 200]
    if direction: # direction is RIGHT
        ball_vel[0] = random.randrange(120, 240) // 60
        ball_vel[1] = random.randrange(-80, -60) // 60
    else:         # direction is LEFT
        ball_vel[0] = random.randrange(-240, -120) // 60
        ball_vel[1] = random.randrange(-80, -60) // 60 
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = [[0, (HEIGHT - PAD_HEIGHT) / 2], [PAD_WIDTH, (HEIGHT - PAD_HEIGHT) / 2], 
               [PAD_WIDTH, (HEIGHT + PAD_HEIGHT) / 2], [0, (HEIGHT + PAD_HEIGHT) / 2]]
    paddle2_pos = [[(WIDTH - PAD_WIDTH - 1), (HEIGHT - PAD_HEIGHT) / 2], [(WIDTH - 1), (HEIGHT - PAD_HEIGHT) / 2], 
               [(WIDTH - 1), (HEIGHT + PAD_HEIGHT) / 2], [(WIDTH - PAD_WIDTH - 1), (HEIGHT + PAD_HEIGHT) / 2]]
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0]
    score1 = 0
    score2 = 0
    direction = random.randrange(0, 2)
    if direction == 0:
        spawn_ball(RIGHT)
    else:
        spawn_ball(LEFT)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        ball_vel[0] = -ball_vel[0]
    elif ball_pos[0] >= WIDTH - 1 - BALL_RADIUS - PAD_WIDTH:
        ball_vel[0] = -ball_vel[0]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= HEIGHT - 1 - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
            
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if 0 < paddle1_pos[0][1] < HEIGHT - PAD_HEIGHT:
        paddle1_pos[0][1] = (paddle1_vel[1]+paddle1_pos[0][1]) 
        paddle1_pos[1][1] = (paddle1_vel[1]+paddle1_pos[1][1]) 
        paddle1_pos[2][1] = (paddle1_vel[1]+paddle1_pos[2][1]) 
        paddle1_pos[3][1] = (paddle1_vel[1]+paddle1_pos[3][1]) 
    elif paddle1_pos[0][1] <= 0 and paddle1_vel[1] > 0 or paddle1_pos[0][1] >= HEIGHT - PAD_HEIGHT and paddle1_vel[1] < 0:
        paddle1_pos[0][1] = (paddle1_vel[1]+paddle1_pos[0][1]) 
        paddle1_pos[1][1] = (paddle1_vel[1]+paddle1_pos[1][1]) 
        paddle1_pos[2][1] = (paddle1_vel[1]+paddle1_pos[2][1]) 
        paddle1_pos[3][1] = (paddle1_vel[1]+paddle1_pos[3][1])
   
    if 0 < paddle2_pos[0][1] < HEIGHT - PAD_HEIGHT:
        paddle2_pos[0][1] = (paddle2_vel[1]+paddle2_pos[0][1]) 
        paddle2_pos[1][1] = (paddle2_vel[1]+paddle2_pos[1][1]) 
        paddle2_pos[2][1] = (paddle2_vel[1]+paddle2_pos[2][1]) 
        paddle2_pos[3][1] = (paddle2_vel[1]+paddle2_pos[3][1]) 
    elif paddle2_pos[0][1] <= 0 and paddle2_vel[1] > 0 or paddle2_pos[0][1] >= HEIGHT - PAD_HEIGHT and paddle2_vel[1] < 0:
        paddle2_pos[0][1] = (paddle2_vel[1]+paddle2_pos[0][1]) 
        paddle2_pos[1][1] = (paddle2_vel[1]+paddle2_pos[1][1]) 
        paddle2_pos[2][1] = (paddle2_vel[1]+paddle2_pos[2][1]) 
        paddle2_pos[3][1] = (paddle2_vel[1]+paddle2_pos[3][1])
    
    # draw paddles
    c.draw_polygon(paddle1_pos, 1, "white","white")
    c.draw_polygon(paddle2_pos, 1, "white","white")              
    
    # draw scores
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS and (ball_pos[1] < paddle1_pos[0][1] or ball_pos[1] > paddle1_pos[3][1]):
        score2 = score2 + 1
        spawn_ball(RIGHT)
    if ball_pos[0] >= WIDTH - 1 - PAD_WIDTH - BALL_RADIUS and (ball_pos[1] < paddle2_pos[0][1] or ball_pos[1] > paddle2_pos[3][1]):
        score1 = score1 + 1
        spawn_ball(LEFT)
    c.draw_text(str(score1), [200, 100], 50, "white")
    c.draw_text(str(score2), [400, 100], 50, "white")
    # update velocity
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS and paddle1_pos[0][1] <= ball_pos[1] <= paddle1_pos[3][1] or ball_pos[0] >= WIDTH - 1 - PAD_WIDTH - BALL_RADIUS and paddle2_pos[0][1] <= ball_pos[1] <= paddle2_pos[3][1]:
        ball_vel[0] = ball_vel[0] * 1.1
        ball_vel[1] = ball_vel[1] * 1.1
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = -5
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 5
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = -5
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 5
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0

def reset():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", reset, 50)

# start frame
new_game()
frame.start()
