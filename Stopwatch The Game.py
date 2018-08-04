# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
counter = 0
success = 0
tostop = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenth_sec = t % 10
    t = t // 10 
    second = t % 60
    minute = t // 60
    if second < 10:
        display = str(minute) + ":" + "0" + str(second) + "." + str(tenth_sec)
    else:
        display = str(minute) + ":" + str(second) + "." + str(tenth_sec)
    return display
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start():
    global tostop
    timer.start()
    tostop = True
  
def button_stop():
    global counter, success, tostop
    timer.stop()
    if tostop:
        counter = counter +1
        if time % 10 == 0:
            success = success + 1
    tostop = False
    
def button_reset():
    global counter, success, time
    timer.stop()
    counter = 0
    success = 0 
    time = 0
    
   

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time = time + 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [30,85], 50, "White")
    canvas.draw_text(str(success)+"/"+str(counter), [150,25], 24, "Green")
    
    
# create frame
frame = simplegui.create_frame("Stopwacth", 200, 150)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.add_button("Start", button_start, 100)
frame.add_button("Stop", button_stop, 100)
frame.add_button("Reset", button_reset, 100)
frame.set_draw_handler(draw)

# start frame
frame.start()

# Please remember to review the grading rubric
