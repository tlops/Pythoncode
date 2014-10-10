import simplegui

# Event handler
def tick ():
    print "tick!"

# Register handler
timer = simplegui.create_timer(1000, tick)

# start timer
timer.start()
