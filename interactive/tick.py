import os
import sys
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Event handler
def tick ():
    print "tick!"

# Register handler
timer = simplegui.create_timer(1000, tick)

# start timer
timer.start()
