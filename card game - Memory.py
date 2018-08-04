# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global num_list, exposed, state, index1, index2, turn 
    lst = range(8)
    num_list = lst + lst
    random.shuffle(num_list)
    exposed = [False, False, False, False, False, False, False, False, 
               False, False, False, False, False, False, False, False,]
    state = 0
    index1 = 0
    index2 = 1
    turn = 0

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, index1, index2, turn
    if state == 0:
        state = 1
        index1 = pos[0] // 50
        exposed[index1] = True
    elif state == 1:
        if exposed[pos[0] // 50] == False:
            state = 2 
            index2 = pos[0] // 50
            exposed[index2] = True
            turn += 1
            label.set_text("Turns:" + str(turn))
    else:
        if exposed[pos[0] // 50] == False:
            state = 1
            if num_list[index1] == num_list[index2]:
                index1 = pos[0] // 50
                exposed[index1] = True
            else:
                exposed[index1] = False
                exposed[index2] = False
                index1 = pos[0] // 50
                exposed[index1] = True
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    index1 = 0
    for number in num_list:
        if exposed[index1] == True:
            canvas.draw_text(str(number), [(50 * index1 + 10) , 70], 60, "white")
        index1 += 1
     
    index2 = 0
    for n in exposed:
        if n == False:
            canvas.draw_polygon([[50 * index2, 0], [50 * (index2 + 1), 0], [50 * (index2 + 1), 100], [50 * index2, 100]], 2, "maroon", "green")
        index2 += 1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric