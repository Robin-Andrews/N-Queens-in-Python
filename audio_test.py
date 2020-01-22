try:
    import simplegui

    queen_image = simplegui.load_image("https://compucademy.co.uk/assets/queen.PNG")
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True
    simplegui.Frame._keep_timers = False
    queen_image = simplegui._load_local_image("queen.PNG")

collision_sound  = simplegui.load_sound("https://compucademy.co.uk/dev/buzz3x.wav")
success_sound = simplegui.load_sound("https://compucademy.co.uk/dev/treasure-found.wav")

def press():
    success_sound.play()

frame = simplegui.create_frame("Test", 400, 400, 100)
frame.add_button("press me", press)
frame.start()