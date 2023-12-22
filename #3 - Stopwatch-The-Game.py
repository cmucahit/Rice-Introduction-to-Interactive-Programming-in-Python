# template for "Stopwatch: The Game"
import simplegui
import math

# define global variables
position = [60, 110]
interval = 100
time = 0
success = 0
tries = 0
running = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = 0
    seconds = 0
    tenths = 0
    
    tenths = str(t % 10)
    
    seconds = (t // 10) % 60
    
    minutes = str(t // 600)
    
    if seconds < 10:
        seconds = str(0) + str(seconds)
    else:
        seconds = str(seconds)
        
    if minutes < 1:
        minutes = str(0) + str(minutes)
        
    return minutes + ":" + seconds + "." + tenths
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    
    timer.start()
    
    running = True
    
def stop():
    global tries
    global success
    global running
    
    if running == True:
        tries += 1
        if time % 10 == 0:
            success += 1
    
    timer.stop()
    running = False
    
def reset():
    global time
    global tries
    global success
    
    timer.stop()
    running = False
    
    time = 0
    tries = 0
    success = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    
    time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), position, 36, "Red")
    
    # create score string
    score_string = str(success) + "/" + str(tries)
    
    canvas.draw_text(score_string, [110,30], 36, "Blue")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 200)


# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)

# start frame
frame.start()
